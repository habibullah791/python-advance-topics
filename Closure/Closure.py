from typing import Callable

def count_function_calls(func: Callable):
    '''
        @params:    func (Callable): The function to be counted.
        @desc:      This function creates a closure that counts the number of calls to a given function.
        @returns:   Callable: A closure that tracks the number of calls to the input function.
    '''
    # Initialize a counter
    count = 0

    def inner_function(*args, **kwargs):
        '''        
            @params:  *args: Positional arguments to be passed to the input function.
                    **kwargs: Keyword arguments to be passed to the input function.
            @desc:    This inner function tracks the number of calls to the input function and prints the count.  
            @returns: Any: The result of the input function.            
        '''
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__} has been called {count} times.')
        return result

    return inner_function

# Define a function you want to track
def add(a: int, b: int) -> int:
    '''
        @desc:      Adds two integers.
        @params:    a (int): The first integer.
                    b (int): The second integer.
        @returns:  int: The sum of the two integers.
    '''
    return a + b

# Create a closure to count calls to the 'add' function
counted_add = count_function_calls(add)

# Call the wrapped function
result = counted_add(3, 4)
print(f'Result: {result}')  # This will print 'Result: 7'

result = counted_add(5, 6)
print(f'Result: {result}')  # This will print 'Result: 11'
