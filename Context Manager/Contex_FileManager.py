from contextlib import contextmanager
import time


@contextmanager
def file_manager(file_name: str, mode: str):
    """

        @params:    file_name (str): The name of the file to be opened.
                    mode (str): The mode in which the file should be opened
                    ('r' for reading, 'w' for writing, etc.).

        @desc:A context manager for file handling and also calculate the time taken for this process.
        @Yields:    file: The file object opened in the specified mode.
    """
    start_time = time.time()
    file = open(file_name, mode)
    try:
        yield file
    finally:
        file.close()

        end_time = time.time()
        execute_time = end_time - start_time
        print(f'Total time to write in a file is {execute_time}s')

with file_manager('data.txt', 'w') as f:
    for i in range(1000000):
        f.write(f'Line - {i}\n')
