import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Please provide the CSV filename as a command line argument")
    sys.exit(1)

filename = sys.argv[1]
if filename == "lists/final_data.csv":
    df = pd.read_csv(filename, header=None, names=["BASE_LINE_ANGLE", "TOP_MARGIN", "LINE_SPACING", "SLANT_ANGLE", "WORD_SPACING", "LETTER_SIZE", "Extroversion", "Introversion", "Emotional_stability", "Neuroticism", "Openness_to_experience", "Conscientiousness", "Agreeableness", "file_name"])
else:
    df = pd.read_csv(filename, header=None, names=["BASE_LINE_ANGLE", "TOP_MARGIN", "LINE_SPACING", "SLANT_ANGLE", "WORD_SPACING", "LETTER_SIZE", "file_name"])


print(df.head(20))
