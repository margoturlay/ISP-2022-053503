import toml
from serializer.serializer import serialize_object


class TomlParser:

    def dumps(self, obj) -> str:
        self.replace_null(obj)
        return toml.dumps(obj)

    def dump(self, obj, file="parsed_file/parsed.toml"):
        packed = serialize_object(obj)
        with open(file, 'w') as fw:
            toml.dump(packed, fw)

    def loads(self, obj: str):
        loaded = toml.loads(obj)
        self.replace_null_back(loaded)
        return loaded

    def load(self, file="parsed_file/parsed.toml"):
        try:
            with open(file, "r") as fp:
                data = fp.read()
        except FileNotFoundError:
            raise FileNotFoundError("file doesn't exist")
        return toml.loads(data)

    def replace_null(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if value is None:
                    obj[key] = "null"
                self.replace_null(value)
        if isinstance(obj, list):
            for i in range(len(obj)):
                if obj[i] is None:
                    obj[i] = "null"
                self.replace_null(obj[i])

    def replace_null_back(self, obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if value == "null":
                    obj[key] = None
                else:
                    self.replace_null_back(value)

        if isinstance(obj, list):
            for i in range(len(obj)):
                if obj[i] == "null":
                    obj[i] = None
                else:
                    self.replace_null_back(obj[i])



