import os
from serializer.parsers.parser import Parser


def test_all_parsers(obj):
    path = 'parsed_files/'

    # json parser
    serializer = Parser('json')
    serializer.dump(obj, os.path.join(path, 'parsed.json'))
    result = serializer.load(os.path.join(path, 'parsed.json'))
    print(f'json parser result: {result}')

    # toml parser
    serializer = Parser('toml')
    serializer.dump(obj, os.path.join(path, 'parsed.toml'))
    result = serializer.load(os.path.join(path, 'parsed.toml'))
    print(f'toml parser result: {result}')

    # yaml parser
    serializer = Parser('yaml')
    serializer.dump(obj, os.path.join(path, 'parsed.yaml'))
    result = serializer.load(os.path.join(path, 'parsed.yaml'))
    print(f'yaml parser result: {result}')
    print()


def test_parsers(obj, formt=None, is_func=False):
    path = 'parsed_files/'
    formt = formt.lower()

    # json parser

    if formt == 'json':
        serializer = Parser('json')
        serializer.dump(obj, os.path.join(path, 'parsed.json'))
        result = serializer.load(os.path.join(path, 'parsed.json'))
        if not is_func:
            print(f'json parser result: {result}')
        elif formt == 'json' and is_func:
            return result

    # toml parser
    if formt == 'toml' :
        serializer = Parser('toml')
        serializer.dump(obj, os.path.join(path, 'parsed.toml'))
        result = serializer.load(os.path.join(path, 'parsed.toml'))
        if not is_func:
            print(f'toml parser result: {result}')
        elif formt == 'toml' and is_func:
            return result

    # yaml parser

    if formt == 'yaml':
        serializer = Parser('yaml')
        serializer.dump(obj, os.path.join(path, 'parsed.yaml'))
        result = serializer.load(os.path.join(path, 'parsed.yaml'))
        if not is_func:
            print(f'yaml parser result: {result}')
        elif formt == 'yaml' and is_func:
            return result

