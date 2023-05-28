import pandas as pd

# Read the CSV file
df = pd.read_csv('lists/final_data.csv', names=["BASE_LINE_ANGLE", "TOP_MARGIN", "LINE_SPACING", "SLANT_ANGLE", "WORD_SPACING", "LETTER_SIZE", "Extroversion","Introversion","Emotional_stability","Neuroticism", "Openness_to_experience","Conscientiousness","Agreeableness", "file_name"])

# Define the target variables
target_variables = ["Extroversion", "Introversion", "Emotional_stability", "Neuroticism", "Openness_to_experience", "Conscientiousness", "Agreeableness"]

# Get the ranges for WORD_SPACING and LINE_SPACING for each target variable
for target in target_variables:
    target_data = df[df[target] == 1]
    word_spacing_range = (target_data["WORD_SPACING"].min(), target_data["WORD_SPACING"].max())
    line_spacing_range = (target_data["LINE_SPACING"].min(), target_data["LINE_SPACING"].max())
    print(f"Range for {target}: WORD_SPACING {word_spacing_range}, LINE_SPACING {line_spacing_range}")
