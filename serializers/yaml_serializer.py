from serialization import serialize_object, deserialize_object
from serializers.parser_sk import Parser
from yaml import dump as dumps, full_load as loads


class YamlSerializer(Parser):
    @staticmethod
    def dumps(obj) -> str:
        return dumps(obj)

    @staticmethod
    def dump(obj, file="testyaml.yaml"):
        with open(file, 'w+') as fw:
            dumps(obj, fw)

    @staticmethod
    def loads(obj: str):
        return loads(obj)

    @staticmethod
    def load(file="testyaml.yaml"):
        with open(file, 'r+') as fr:
            return loads(file)
