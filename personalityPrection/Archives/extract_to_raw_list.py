import os
import cv2
from extract import extract_feature
import time

start_time = time.time()

directory = 'data'
page_ids = set()

print(os.path)

if os.path.isfile("lists/raw_features"):
    # Check if the feature list file already exists and read in any existing page IDs.
    print("I3enfo: raw_features already exists.")
    with open("lists/raw_features", "r") as f:
        for line in f:
            page_id = line.split()[-1]
            page_ids.add(page_id)

with open("lists/raw_features", "a") as f:
    count = 0
    # Loop through each file in the directory and extract features.
    for file_name in os.listdir(directory):
        if file_name in page_ids:
            # Skip files that have already been processed.
            continue

        img = cv2.imread(os.path.join(directory, file_name))
        print(os.path.join(directory, file_name))
        features = extract_feature(img)

        #rounding everythin to 2 decimal point
        # features = [round(feature, 2) for feature in features]
        # Append the extracted features and file name to the feature list file.
        f.write("\t".join(str(x) for x in features))
        f.write("\t" + file_name + "\n")
        count += 1
        # Print progress to the console.
        progress = (count * 100) // len(os.listdir(directory))
        print(f"{count} {file_name} {progress}%")
    print("Done!")

end_time = time.time()

elapsed_time = end_time - start_time
hours, rem = divmod(elapsed_time, 3600)
minutes, seconds = divmod(rem, 60)

print("Elapsed time: {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))

    



