from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Post, Author
from .forms import AddPost
import datetime

def home(request):

    all_posts = Post.objects.all()

    viewed_posts = request.session.get("viewed_posts", {})
    print(viewed_posts)
    return render(request, 'home.html', {'posts': all_posts, 'viewed_posts': viewed_posts})

def post(request, post_id):

    p = Post.objects.get(id=post_id)

    viewed_posts = request.session.get("viewed_posts", {})
    viewed_posts[post_id] = int(post_id)
    request.session["viewed_posts"] = viewed_posts

    return render(request, 'post.html', {'post': p, 'viewed_posts': viewed_posts})

def add_post(request):

    if request.method == "POST":
        
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            post_entity = Post()
            post_entity.title = form.cleaned_data['title']
            post_entity.subtitle = form.cleaned_data['subtitle']
            post_entity.content = form.cleaned_data['content']
            post_entity.post_type = form.cleaned_data['post_type']
            post_entity.image = form.cleaned_data['image']

            post_entity.issued = datetime.datetime.now()
            post_entity.author = Author.objects.get(name = request.user.username)

            post_entity.save()

            return redirect('posts')
    else:
        form = AddPost()

    return render(request, 'add.html', {'form':form})
