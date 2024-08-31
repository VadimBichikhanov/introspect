import inspect
import pprint

def introspection_info(obj):
    info = {}
    
    # Тип объекта
    info['type'] = type(obj).__name__
    
    # Атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    
    # Методы объекта
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    
    # Модуль, к которому объект принадлежит
    info['module'] = inspect.getmodule(obj).__name__
    
    # Документация объекта
    info['doc'] = inspect.getdoc(obj)
    
    # Сигнатуры методов
    info['method_signatures'] = {method: str(inspect.signature(getattr(obj, method))) for method in info['methods']}
    
    # Источник кода (если доступен)
    try:
        info['source'] = inspect.getsource(obj)
    except TypeError:
        info['source'] = None
    
    # Иерархия наследования (для классов)
    if inspect.isclass(obj):
        info['inheritance'] = [base.__name__ for base in inspect.getmro(obj)]
    
    return info

# Пример использования
class MyClass:
    """Это документация для MyClass."""
    def __init__(self):
        self.attribute = 42
    
    def my_method(self, param1, param2=None):
        """Это документация для my_method."""
        pass

obj = MyClass()
obj_info = introspection_info(obj)
pprint.pprint(obj_info)