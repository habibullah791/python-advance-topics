class RangeValidator:
    def __init__(self, name: str, min_value: int, max_value: int):
        """
            @param :    The minimum allowed value for the attribute.
                        The maximum allowed value for the attribute.
            @desc:      Initialize the RangeValidator descriptor.
            @returns:   None
        """
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        """
            @param:     The instance of the class.
                        The class owning the descriptor.
            @desc:      Get the value of the attribute.
            @returns:   The value of the attribute.
        """
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
            @param:     The instance of the class.
                        The value to be set.
            @desc:      Set the value of the attribute, performing range validation.
            @returns:   The value of the attribute.
        """
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"{self.name} must be between {self.min_value} and {self.max_value}")
        instance.__dict__[self.name] = value

class MyClass:
    age = RangeValidator("age", 0, 120)

    def __init__(self, name: str, age: int):
        """
            @desc:      Initialize the MyClass instance.
            @param:     The name of the person.
                        The age of the person.
            @returns: None
        """
        self.name = name
        self.age = age



obj = MyClass("Alice", 25)

print(obj.age)
obj.age = 30

try:
    obj.age = 150
except ValueError as e:
    print(e)
