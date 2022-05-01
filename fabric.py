from serializers import json_serializer, toml_serializer, yaml_serializer

serializers = {
    "json": json_serializer.JsonSerializer,
    "toml": toml_serializer.TomlSerializer,
    "yaml": yaml_serializer.YamlSerializer
}


class Factory(object):
    @staticmethod
    def create_serializer(file_format: str):
        serializer = serializers.get(file_format.lower(), None)
        return serializer
