import toml
import pytomlpp
from serialization import serialize_object
from serializers.parser_sk import Parser


class TomlSerializer(Parser):
    @staticmethod
    def dumps(obj) -> str:
        return toml.dumps(obj)

    @staticmethod
    def dump(obj, file="testtoml.toml"):
        packed = serialize_object(obj)
        with open(file, 'w+') as fw:
            toml.dump(packed, fw)

    @staticmethod
    def loads(obj: str):
        return toml.loads(obj)

    @staticmethod
    def load(file="testtoml.toml"):
        try:
            with open(file, "r") as file:
                data = file.read()
        except FileNotFoundError:
            raise FileNotFoundError("file doesn't exist")
        return toml.loads(data)
