import pandas as pd
import matplotlib.pyplot as plt


# Preliminary EDA
df = pd.read_csv(r'C:\Users\Evan\Desktop\CUNY\602\Assignments\final project\creditcard.csv')
print("Dataset shape:", df.shape)
print(df.head())
print(df.describe())
print(df["Class"].value_counts())
#plot
plt.hist(df["Class"])
plt.title("Distribution of Target Variable")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()
# correlation
correlations = df.corr()
print(correlations)
plt.figure(figsize=(10,10))
plt.title("Correlation Matrix")
plt.imshow(correlations, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(df.columns)), df.columns, rotation=90)
plt.yticks(range(len(df.columns)), df.columns)
plt.show()
