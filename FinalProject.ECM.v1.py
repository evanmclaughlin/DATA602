import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import plotly.graph_objects as go
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# data loading
file_path = r"C:\Users\Evan\Desktop\CUNY\602\Assignments\final project\creditcard.csv"
data = pd.read_csv(file_path)

# explore the data, its dimensions, and summary statistics, checking data types and missing values
print(data.head())
print(data.shape)
print(data.describe())
print(data.dtypes)
print(data.isnull().sum())

# Count the number of different "Classes" - fraud vs. non-fraud
class_counts = data["Class"].value_counts()
print(class_counts)

# now let's conduct our EDA, including the visualizations.
# Visualize the distribution of target variable (fraudulent vs. non-fraudulent transactions)
transaction_counts = data['Class'].value_counts()
fig = px.bar(transaction_counts, x=transaction_counts.index, y=transaction_counts.values)
fig.update_layout(title='Distribution of Transactions', xaxis_title='Class', yaxis_title='Count')
fig.show()

# Percentage of fraudulent transactions
fraud_percentage = class_counts[1] / len(data) * 100
print("\nPercentage of Fraudulent Transactions: {:.2f}%".format(fraud_percentage))


# We can see above that the overwhelming number of transactions are not fraudulent (Class=0), so much so that the
# distribution graphic barely registers the fraudulent (Class=1) transactions. Fraudulent transactions = .17% of
# transactions

# Distribution of Transaction Amounts (Histogram)
fig = px.histogram(data, x='Amount', nbins=30)
fig.update_layout(title='Distribution of Transaction Amounts', xaxis_title='Amount', yaxis_title='Count')
fig.show()

# The above figure shows the distribution of transaction amounts it would ideally be used to help us
# identify outlier transaction amounts by generating baseline expectations for the "typical" transaction.

# Distribution of Transaction Amounts by Class (Boxplot)
fig = px.box(data, x='Class', y='Amount')
fig.update_layout(title='Distribution of Transaction Amounts by Class', xaxis_title='Class', yaxis_title='Amount')
fig.show()

# This boxplot provides a superior alternative to the bar chart above, as it enables the viewer to assess differences
# in transaction amounts between the two classes and determine if there are any outliers or extreme values. In this case
# we are left with more questions than answers, as there is no outwardly evident relationship between transaction size
# and likelihood of fraud. However, it should be useful to graphically display this information again at a slightly more
# granular level.

# Remove outliers from the Transaction Amount column using IQR method
Q1 = data['Amount'].quantile(0.25)
Q3 = data['Amount'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR
filtered_data = data[data['Amount'] <= upper_bound]


# Re-run the boxplot after removing outliers
fig = px.box(filtered_data, x='Class', y='Amount')
fig.update_layout(title='Distribution of Transaction Amounts by Class (Outliers Removed)', xaxis_title='Class', yaxis_title='Amount')
fig.show()

# Calculate mean transaction amount for each class
mean_amounts = filtered_data.groupby('Class')['Amount'].mean().reset_index()
print(mean_amounts)

# This provides a more sophisticated look at the transaction distribution across classes and further reinforces how
# unlikely it will be that transaction amount provides much insight into. This itself is reinforced by the relative
# proximity of the mean transaction amount across the classes.

# Correlation Heatmap
corr = data.corr()
fig = px.imshow(corr, color_continuous_scale='rainbow')
fig.update_layout(title='Correlation Heatmap')
fig.show()

# Correlation Heatmap with outliers removed
corr = filtered_data.corr()
fig = px.imshow(corr, color_continuous_scale='rainbow')
fig.update_layout(title='Correlation Heatmap')
fig.show()

# We don't gain much in the way of insight from this heatmap, other than the fact that the V2 feature has a strong
# negative correlation with the amount. We could guess as to what this feature might be, but it wouldn't be a great
# use of time. There are a couple other features that seem to correlate with the amount, also, but our interest lies
# in those that correlate with "class," which does not appear to correlate strongly, negatively or positively, with
# any of the features in the dataset, at least upon cursory glance. The same is true even after we remove the outliers
# from the non-fraud dataset that were skewing results and hindering our analysis. However, it should be noted that
# the heatmap generated using filtered data produces a graphic that demonstrates more negative correlation across
# almost all features.

# Since there are no missing values in the dataset, we don't have to worry about imputing that data. We can proceed to
# running our train-test split and seeing how our model performs. However, with so many anonymized features, we would
# do well to employ feature selection to better zero in on the most impactful features, even though we still don't
# have descriptions of them.

# Separate the features and the target variable and create the tt-split
X = filtered_data.drop("Class", axis=1)
y = filtered_data["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Next generate the logistic regression and train the model
log_model = LogisticRegression(solver='lbfgs', max_iter=1000)
log_model.fit(X_train, y_train)

# Produce predictions and measure model
y_pred = log_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy*100)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

    # What we see here is a very accurate model, 99.89% accuracy, that we have a very difficult time explaining, since 1. we
# don't have descriptions of the features that are driving the model, since the data is confidential, and 2. no
# single variable has an obvious impact on the Class.

# What we're left with is perhaps more questions than we started
# with, since feature descriptions would be enormously helpful is helping us intuit what we might be looking at.
# Nevertheless, we still have a remarkably accurate model that can be used, at the very least, to answer our research
# question,

# Looking at the calculations above, the accuracy is very high at 99.90%. This indicates that the model is correctly
# classifying the majority of the instances in the dataset.
# The precision measures the proportion of correctly predicted positive instances out of all instances predicted
# as positive. Out of all the instances the model predicted as positive, approximately 79.17% of them are actually
# positive. When the model predicts a transaction as fraudulent, it is correct about 79.17% of the time.
# Looking at the Recall, the proportion of correctly predicted positive instances out of all actual positive instances,
# the value of 0.63 means that the model is able to correctly identify approximately 62.64% of the actual fraudulent
# transactions in the dataset. In other words, the model has a moderate ability to capture fraudulent transactions.
# Lastly, F1-score, a combination of mean of precision and recall provides a balanced measure of the model's
# performance, taking into account both precision and recall. The F1-score value of 0.70 indicates that the model
# has a reasonably balanced performance between correctly identifying fraud and minimizing false positives.

