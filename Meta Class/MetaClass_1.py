# class is of type type, so we can create class with type()



# base class
class Base:
    pass

# add methods 
def add_attributes(self):
    self.z = 8
    self.name = 'Habib'

Test = type('Test', (Base,), {'x': 5, 'add_attributes':add_attributes})

# 'Test' = Name of the class
# () = base we inherit from 
# {} = any attributes 

obj = Test()

print(type(obj))
print(obj.x)
obj.add_attributes()
print(obj.z, obj.name)
