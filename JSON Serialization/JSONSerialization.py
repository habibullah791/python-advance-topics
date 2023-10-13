import json

class Person:
    def __init__(self, name: str, age: int):
        '''
            @params:    name (str): The name of the person.
                        age (int): The age of the person.
            @desc:      Initialize a Person object.
            @returns:   None
        '''
        self.name = name
        self.age = age
    
    def to_json(self) -> str:
        '''
            @desc:      Serialize the Person object to a JSON-formatted string.
            @returns:   str: A JSON-formatted string representing the Person object.
        '''
        return json.dumps({'name': self.name, 'age': self.age})
    
    @classmethod
    def from_json(cls, json_string: str) -> 'Person':
        '''
            @desc:      Deserialize a Person object from a JSON string.
            @params:    json_string (str): The JSON string representing a Person object.
            @returns:   Person: A new Person object created from the JSON data.
        '''
        data = json.loads(json_string)
        return cls(data['name'], data['age'])

# Example usage:
# Serialization
person = Person('Alice', 30)
json_data = person.to_json()
print('Serialized JSON data:', json_data)

# Deserialization
new_person = Person.from_json(json_data)
print('Deserialized Person object - Name:', new_person.name, ', Age:', new_person.age)
