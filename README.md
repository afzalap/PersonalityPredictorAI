# Personality Prediction System Based On Graphological Features

The project aims to develop a system for predicting human personality traits based on handwriting analysis. It leverages graphological analysis techniques and machine learning algorithms to extract meaningful features from handwriting samples and accurately predict personality traits.

The system incorporates image processing methods to analyze and extract relevant graphological features from the handwriting samples, enhancing efficiency and reducing errors in personality trait prediction.

A user-friendly web application has been developed to provide an intuitive interface for users to input their handwriting samples and receive personality trait predictions. The web application ensures easy accessibility and convenience, eliminating the need for specialized software or technical expertise.

The project's GitHub repository can be found at: [https://github.com/afzalap/PersonalityPredictorAI](https://github.com/afzalap/PersonalityPredictorAI)

## Table of Contents

- [Project Structure](project-structure)
- [Dataset Overview](#dataset-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preparation](#data-preparation)
- [License](#license)

## Project Structure

The project is organized into two main directories:

1. DjangoPredictor:
   - This directory contains the Django web application for personality prediction. It provides a user-friendly interface for users to input their handwriting samples and receive personality trait predictions. It handles the communication with the backend models and displays the results to the user.

2. personalityPrection:
   - This directory is dedicated to feature extraction and model building. It includes scripts and modules for extracting relevant graphological features from handwriting samples and training machine learning models for personality prediction. It performs the necessary data preprocessing, feature engineering, and model training steps.

The project structure is designed to separate the front-end web application (DjangoPredictor) from the back-end feature extraction and model building (personalityPrection). This modular organization allows for easier maintenance, scalability, and future improvements.

Feel free to explore the respective directories to understand the implementation details and make any necessary modifications based on your specific requirements.

## Dataset Overview

The dataset used for training and evaluation consists of a total of 1839 samples from 657 different writers. 

- 1539 samples of 657 were taken from the IAM Handwriting Dataset (http://www.fki.inf.unibe.ch/databases/iam-handwriting-database) which provides a diverse collection of handwritten documents.

- Additional 300 samples were collected from 100 writers who volunteered from friends and family.

## Installation

To install the necessary packages, run the following command:

 ```
  pip install -r requirements.txt
 ```
 
## Usage

- Run extract_raw_data.py to extract features from the images in the data folder. This will create the file lists/raw_features.csv       containing the raw features in pixels.

  ```
  cd personalityPrection
  python3 extract_raw_data.py
  ```
  
- Run gen_clean_data.py to clean the extracted features. It will convert pixel values to millimeters, round them to 2 decimal places, and handle missing values. This script uses the lists/raw_features.csv file as input and creates the file lists/clean_data.csv

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

The input to the web App and the samples in the personalityPrection/data should be in the following cropped form containing only the handwritten text


<img src="https://github.com/afzalap/PersonalityPredictorAI/assets/68552769/18cdabd7-1268-4794-8f13-09cebfa956c7" alt="Image" width="300" height="300"/>


## License

[MIT License](LICENSE)

