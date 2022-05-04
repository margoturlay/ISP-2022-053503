from yaml import dump as dumps, full_load as loads


class YamlParser:
    @staticmethod
    def dumps(obj) -> str:
        return dumps(obj)

    @staticmethod
    def dump(obj, file="parsed_file/parsed.yaml"):
        with open(file, 'w') as fw:
            dumps(obj, fw)

    @staticmethod
    def loads(obj: str):
        return loads(obj)

    @staticmethod
    def load(file="parsed_file/parsed.yaml"):
        with open(file, 'r') as fp:
            return loads(fp)

