# Generated by Django 3.2.3 on 2021-08-03 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('post_type', models.CharField(choices=[('c', 'Commercial'), ('a', 'Author')], max_length=1)),
                ('image', models.ImageField(upload_to='uploads')),
                ('issued', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.author')),
            ],
        ),
    ]
