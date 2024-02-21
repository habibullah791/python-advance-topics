import re

def validate_email(email: str) -> None:
    '''
        @desc:   Validates an email address based on a regular expression pattern.
        @params: email (str): The email address to be validated.
        @returns:None. Prints whether the provided email is valid or not.
    '''

    email_template = r'^[a-zA-Z]+[._]?[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}'
    if re.search(email_template, email):
        print(f'{email} is a Valid Email')
    else:
        print(f'{email} is Not a Valid Email')

if __name__ == '__main__':
    email = input('Enter the Email to Validate: ')
    validate_email(email)
