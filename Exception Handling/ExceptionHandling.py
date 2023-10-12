import os

class InvalidAgeException(Exception):
    '''
    @params:age (int): The age value that caused the exception.
            message (str): The error message associated with the exception.
    @desc:  Exception for invalid age when checking voting eligibility.
    @returns: None
    '''
    def __init__(self, age: int, message: str = "Can't cast vote: Age is not greater than 18") -> None:
        self.age = age
        self.message = message
        super().__init__(self.message)

class CustomFileNotFoundException(Exception):
    '''
    @params: file_path (str): The file path that caused the exception.
             message (str): The error message associated with the exception.
    @desc:   Exception for a file not found error.
    @returns:None
    '''
    def __init__(self, file_path: str, message: str = 'File not found') -> None:
        self.file_path = file_path
        self.message = message
        super().__init__(self.message)

def is_eligible(age: int) -> None:
    '''
    @params: age (int): The age to be checked for eligibility.
    @desc:   Check the eligibility for casting a vote based on age.
    @returns:None
    @raises: InvalidAgeException: If the age is less than 18.
    '''
    if age < 18:
        raise InvalidAgeException(age)
    else:
        print('Can cast a vote')


if __name__ == '__main':
    try:
        age = int(input('Enter the age: '))
        is_eligible(age)
    except InvalidAgeException as e:
        print('Error message:', e)
    
    try:
        file_path = input('Enter file name: ')
        if not os.path.exists(file_path):
            raise CustomFileNotFoundException(file_path)
    except CustomFileNotFoundException as e:
        print('Error message:', e)
