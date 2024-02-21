from typing import Callable

def decorator(*args, **kwargs):
    '''
        @params:    - args (tuple): Variable length arguments.
                    - kwargs (dict): Keyword arguments.

        @deas:      A decorator that can be used with or without arguments.    
                    If used without arguments, it's applied without parentheses.
                    If used with an argument, it's applied with parentheses.
        
        @return:   - callable: The decorator function.
    '''
    def decorator_fun(fun: Callable) -> Callable:
        '''
            @params:    - fun (Callable): The function being decorated.
            @desc:      The actual decorator function.        
            @return:    - Callable: The wrapped function.
        '''
        def wrapper(*args, **kwargs) -> None:
            print('Hello from wrapper function')
            result = fun(*args, **kwargs)
            
            return result
        
        return wrapper

    if len(args) == 1 and callable(args[0]):
        return decorator_fun(args[0])
    else:
        return decorator_fun

@decorator
def my_fun() -> None:
    '''
        @params:    - None
        @desc:      A function decorated without parentheses.
        @return:    - None
    '''
    print('Without ()')

@decorator('habib')
def my_fun_1() -> None:
    '''
        @params:    - None
        @desc:      A function decorated parentheses.
        @return:    - None
    '''
    print('With ()')

my_fun()
my_fun_1()
