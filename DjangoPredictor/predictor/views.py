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
from PIL import Image
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

        with Image.open(os.path.join(settings.BASE_DIR, "media", filename)) as img2:
            dpi = img2.info.get('dpi')
            mm_per_px = 25.4 / dpi[0]

        print(mm_per_px)
        predictions, features_list = predict_personality_traits(img, mm_per_px)

        
        traits_img_processing = get_traits(features_list, mm_per_px)
        

        featureValue = {
            'BASE_LINE_ANGLE': str(features_list[0]) +  " deg",
            'TOP_MARGIN': str(features_list[1]) + " % of whole page",
            'LINE_SPACING': str(features_list[2]) + " mm",
            'SLANT_ANGLE': str(features_list[3]) + " deg",
            'WORD_SPACING': str(features_list[4]) + " mm",
            'LETTER_SIZE': str(features_list[5]) + " mm"
        }

        return render(request, 'predict.html', {'predictions': predictions,'img_path': img_path, 'featureValue':featureValue, 'traits_img_processing' : traits_img_processing})
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

def predict_personality_traits(img, mm_per_px):
    # Extract the features from the input image
    
    features_list_ = extract_feature(img)
    indices = [2, 4, 5]  # The indices to multiply with 'x'
    for index in indices:
        features_list_[index] *= mm_per_px
    features_list =[round(float(num), 2) for num in features_list_]
    print(features_list)

    

    

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

        print(prediction)

        # Store the predicted personality trait in the dictionary
        predictions[trait] = prediction

        print(predictions)



    from tabulate import tabulate

    print("\n\n\n")

    table = []
    for trait, prediction in predictions.items():
        table.append([trait, prediction])

    print(tabulate(table, headers=["Trait", "Prediction"]))

    print("\n\n\n")

    return predictions, features_list


def get_traits(features_list, mm_per_px):
    # get_baseline(features_list[0])
    # get_top_margin(features_list[1])
    # get_line_spacing(features_list[2] * mm_per_px)
    # get_slant_of_writing(features_list[3])
    # get_spacing_between_words(features_list[4] * mm_per_px)
    # get_size_of_letters(features_list[5] * mm_per_px)

    traits_img_processing = {
            'BASE_LINE_ANGLE': get_baseline(features_list[0]),
            'TOP_MARGIN': get_top_margin(features_list[1]),
            'SLANT_ANGLE': get_slant_of_writing(features_list[3]),
            'LETTER_SIZE': get_size_of_letters(features_list[5] * mm_per_px)
    }

    return traits_img_processing

def get_size_of_letters(size_of_letters):
    if size_of_letters > 3:
        return "Boldness"
    elif 2.5 < size_of_letters < 3:
        return "Adaptability"
    elif 1.5 < size_of_letters < 2.5:
        return "Modesty"
    return None


def get_slant_of_writing(slant_of_writing):
    if slant_of_writing == 0:
        return "Independence"
    elif 0 < slant_of_writing <= 15:
        return "Empathy"
    elif 16 <= slant_of_writing <= 30:
        return "Goal-orientation"
    elif 31 <= slant_of_writing <= 45:
        return "Passion"
    elif -15 <= slant_of_writing < 0:
        return "Charm"
    elif -30 <= slant_of_writing < -15:
        return "Independence"
    elif -45 <= slant_of_writing < -30:
        return "Evasiveness"
    return None




def get_baseline(baseline):
    if -30 <= baseline <= -5:
        return "Fatigue"
    elif -5 <= baseline <= 5:
        return "Dependability"
    elif 5 <= baseline <= 30:
        return "Ambition"
    return None


def get_top_margin(top_margin):
    if 0 <= top_margin <= 10:
        return "Focus"
    elif 10 <= top_margin <= 20:
        return "Balance"
    elif top_margin > 20:
        return "Creativity"
    return None


def get_spacing_between_words(spacing_between_words):
    if spacing_between_words == "Closely Spaced":
        return "Hostility"
    elif spacing_between_words == "Evenly Spaced":
        return "Self-Confidence"
    elif spacing_between_words == "Widely Spaced":
        return "Extroversion"
    return None

def get_line_spacing(line_spacing):
    if line_spacing == "Heavy":
        return ""

# C=100, gamma=0.5