def fibonacci_generator() -> int:
    '''
        @params: none
        @desc: You can create a generator object using fibonacci_generator() and then use
            the next() function to obtain the next Fibonacci number in the sequence.
        @Returns: Yields (int) : The next Fibonacci number in the sequence.

    '''
    
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    while True:
        yield a  # Yield the current Fibonacci number
        a, b = b, a + b  # Calculate the next Fibonacci number and update a and b

# Create a generator object
fib_gen = fibonacci_generator()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fib_gen))  # Get the next Fibonacci number from the generator
