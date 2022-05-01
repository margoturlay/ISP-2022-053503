from serializers.json_serializer import JsonSerializer
import math
d = {'a': [1, {'a': 1.1, 'b': None, 'c': {'d': {}, 'a': []}}, 3]}

c = 42


def d(x):
    a = 123
    return math.sin(a * x * c)


s = JsonSerializer.dumps(d)
print(s)
new = JsonSerializer.loads(s)
print(new)
print(type(new))
print(new(123))
print(d(123))
