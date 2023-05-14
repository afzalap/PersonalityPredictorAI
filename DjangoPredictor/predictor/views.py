# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
import cv2
import pickle
import numpy as np
from .extract import *
from django.conf import settings
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# import argparse



def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        img_path = fs.url(filename)
        # os.path.isfile(img_path)
        # img_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images', filename))
        # print(img_path)

        # print("-----------------------" + str( os.path.join(PROJECT_ROOT, img_path)))
        # Call the predict_personality_traits function with the input image path
        # project_root = settings.PROJECT_ROOT
        print(os.path.join(settings.BASE_DIR, "media", filename))
        img = cv2.imread(os.path.join(settings.BASE_DIR, "media", filename))
        # print(os.path.isfile(os.path.join(project_root, img_path)))
        # print(os.path.join(settings.PROJECT_ROOT, img_path))
        # print(os.path.join(project_root, 'media', img_path))
        
        # check if the image was read successfully
        # if img is not None:
        #     print("True")
        # else:
        #     print("False")
        predictions, features_list = predict_personality_traits(img)

        featureValue = {
            'BASE_LINE_ANGLE': str(round(features_list[0], 2)) + " deg",
            'TOP_MARGIN': str(round(features_list[1], 2)) + " % of whole page",
            'LINE_SPACING': str(round(features_list[2] * 0.0846, 2)) + " mm",
            'SLANT_ANGLE': str(round(features_list[3], 2)) + " deg",
            'WORD_SPACING': str(round(features_list[4] * 0.0846, 2)) + " mm",
            'LETTER_SIZE': str(round(features_list[5] * 0.0846, 2)) + " mm"
        }

        return render(request, 'predict.html', {'predictions': predictions,'img_path': img_path, 'featureValue':featureValue})
    return render(request, 'predict.html')


# Define the paths for the saved models
models_dir = os.path.join(settings.BASE_DIR, "models")
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

def predict_personality_traits(img):
    # Extract the features from the input image
    
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

    return predictions, features_list
