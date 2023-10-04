import time


def cal_execution_time(function):
    '''
        @params: Function to be decorated
        @description: This function will measure and print the execution time of the function
        @returns: function ( Decorated Function )
    '''
    
    def wrapper(*args, **kwargs):
        '''
            @params:   *args: Positional arguments passed to the decorated function.
                       **kwargs: Keyword arguments passed to the decorated function.
            @description: This function will measure the execution time of the decorated function
            @returns: Sum of series of numbers : result of the decorated functin
        '''
        start_time = time.time()
        # Pass the arguments to the wrapped function
        result = function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(
            f'Function {function.__name__} took {execution_time:.4f} seconds to execute')

        return result

    return wrapper


@cal_execution_time
def add_series_of_num(number: int) -> int:
    '''
        @params: number
        @description: This function will measure the sum from 0 to that number
        @returns: sum of series of number 
    '''
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum


result = add_series_of_num(1000)  # Call the decorated function
print(f'Sum is : {result}')
