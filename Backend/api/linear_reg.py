import pandas as pd
import csv
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics



def process_file(features, label, file):

    # convert comma seperated list of features to list
    feature_list = features.split(',')

    # read training csv into pandas
    training_data = pd.read_csv(file)

    # data frame containing features
    features_df = training_data[feature_list]

    # label name of what we are trying to predicts
    label_name = label

    y = training_data[label_name]

    # split the data the user gave us into 70, 30 sets so that we can give them an indication of how accurate
    # the model is
    # x_train is 70% of our feature rows
    # x_test is 30% of our feature rows
    # y_train is 70% of our label rows
    # y_test is 30% of our label rows
    x_train, x_test, y_train, y_test = train_test_split(features_df, y, test_size=.3)

    lm = linear_model.LinearRegression()

    model = lm.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    print("Accuracy of model: ", accuracy)
    print(type(model))
    return accuracy, model
