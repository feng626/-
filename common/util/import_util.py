import os
import importlib


def include_settings(package: str, main_dict: dict):
    package_m = importlib.import_module(package)
    for mf in os.listdir(os.path.dirname(package_m.__file__)):
        if not mf.startswith('__'):
            name, _ = os.path.splitext(mf)
            m = importlib.import_module('.' + name, package=package)
            for k in dir(m):
                if not k.startswith('__'):
                    main_dict[k] = getattr(m, k)


def get_reference(cls_func_method):
    return f'{cls_func_method.__module__}.{cls_func_method.__qualname__}'
