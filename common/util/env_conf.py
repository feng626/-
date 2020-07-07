import os

TRUE_VALUES = {
    't', 'T',
    'y', 'Y', 'yes', 'YES',
    'true', 'True', 'TRUE',
    'on', 'On', 'ON',
    '1', 1,
    True
}


class EnvConfMetaClass(type):
    def __new__(cls, name: str, bases, attrs: dict):
        ex_name = ('conf', 'full_name_conf')

        conf = {}
        full_name_conf = {}
        for k, v in attrs.items():
            if not k.startswith('_') and k not in ex_name:
                env_name = f'{name.upper()}_{k.upper()}'
                assert v is not None
                type_clz = type(v)
                ev = os.getenv(env_name, None)
                if ev is not None:
                    if type_clz is bool:
                        if ev in TRUE_VALUES:
                            v = True
                        else:
                            v = False
                    else:
                        v = type_clz(ev)

                conf[k] = v
                full_name_conf[env_name] = v

        attrs.update(conf)

        for n in ex_name:
            attrs[n] = locals()[n]

        return type.__new__(cls, name, bases, attrs)


class EnvConfBase(metaclass=EnvConfMetaClass):
    conf = {}
    full_name_conf = {}
