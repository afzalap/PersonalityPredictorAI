import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Read in the dataset
df = pd.read_csv('lists/final_data.csv', names=["BASE_LINE_ANGLE", "TOP_MARGIN", "LINE_SPACING", "SLANT_ANGLE", "WORD_SPACING", "LETTER_SIZE", "Extroversion","Introversion","Emotional_stability","Neuroticism", "Openness_to_experience","Conscientiousness","Agreeableness", "file_name"])

# Define the target variable names and corresponding features
targets = {"Extroversion": ["LETTER_SIZE", "SLANT_ANGLE", "WORD_SPACING", "TOP_MARGIN", "LINE_SPACING"],
           "Introversion": ["LETTER_SIZE", "SLANT_ANGLE", "WORD_SPACING", "TOP_MARGIN", "LINE_SPACING"],
           "Emotional_stability": ["BASE_LINE_ANGLE", "WORD_SPACING"],
           "Neuroticism": ["BASE_LINE_ANGLE", "SLANT_ANGLE"],
           "Openness_to_experience": ["LETTER_SIZE", "SLANT_ANGLE", "WORD_SPACING", "LINE_SPACING"],
           "Conscientiousness": ["LETTER_SIZE", "WORD_SPACING", "TOP_MARGIN"],
           "Agreeableness": ["LETTER_SIZE", "SLANT_ANGLE", "WORD_SPACING", "LINE_SPACING"]}

# targets = {"Extroversion": ["LETTER_SIZE", "SLANT_ANGLE", "TOP_MARGIN"],
#            "Introversion": ["LETTER_SIZE", "SLANT_ANGLE", "TOP_MARGIN"],
#            "Emotional stability": ["BASE_LINE_ANGLE"],
#            "Neuroticism": ["BASE_LINE_ANGLE", "SLANT_ANGLE"],
#            "Openness to experience": ["LETTER_SIZE", "SLANT_ANGLE"],
#            "Conscientiousness": ["LETTER_SIZE", "TOP_MARGIN"],
#            "Agreeableness": ["LETTER_SIZE", "SLANT_ANGLE"]}

# Train and save a separate model for each target variable
for target, features in targets.items():
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

    # Train the model
    clf = SVC(kernel='linear', C=1.0)
    clf.fit(X_train, y_train)

    # Test the model
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of {target}: {accuracy}")

    # Save the model using pickle
    with open(f"models/{target}_model.pickle", "wb") as f:
        pickle.dump(clf, f)
