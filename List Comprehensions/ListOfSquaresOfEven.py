

if __name__ == '__main__':
    
    '''
        Generate a list of squares of even numbers from 1 to 20.
    '''
    square_of_even_numbers : list[int] = [x**2 for x in range(1, 21) if x % 2 == 0]
    print(square_of_even_numbers)
