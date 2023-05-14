import pandas as pd
# Read the features from the file
with open("lists/raw_features", "r") as f:
    lines = f.readlines()

features = []
for line in lines:
    features.append(line.strip().split("\t"))

# Create a pandas dataframe from the features list
df = pd.DataFrame(features, columns=["BASE_LINE_ANGLE", "TOP_MARGIN", "LINE_SPACING", "SLANT_ANGLE", "WORD_SPACING", "LETTER_SIZE", "file_name"])



def to_pixel(x):
    return 0.086 * float(x)


df['LINE_SPACING'] = df['LINE_SPACING'].apply(to_pixel)
df['WORD_SPACING'] = df['WORD_SPACING'].apply(to_pixel)
df['LETTER_SIZE'] = df['LETTER_SIZE'].apply(to_pixel)

# df.fillna(df.mean(), inplace=True)



df['BASE_LINE_ANGLE'] = pd.to_numeric(df['BASE_LINE_ANGLE'], errors='coerce').round(2)
df['TOP_MARGIN'] = pd.to_numeric(df['TOP_MARGIN'], errors='coerce').round(2)
df['LINE_SPACING'] = pd.to_numeric(df['LINE_SPACING'], errors='coerce').round(2)
df['SLANT_ANGLE'] = pd.to_numeric(df['SLANT_ANGLE'], errors='coerce').round(2)
df['WORD_SPACING'] = pd.to_numeric(df['WORD_SPACING'], errors='coerce').round(2)
df['LETTER_SIZE'] = pd.to_numeric(df['LETTER_SIZE'], errors='coerce').round(2)

# Fill missing values in specific columns with their respective mean values
cols_to_fill = ["BASE_LINE_ANGLE", "TOP_MARGIN", "LINE_SPACING", "SLANT_ANGLE", "WORD_SPACING", "LETTER_SIZE"]
mean_values = {col: df[col].mean() for col in cols_to_fill}
df[cols_to_fill] = df[cols_to_fill].fillna(value=mean_values)



df.to_csv('lists/clean_raw_list', sep='\t', index=False, header=False)


print(df.head(10).to_string(index=False))