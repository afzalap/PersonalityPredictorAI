import pandas as pd

# Read the features from the CSV file
df = pd.read_csv('lists/raw_data.csv', header=None, names=["BASE_LINE_ANGLE", "TOP_MARGIN", "LINE_SPACING", "SLANT_ANGLE", "WORD_SPACING", "LETTER_SIZE", "file_name", "height", "width", "dpi" ])

# Convert line spacing, word spacing, and letter size to pixel values

def to_mm(dpi, x):
    return (25.4 / dpi) * float(x)

df['LINE_SPACING'] = df.apply(lambda row: to_mm(row['dpi'], row['LINE_SPACING']), axis=1)
df['WORD_SPACING'] = df.apply(lambda row: to_mm(row['dpi'], row['WORD_SPACING']), axis=1)
df['LETTER_SIZE'] = df.apply(lambda row: to_mm(row['dpi'], row['LETTER_SIZE']), axis=1)


# Convert columns to numeric and round to 2 decimal places
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

# Convert columns to numeric and round to 2 decimal places
df['BASE_LINE_ANGLE'] = pd.to_numeric(df['BASE_LINE_ANGLE'], errors='coerce').round(2)
df['TOP_MARGIN'] = pd.to_numeric(df['TOP_MARGIN'], errors='coerce').round(2)
df['LINE_SPACING'] = pd.to_numeric(df['LINE_SPACING'], errors='coerce').round(2)
df['SLANT_ANGLE'] = pd.to_numeric(df['SLANT_ANGLE'], errors='coerce').round(2)
df['WORD_SPACING'] = pd.to_numeric(df['WORD_SPACING'], errors='coerce').round(2)
df['LETTER_SIZE'] = pd.to_numeric(df['LETTER_SIZE'], errors='coerce').round(2)

# Write the cleaned data to a new CSV file
df.to_csv('lists/clean_data.csv', sep=',', index=False, header=False)

print(df.head(10).to_string(index=False))
