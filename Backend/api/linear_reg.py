import pandas as pd
import csv
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
from .models import MLModel


def process_file(features, label, file):

    # convert comma separated list of features to list
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
    #save_linear_model(model, x_test, y_test)
    pickled_model = pickle.dumps(model)
    saved_model = MLModel.objects.create(ml_model=pickled_model)
    model_id = saved_model.id
    depickle(model_id, x_test, y_test)
    return accuracy, model_id

def depickle(id, x_test, y_test):
    pickled_model = MLModel.objects.get(pk=id).ml_model
    model = pickle.loads(pickled_model)
    return model

def save_linear_model(model, x_test, y_test):
    filename = "model1.pk1"
    with open(filename, "wb") as file:
        pickle.dump(model, file)

    with open(filename, "rb") as file:
        pickle_model = pickle.load(file)
        print(pickle_model.score(x_test, y_test))