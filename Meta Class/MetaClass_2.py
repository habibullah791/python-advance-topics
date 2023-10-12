class Meta(type):
    def __new__(self, class_name, bases, attrs):
        
        a= {}

        for name, value in attrs.items():
            if name.startswith('__'):
                a[name] = value
            else:
                a[name.upper()] = value
                
        print(attrs)

        return type(class_name, bases,a)
    pass


class Dog(metaclass=Meta):
    x =5
    Y =6


d= Dog()

print(d.X)