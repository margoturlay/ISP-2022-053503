from serializer.serializer import serialize_object, deserialize_object
from serializer.parsers.parser import Parser
import math

import unittest

test_number = 228
test_dict = {'l': 'qwe', 'b': 123, 228: 456.789}
test_list = [1, 'qwe', 3, 22.8, test_dict, (1, 2, 3), True, None]
test_tuple = (test_dict, test_number, 'okey')



def test_mul(n):
    return n * 2


def test_fact(n):
    if n == 0:
        return 1
    else:
        return n * test_fact(n - 1)


def test_wrapper(n):
    return test_fact(n - 1) * n


def test_vars(n):
    return test_list, n


test_dict_func = {test_wrapper: test_fact}


def serialize_and_compare_obj(obj, tester):
    ser = serialize_object(obj)
    res = deserialize_object(ser)
    tester.assertEqual(res, obj)


def serialize_and_compare_func(func, tester):
    ser = serialize_object(func)
    res = deserialize_object(ser)
    tester.assertEqual(res(2), func(2))


def parse_and_compare_func(func, format, tester):
    format = format.lower()
    p = Parser(format)
    file = f'../output/output.{format}'
    p.dump(func, file)
    res = p.load(file)
    tester.assertEqual(res(2), func(2))

c = 42
def f(x):
    a = 123
    return math.sin(a * x * c)


class TestClass(unittest.TestCase):
    def test_serialization_obj(self):
        serialize_and_compare_obj(test_number, self)
        serialize_and_compare_obj(test_dict, self)
        serialize_and_compare_obj(test_list, self)

    def test_serialization_func(self):
        serialize_and_compare_func(test_mul, self)

    def test_parse_json(self):
        parse_and_compare_func(test_mul, 'json', self)
        parse_and_compare_func(test_mul, 'jSoN', self)

    def test_parse_toml(self):
        parse_and_compare_func(test_mul, 'toml', self)
        parse_and_compare_func(test_mul, 'toMl', self)

    def test_parse_yaml(self):
        parse_and_compare_func(test_mul, 'yaml', self)
        parse_and_compare_func(test_mul, 'yAmL', self)

    def test_parse_err(self):
        res = False
        try:
            p = Parser.create_parser('err')
        except ValueError:
            res = True
        self.assertTrue(res)

    def test_complex_dict(self):
        ser = serialize_object(test_mul)
        res = deserialize_object(ser)
        self.assertEqual(res(2), test_mul(2))

    def test_complex_list(self):
        ser = serialize_object(test_list)
        res = deserialize_object(ser)
        self.assertEqual(test_list, res)

    def test_number(self):
        ser = serialize_object(test_number)
        res = deserialize_object(ser)
        self.assertEqual(test_number, res)

    def test_tuple(self):
        ser = serialize_object(test_tuple)
        res = deserialize_object(ser)
        self.assertEqual(test_tuple, res)


