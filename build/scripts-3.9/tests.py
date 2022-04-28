from serializer.serializer import serialize, deserialize
from serializer.parsers.parser import Parser

import unittest

test_number = 228
test_dict = {"a": "qwe", "b": 123, 228: 456.789}
test_list = [1, "qwe", 3, 22.8, test_dict, (1, 2, 3), True, None]
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
    ser = serialize(obj)
    res = deserialize(ser)
    tester.assertEqual(res, obj)


def serialize_and_compare_func(func, tester):
    ser = serialize(func)
    res = deserialize(ser)
    tester.assertEqual(res(2), func(2))


def parse_and_compare_func(func, format, tester):
    format = format.lower()
    p = Parser(format)
    file = open(f"output/output.{format}", "w")
    p.dump(func, file)
    file.close()
    file = open(f"output/output.{format}", "r")
    res = p.load(file)
    file.close()
    tester.assertEqual(res(2), func(2))


class TestClass(unittest.TestCase):
    def test_serialization_obj(self):
        serialize_and_compare_obj(test_number, self)
        serialize_and_compare_obj(test_dict, self)
        serialize_and_compare_obj(test_list, self)

    def test_serialization_func(self):
        serialize_and_compare_func(test_mul, self)
        serialize_and_compare_func(test_fact, self)
        serialize_and_compare_func(test_wrapper, self)
        serialize_and_compare_func(test_vars, self)

    def test_parse_json(self):
        parse_and_compare_func(test_fact, "json", self)
        parse_and_compare_func(test_fact, "jSoN", self)

    def test_parse_toml(self):
        parse_and_compare_func(test_fact, "toml", self)
        parse_and_compare_func(test_fact, "toMl", self)

    def test_parse_yaml(self):
        parse_and_compare_func(test_fact, "yaml", self)
        parse_and_compare_func(test_fact, "yAmL", self)

    def test_parse_err(self):
        res = False
        try:
            p = Parser.create_parser("err")
        except ValueError:
            res = True
        self.assertTrue(res)

    def test_complex_dict(self):
        #s = Serializer()
        ser = serialize(test_dict_func)
        res = deserialize(ser)
        f1 = list(res)[0]
        f2 = res[f1]
        self.assertEqual(f1(2), test_wrapper(2))
        self.assertEqual(f2(2), test_fact(2))

    def test_complex_list(self):
        ser = serialize(test_list)
        res = deserialize(ser)
        self.assertEqual(test_list, res)

    def test_number(self):
        ser = serialize(test_number)
        res = deserialize(ser)
        self.assertEqual(test_number, res)

    def test_tuple(self):
        ser = serialize(test_tuple)
        res = deserialize(ser)
        self.assertEqual(test_tuple, res)


