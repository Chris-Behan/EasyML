import pandas as pd
import csv
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
from .models import MLModel
from sklearn.metrics import mean_absolute_error, accuracy_score


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

    # make predictions on the test feature set
    predictions = model.predict(x_test)
    # Calculate absolute mean error between actual values of feature set and predicted values
    mean_error = mean_absolute_error(y_test, predictions)
    # Calculate mean price of actual test values
    mean_price = sum(y_test) / len(y_test)
    # Calculate "accuracy" of model on training set
    accuracy = (1 - (mean_error / mean_price)) * 100
    print('Mean price:$', mean_price)
    print("Mean error:$", mean_error)
    print('Based on this definition, the accuracy is: ', accuracy, '%')
    #save_linear_model(model, x_test, y_test)
    # Pickle model so that it can be stored in DB
    pickled_model = pickle.dumps(model)
    # Create and save pickled ml model and store in DB
    saved_model = MLModel.objects.create(ml_model=pickled_model)
    model_id = saved_model.id
    return accuracy, mean_error, model_id


def depickle(id):
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


def make_prediction(model_id, feature_list):
    model = depickle(model_id)
    return model.predict([feature_list])