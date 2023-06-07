# Personality Prediction System Based On Graphological Features

## Overview

The project aims to develop a system for predicting human personality traits based on handwriting analysis. It leverages graphological analysis techniques and machine learning algorithms to extract meaningful features from handwriting samples and accurately predict personality traits.

The system incorporates image processing methods to analyze and extract relevant graphological features from the handwriting samples, enhancing efficiency and reducing errors in personality trait prediction.

A user-friendly web application has been developed to provide an intuitive interface for users to input their handwriting samples and receive personality trait predictions. The web application ensures easy accessibility and convenience, eliminating the need for specialized software or technical expertise.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Preparation](#data-preparation)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the necessary packages, run the following command:

 ```
  pip install -r requirements.txt
 ```
 
## Usage

- Run extract_raw_data.py to extract features from the images in the data folder. This will create the file lists/raw_features.csv containing the raw features in pixels.
  ```
  cd personalityPrection
  python3 extract_raw_data.py
  ```
- Run gen_clean_data.py to clean the extracted features. It will convert pixel values to millimeters, round them to 2 decimal places, and handle missing values. This script uses the lists/raw_features.csv file as input and creates the file lists/clean_data.csv.
  ```
  python3 gen_clean_data.py
  ```
- Run gen_final_data.py to label the data based on graphological rules. It uses the lists/clean_data.csv file as input and generates the final labeled dataset.
  ```
  python3 gen_final_data.py
  ```
- Run train_models.py to train the models using the labeled dataset. The trained models can be used in the DjangoPredictor or you can change the path for saving the models to the DjangoPredictor/models directory.
  ```
  python3 train_models.py
  ```
- Start the Django server in the DjangoPredictor directory to use the system.
  ```
  cd ../DjangoPredictor
  python manage.py runserver
  ```

## Data Preparation

The input to the web App should be in the following cropped form


## License

[MIT License](LICENSE)

