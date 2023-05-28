import os
import cv2
import csv
from extract import extract_feature
import time
from PIL import Image

start_time = time.time()

directory = 'data'
page_ids = set()

count = 0

print(os.path)

if os.path.isfile("lists/raw_features.csv"):
    # Check if the feature list file already exists and read in any existing page IDs.
    print("I3enfo: raw_features.csv already exists.")
    with open("lists/raw_features.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            page_id = row[-4]
            page_ids.add(page_id)
            count = len(page_ids)

with open("lists/raw_features.csv", "a", newline='') as f:
    writer = csv.writer(f)
    
    # Loop through each file in the directory and extract features.
    for file_name in os.listdir(directory):
        if file_name in page_ids:
            # Skip files that have already been processed.
            continue

        img = cv2.imread(os.path.join(directory, file_name))
        print(os.path.join(directory, file_name))
        features = extract_feature(img)


        with Image.open(os.path.join(directory, file_name)) as img:
            width, height = img.size
            dpi = img.info.get('dpi')
            if dpi:
                print(f"Image size: {width} x {height} pixels")
                print(f"Resolution: {dpi[0]} x {dpi[1]} dpi")
                mm_per_px = 25.4 / dpi[0] # assuming 1 inch = 25.4 mm
                print(f"1 pixel = {mm_per_px:.3f} mm")
            else:
                print("Error: Image DPI not found.")


        #rounding everythin to 2 decimal point
        # features = [round(feature, 2) for feature in features]
        # Append the extracted features and file name to the feature list file.
        writer.writerow(features + [file_name, height, width, dpi[0]])
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
