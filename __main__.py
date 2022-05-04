from tests.test_parsers import test_parsers

import math

c = 42


def f(x):
    a = 123
    return math.sin(a * x * c)


def j(x):
    return x**2**2


if __name__ == '__main__':
    res = test_parsers(j, 'json', True)
    print(res(2))
    print()
    res = test_parsers(f, 'json', True)
    print(res(123))
    res = test_parsers(f, 'yaml', True)
    print(res(123))
    print()


