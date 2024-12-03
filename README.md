# Sentiment analysis for movie review

## Overview
This project demonstrates a sentiment analysis pipeline for classifying movie reviews as either positive or negative using Logistic Regression. The dataset used is the IMDB Dataset of 50K Movie Reviews, which contains 25,000 positive and 25,000 negative labeled reviews.

## Features of the Project

Data Cleaning:
Removal of HTML tags and special characters.
Stemming using the Porter Stemmer.
Elimination of stopwords from reviews.

Feature Engineering:
Text vectorization using TF-IDF Vectorizer for extracting meaningful features from the text.

Model Training:
Logistic Regression is used as the classifier.
Model trained using an 80-20 train-test split.

Evaluation:
Accuracy score reported for both train and test datasets.

Pickle Support:
The trained model and TF-IDF vectorizer are saved using pickle for future use.
Prerequisites

To run the project, ensure you need the following libraries:

Python 3.7+
NumPy
Pandas
NLTK
Scikit-learn

## Project Pipeline

Load the Dataset:
Load the IMDB dataset using pandas.

Data Preprocessing:
Remove HTML tags using regex.
Remove special characters and convert text to lowercase.
Apply stemming and remove stopwords using NLTK.

Feature Engineering:
Convert the processed reviews into numerical vectors using TF-IDF Vectorizer.

Model Training:
Train a Logistic Regression model on the training data.

Evaluation:
Measure accuracy on the test and training datasets.

Serialization:
Save the trained model and vectorizer as .sav and .pkl files for future use.


## Dataset
The dataset used is the IMDB Dataset of 50K Movie Reviews. It can be downloaded from here.


## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/sentiment-analysis-logistic-regression.git

cd sentiment-analysis-logistic-regression
```

2. Run the following command for installing required libraries:

```bash
pip install requirements.txt
```

3. For the project code run this command:

```bash
jupyter notebook imdb_reviews_sentiment_analysis.ipynb
```

4. To use the model open code with this command:

```bash
jupyter notebook use_model.ipynb
```


