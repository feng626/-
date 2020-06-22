
class NamedTupleMixin:
    @classmethod
    def create_from_obj(cls, obj):
        return cls(*(getattr(obj, f, None) for f in cls._fields))
