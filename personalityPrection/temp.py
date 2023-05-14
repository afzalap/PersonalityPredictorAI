import os

# Path to the file
file_path = 'models/Emotional_Stability_model.pickle'

# Check if the file exists
if os.path.isfile(file_path):
    print('File exists')
else:
    print('File does not exist')
