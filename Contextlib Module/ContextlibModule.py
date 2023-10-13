from contextlib import contextmanager
import logging
from typing import IO

@contextmanager
def creating_log(file_name: str, method: str) -> IO[str]:
    '''
        @params:    file_name (str): The name of the file to be opened.
                    method (str): The mode in which the file is opened ('w' for write, 'a' for append, etc.).
        @desc:      A context manager that opens a file and yields the file object for writing.

        @returns:   IO[str]: A file object for writing.

        Raises:
            FileNotFoundError: If the specified file is not found.
            PermissionError: If the program doesn't have the necessary permissions to open the file.
    '''
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        logging.info('Entering: File is opening !!!!!')
        my_file = open(file_name, method)
        yield my_file
    finally:    
        logging.info('Exiting: Data has been written to the file and it\'s closing !!!!')
        my_file.close()

with creating_log('data.txt', 'w') as file:
    file.write('Writing data to file . ')
