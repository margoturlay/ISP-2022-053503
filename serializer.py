from serialization import deserialize_object, serialize_object


class Serializer:

    @staticmethod
    def serialize_object(obj: object):
        return serialize_object(obj)

    @staticmethod
    def deserialize_object(obj: object):
        return deserialize_object(obj)
