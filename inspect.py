import inspect
from pprint import pprint


def introspection_info(obj):
    info = {}

    info['Type'] = type(obj).__name__

    info['Attributes'] = [attr for attr in dir(obj) if not inspect.ismethod(attr)]

    info['Methods'] = [method for method in dir(obj) if inspect.ismethod(getattr(obj, method))]

    info['Module'] = inspect.getmodule(obj)

    info['Length'] = len(obj)

    return info

number_info = introspection_info('42')
pprint(number_info)