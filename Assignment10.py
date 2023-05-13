# core
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly as px

# ml
from sklearn import datasets as ds
from sklearn import linear_model as lm
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score


#iris
iris = ds.load_iris()
#boston
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
boston = raw_df.values[1::2, 2]

# Q1 - Create the dataframe a DataFrame with feature names as column headings
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print(iris_df.head(5))
print(iris.target_names.tolist())

# Q2 - Fit the Iris dataset into a kNN model with neighbors=5 and predict the category of observations passed
# in argument new_observations. Return back the target names of each prediction (and not their encoded values,
# i.e. return setosa instead of 0).

#knn classifier with n=5, and fit data into knn
knn = KNN(n_neighbors=5)
knn.fit(iris.data, iris.target)

# New observations and predictions, I'm proceeding as though I'm responsible for inputting some new predictions.
new_observations = [[6.7, 3.1, 4.4, 1.5], [5.9, 3.0, 5.1, 1.9], [4.8, 2.8, 5.5, 1.4]]

predictions = knn.predict(new_observations)

# Convert the encoded predictions to target names
target_names = iris.target_names[predictions]

print(target_names)

# Q3 - train-test, k-nearest, accuracy score

def tt_knn(split, neighbors):
    iris = ds.load_iris()
    X_train, X_test, y_train, y_test = tts(iris.data, iris.target, test_size=.2, random_state=42)

    # create knn, set neighbors, and fit with training data
    knn = KNN(n_neighbors=neighbors)
    knn.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = knn.predict(X_test)

    # Calculate the accuracy score
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

split_ratio = .2
neighbors = 5

accuracy = tt_knn(split_ratio, neighbors)

print(accuracy)

# Q4 - overfitting / underfitting
# train test splits and defining neighbors
iris = ds.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=42)
neighbors_range = range(1, 31)

# Instantiate lists
train_accuracy = []
test_accuracy = []

# loop over neighbors and fit model
for k in neighbors_range:
    knn = KNN(n_neighbors=k)
    knn.fit(X_train, y_train)
    # make predictions and calculate accuracy
    y_train_pred = knn.predict(X_train)
    y_test_pred = knn.predict(X_test)
    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)
    train_accuracy.append(train_acc)
    test_accuracy.append(test_acc)

# Plot for overfitting/underfitting
plt.figure(figsize=(8, 4))
plt.plot(neighbors_range, train_accuracy, label='train Accuracy')
plt.plot(neighbors_range, test_accuracy, label='test Accuracy')
plt.title('Overfitting/Underfitting Curve')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('accuracy')
plt.xticks(np.arange(1, 31, step=2))
plt.legend()
plt.grid(True)
plt.show()

# Q5 - pupil-teacher ratio and home values, you said on Slack to ignore the Boston dataset, but I wanted to try this one
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
boston = raw_df.values[1::2, 2]

# isolate ptratio and get MEDV targets
PTRATIO = boston['PTRATIO'].astype(int).to_numpy()

MEDV = boston['MEDV'].astype(int).to_numpy()


# plot
plt.figure(figsize=(7, 5))
plt.scatter(PTRATIO, MEDV, c='red', alpha=0.6)
plt.title('Pupil / Teacher Ratio and Median Home Value')
plt.xlabel('PTRATIO')
plt.ylabel('MEDV')
plt.grid(True)
plt.show()

# ptratio as a numpy array
PTRATIO_array = np.array(PTRATIO)
PTRATIO_array


