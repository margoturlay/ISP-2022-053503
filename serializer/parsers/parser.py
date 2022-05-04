from serializer.parsers.json.json_p import JsonParser
from serializer.parsers.yaml.yaml_p import YamlParser
from serializer.parsers.toml.toml_p import TomlParser

class Parser:
    def __init__(self, parser_name):
        self.parser = self.create_parser(parser_name)

    @staticmethod
    def create_parser(name):
        name.lower()
        if name == 'json':
            return JsonParser()
        if name == 'toml':
            return TomlParser()
        if name == 'yaml':
            return YamlParser()
        raise ValueError

    def dumps(self, obj) -> str:
        return self.parser.dumps(obj)

    def dump(self, obj, file):
        return self.parser.dump(obj, file)

    def loads(self, obj: str):
        return self.parser.loads(obj)

    def load(self, file):
        return self.parser.load(file)



