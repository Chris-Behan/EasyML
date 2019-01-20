import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
"""
Please ensure that the features are either one-hot encoded OR ensure users are able to only select numeric columns

"""
def process_logistic_file(features, label, file):
    # convert comma seperated list of features to list
    feature_list = features.split(',')

    # read training csv into pandas
    training_data = pd.read_csv(file)

    feature_data = training_data[feature_list]

    label_df = training_data[[label]]

    # we need to encode the labels so that
    encode = LabelEncoder()

    # Here we are encoding the labels. This is to make the categorical labels numeric so that sklearn can handle them
    label_df[label] = encode.fit_transform(label_df[label])

    # print("unique labels:", label_df.PavedDrive.unique())

    # split the data the user gave us into 70, 30 sets so that we can give them an indication of how accurate

    x_train, x_test, y_train, y_test = train_test_split(feature_data, label_df, test_size=.3)

    logreg = LogisticRegression(solver='lbfgs', multi_class='multinomial')

    # Create an instance of Logistic Regression Classifier and fit the data.
    logreg.fit(x_train, y_train)

    accuracy = logreg.score(x_test, y_test)
    print("accuracy:", logreg.score(x_test, y_test))

    print(x_train.head())

    # now make a prediction

    predictions = logreg.predict(x_test)
    print(predictions[0])
    print("test.head", x_test.head())
    return (accuracy, logreg)


def make_LR_prediction(model, data):
    return model.predict([data])