import csv

'''
    You can iterate over the lines in a file without loading
    them all into memory at once using the standard open function.
    Stackoverflow - Source
'''

# Define the path to your CSV file
csv_file_path = 'MOCK_DATA.csv'

# Open the CSV file in read mode
with open(csv_file_path, mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Read the header
    header = next(csv_reader)
    
    # Determine the indices of the columns you want to extract
    columns_to_extract = [i for i, col_name in enumerate(header) if col_name in ["id", "first_name", "last_name", "gender", "country_code"]]
    
    # Open a new CSV file for writing the extracted data
    output_file_path = 'output.csv'
    with open(output_file_path, mode='w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        
        # Write the header to the output file
        csv_writer.writerow([header[i] for i in columns_to_extract])
        
        '''
            Loop through the input file line by line
            this approach will not load the file to thee memory
        '''
        for row in csv_reader:
            # Extract the columns you need and write them to the output file
            extracted_data = [row[i] for i in columns_to_extract]
            csv_writer.writerow(extracted_data)
