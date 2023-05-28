import csv
import tempfile
import shutil

# Define the input file path
input_file = '/home/afzalu/projects-linux/PersonalityPredictionAIPart/personalityPrection/lists/raw_data.csv'

# Define the column names and values
new_columns = ['height', 'width', 'dpi']
column_values = [1705, 2018, 300]

# Create a temporary file to write the updated rows
temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)

# Open the input CSV file
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    writer = csv.writer(temp_file)

    # Iterate over the rows in the input file
    for i, row in enumerate(reader):

        # Add the new columns to the header row
        if i == 0:
            header_row = row
            header_row.extend(new_columns)

        # Add the column values to each data row
        row.extend(column_values)
        writer.writerow(row)

# Replace the original file with the temporary file
shutil.move(temp_file.name, input_file)
