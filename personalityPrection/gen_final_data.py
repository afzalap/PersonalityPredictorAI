import os
def is_extroverted(base_line_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size):
    # Determine if the person is extroverted based on the given features
    if letter_size > 3 and -1 < slant_angle <= 1 or top_margin > 20 or line_spacing == "heavy" or word_spacing == "wide":
        return 1
    else:
        return 0


def is_introverted(base_line_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size):
    # Determine if the person is introverted based on the given features
    if letter_size < 2.5 and -15 <= slant_angle < 0 and top_margin < 20 or word_spacing == "closely spaced"  or line_spacing == "normal":
        return 1
    else:
        return 0


def has_emotional_stability(base_line_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size):
    # Determine if the person has emotional stability based on the given features
    if -5 <= base_line_angle <= 5 or word_spacing == "evenly spaced":
        return 1
    else:
        return 0


def is_neurotic(base_line_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size):
    # Determine if the person is neurotic based on the given features
    # or slant_angle in [90, 75, 60, 45, 105, 120, 135]
    if -30 <= base_line_angle <= -5:
        return 1
    else:
        return 0


def is_open_to_experience(base_line_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size):
    # Determine if the person is open to experience based on the given features
    if 2.5 <= letter_size <= 3 and 0 <= slant_angle <= 30 or word_spacing == "evenly spaced" or line_spacing in ["normal", "heavy"]:
        return 1
    else:
        return 0


def is_conscientious(base_line_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size):
    # Determine if the person is conscientious based on the given features
    if 1.5 <= letter_size <= 2.5  and top_margin < 10 or word_spacing == "evenly spaced" :
        return 1
    else:
        return 0


def is_agreeable(base_line_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size):
    # Determine if the person is agreeable based on the given features
    if 2.5 <=letter_size <= 3 and 0 <= slant_angle <= 30 or word_spacing == "evenly spaced" or line_spacing == "normal":
        return 1
    else:
        return 0


import csv
import os

if os.path.isfile("lists/final_data.csv"):
    print("Error: final_data already exists.")
else:
    if os.path.isfile("lists/clean_data.csv"):
        with open("lists/clean_data.csv", "r") as features_file, open("lists/final_data.csv", "w", newline='') as labels_file:
            features_reader = csv.reader(features_file, delimiter=',')
            labels_writer = csv.writer(labels_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for content in features_reader:
                baseline_angle = float(content[0])
                top_margin = float(content[1])
                line_spacing = float(content[2])
                slant_angle = float(content[3])
                word_spacing = float(content[4])
                letter_size = float(content[5])
                file_name = content[6]

                trait_1 = is_extroverted(baseline_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size)
                trait_2 = is_introverted(baseline_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size)
                trait_3 = has_emotional_stability(baseline_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size)
                trait_4 = is_neurotic(baseline_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size)
                trait_5 = is_open_to_experience(baseline_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size)
                trait_6 = is_conscientious(baseline_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size)
                trait_7 = is_agreeable(baseline_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size)

                labels_writer.writerow([baseline_angle, top_margin, line_spacing, slant_angle, word_spacing, letter_size, trait_1, trait_2, trait_3, trait_4, trait_5, trait_6, trait_7, file_name])
        print("Done!")
    else:
        print("Error: feature_list file not found.")


