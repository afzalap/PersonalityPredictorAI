import os
import cv2
import pickle
import numpy as np
from extract import *
import argparse
# Define the paths for the saved models
models_dir = 'models'
models = {
    'Extroversion': os.path.join(models_dir, 'Extroversion_model.pickle'),
    'Introversion': os.path.join(models_dir, 'Introversion_model.pickle'),
    'Emotional_Stability': os.path.join(models_dir, 'Emotional_stability_model.pickle'),
    'Neuroticism': os.path.join(models_dir, 'Neuroticism_model.pickle'),
    'Openness_to_Experience': os.path.join(models_dir, 'Openness_to_experience_model.pickle'),
    'Conscientiousness': os.path.join(models_dir, 'Conscientiousness_model.pickle'),
    'Agreeableness': os.path.join(models_dir, 'Agreeableness_model.pickle')
}

# Define the specific features for each personality trait
# [BASE_LINE_ANGLE, TOP_MARGIN, LINE_SPACING, SLANT_ANGLE, WORD_SPACING, LETTER_SIZE]
#  0                   1           2             3           4               5
features = {
    'Extroversion': [5, 3, 2, 1, 4],
    'Introversion': [5, 3, 2, 1, 4],
    'Emotional_Stability': [0, 4],
    'Neuroticism': [0, 3],
    'Openness_to_Experience': [5, 3, 2, 4],
    'Conscientiousness': [5, 2, 1],
    'Agreeableness': [5, 3, 2, 4]
}

def predict_personality_traits(img_path):
    # Extract the features from the input image
    img = cv2.imread(img_path)
    features_list = extract_feature(img)
    # features_list = [0,1,2,3,4,5]

    # Initialize an empty dictionary to store the predicted personality traits
    predictions = {}

    # Loop through each personality trait
    for trait, model_path in models.items():
        # Load the saved model for the current trait
        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        # Extract the specific features for the current trait
        trait_features = np.array(features[trait])
        trait_features_list = [features_list[i] for i in trait_features]
        trait_features_array = np.array(trait_features_list).reshape(1, -1)
        # print(trait)

        # Make a prediction using the loaded model and extracted features
        prediction = model.predict(trait_features_array)[0]

        # Store the predicted personality trait in the dictionary
        predictions[trait] = prediction


    from tabulate import tabulate

    print("\n\n\n")

    table = []
    for trait, prediction in predictions.items():
        table.append([trait, prediction])

    print(tabulate(table, headers=["Trait", "Prediction"]))

    print("\n\n\n")

    

    # return predictions

# img = cv2.imread("/content/drive/MyDrive/Major Project B12 - Shared Folder/T/image processing/FetureExtraction/letter size/cropped.png")
# predict_personality_traits(img)
# extract_feature(img)





# Create an argument parser
parser = argparse.ArgumentParser(description='Predict personality traits from an input image')

# Add an argument for the input image path
parser.add_argument('img_path', type=str, help='path to the input image')

# Parse the command line arguments
args = parser.parse_args()

# Get the input image path from the command line arguments
img_path = args.img_path

# Call the predict_personality_traits function with the input image path
predict_personality_traits(img_path)