class DocstringMeta(type):
    def __new__(cls, class_name, bases, attrs):
        print(attrs)
        for attr_name, attr_value in attrs.items():
            # print(attr_name, attr_value)
            # print(attr_value)
            if callable(attr_value) or isinstance(attr_value, property):
                if not attr_name.startswith('__'):
                    if not attr_value.__doc__:
                        print(attr_name)
                        raise ValueError(f'The method ({attr_name}) should have a docstring')

        
        return super().__new__(cls, class_name, bases, attrs)
    
    
class MyClass(metaclass=DocstringMeta):
    def __init__(self) -> None:
        pass
    
    
    def my_fun(self):
        pass  # this
    
    def my_fun_1(self):
        
        pass


