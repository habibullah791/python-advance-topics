import sys
import os

class DynamicClassGenerator:
    def __init__(self, class_name: str, class_properties: list, class_methods: list):
        '''
            @desc:      Initialize a DynamicClassGenerator instance.
            @params:    The name of the dynamic class to be generated.
                        List of properties (attributes) for the class.
                        List of methods (functions) for the class.
            @returns:   None
        '''
        self.class_name = class_name
        self.class_properties = class_properties
        self.class_methods = class_methods

    def generate_class(self) -> str:
        '''
            @desc:   Generate the Python class string based on the provided properties and methods.
            @params: class instance 
            @return: The generated Python class string.
        '''
        class_string = f'class {self.class_name}:\n'

        for property in self.class_properties:
            class_string += f'\t{property} = None\n'

        for method in self.class_methods:
            class_string += f'\tdef {method}(self):\n\t\tpass\n'

        return class_string

    def save_class(self) -> str:
        '''
            @params: class instance
            @desc:   Generate the class string and save it to a .py file with the same name as the class.
            @return: The generated Python class string.
        '''
        class_string = self.generate_class()

        with open(f'{self.class_name}.py', 'w') as file:
            file.write(class_string)

        return class_string

def get_user_input() -> tuple:
    '''
        @params:    None
        @desc:      Get user input for the class name, properties, and methods.
        @return:    A tuple containing the class name, list of properties, and list of methods.
    '''
    class_name = input('Enter the class name: ')
    class_properties = input('Enter the class properties separated by a comma: ').split(',')
    class_methods = input('Enter the class methods separated by a comma: ').split(',')

    return class_name, class_properties, class_methods

def generate_class():
    '''
        @params:    None
        @desc:      Generate a dynamic class based on user input and save it to a .py file.
        @returns:   None
    '''
    class_name, class_properties, class_methods = get_user_input()
    dynamic_class_generator = DynamicClassGenerator(class_name, class_properties, class_methods)
    dynamic_class_generator.save_class()

def run():
    '''
    Main function to run the program.
    '''
    generate_class()

if __name__ == '__main__':
    run()
