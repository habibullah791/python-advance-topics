class GrandParent:
    def __init__(self, GP_name: str, GP_age: int):
        '''
        Constructor for the GrandParent class.

        @param name: The name of the grandparent (str).
        @param age: The age of the grandparent (int).
        '''
        self.GP_name = GP_name
        self.GP_age = GP_age

    def speak(self) -> None:
        '''
        Method to make the grandparent speak.

        @return: None
        '''
        print(f'Hi! I am grandpa. My name is {self.GP_name}, and I am {self.GP_age} years old')


class Parent:
    def __init__(self, parent_name: str, parent_age: int, occopation: str):
        '''
        Constructor for the Parent class.

        @param name: The name of the parent (str).
        @param age: The age of the parent (int).
        '''
        self.parent_name = parent_name
        self.parent_age = parent_age
        self.occopation = occopation

    def speak(self) -> None:
        '''
        Method to make the parent speak.

        @return: None
        '''
        print(f'Hi! I am Parent. My name is {self.parent_name}, and I am {self.parent_age} years old ')

    def work(self) -> None:
        '''
        Method to simulate the parent working to support the family.

        @return: None
        '''
        print(f'{self.parent_name} is working to support the family and our occupation is {self.occopation}')


class Child(Parent, GrandParent):
    def __init__(self, child_name: str, child_age: int, grandpa_name: str, grandpa_age: int, parent_name: str, parent_age: int, occopation: str):
        '''
        Constructor for the Child class.

        @param child_name: The name of the child (str).
        @param child_age: The age of the child (int).
        @param grandpa_name: The name of the grandparent (str).
        @param grandpa_age: The age of the grandparent (int).
        @param parent_name: The name of the parent (str).
        @param parent_age: The age of the parent (int).
        '''
        self.GP = GrandParent.__init__(self, grandpa_name, grandpa_age)
        Parent.__init__(self, parent_name, parent_age, occopation)
        self.child_name = child_name
        self.child_age = child_age
    def speak(self) -> None:
        '''
        Method to make the child speak.

        @return: None
        '''
        print(f'Hi! I am Child. My name is {self.child_name}, and I am {self.child_age} years old.')

    def play(self) -> None:
        '''
        Method to simulate the child playing and having fun.

        @return: None
        '''
        print(f'{self.child_name} is playing and having fun.')

    def family_info(self):
        '''
        Method to display information about the child's family.

        @return: None
        '''
        print(f'{self.child_name} comes from a family with {self.parent_name} as a parent and {self.GP_name} as a grandparent.')

child = Child('Habib', 23, 'M.Ahmed', 77, 'M.Sharef', 55, "Farmer")

child.speak()
child.play()
child.work()
child.family_info()