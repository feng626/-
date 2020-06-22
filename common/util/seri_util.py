def hump_named(name):
    """
    hump_named -> HumpNamed
    """
    return ''.join([w.title() for w in name.split('_')])


def get_seri(name: str, method: str, action: str, serializers_module):
    _method = method.title()
    clz_names = [
        f'{name}{_method}{hump_named(action)}Serializer',
        f'{name}{hump_named(action)}Serializer',
        f'{name}{_method}Serializer',
    ]
    if action == 'partial_update':
        clz_names.append(f'{name}UpdateSerializer')

    clz_names.append(f'{name}Serializer')
    for clz_name in clz_names:
        if hasattr(serializers_module, clz_name):
            return getattr(serializers_module, clz_name)
