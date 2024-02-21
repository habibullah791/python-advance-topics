from typing import List

# in functional programming 
# 1. we use pue function (functon are impodent)
# 2. Can not change the global state 
# 3. First class higher order functions 
# 4. No side effect 

def sum_of_Square_of_even(nums: List[int]) -> int:
    '''
        @params:  nums (List[int]): A list of numbers.
        @desc:    Calculate the sum of the squares of even numbers in a list.
        @returns: int: The sum of the squares of even numbers in the input list.
    '''
    
    even_numbers = filter(lambda x: x % 2 == 0, nums)
    square_of_even = map(lambda x: x ** 2, even_numbers)
    
    return sum(square_of_even)

result = sum_of_Square_of_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(result)
