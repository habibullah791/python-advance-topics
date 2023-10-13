import time


class CustomContexManager():
    '''
        @params: none
        @desc:  class for measuring the execution time of a block of code.
    '''

    def __init__(self):
        '''
            @params: none
            @desc: Initializes the CustomContextManager.
            @return: none
        '''
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        '''
            @params: none
            @desc: Enter the contex and record the start time 
            @return: none
        '''
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        '''
            @params:    exc_type: The exception type (if an exception occurred).
                        exc_value: The exception value (if an exception occurred).
                        The traceback information (if an exception occurred).
            @desc: Enter the contex and record the end time and print it 
            @return: none
        '''
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        print(f'Time taken to complete is {execution_time}')



with CustomContexManager() as man:
    for _ in range(10000):
        print(_)
