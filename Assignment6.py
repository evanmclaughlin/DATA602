import pandas as pd

# Through the city data portal, I eventually came upon data on misconduct complaints registered against the NYPD.

#Unfortunately, there's a lot of data!

#Loading the dataframe and looking at the first few and last few lines
df1 = pd.read_csv('https://raw.githubusercontent.com/new-york-civil-liberties-union/NYPD-Misconduct-Complaint-Database-Updated/main/CCRB%20Complaint%20Database%20Raw%2004.20.2021.csv')
df1.head()
df1.tail()
# Looking at the shape next
print(df1.shape)
#Looking at the columns
print(df1.dtypes)
# Statistical summary
print(df1.describe())


# Next, I'll do the same thing for the Kobe dataset

import pandas as pd

df2 = pd.read_csv('https://raw.githubusercontent.com/data602sps/datasetspractice/main/kobe.csv')
df2.head()
df2.tail()
print(df2.shape)
print(df2.dtypes)
print(df2.describe())

# Next, I'll do the salary data

import pandas as pd
df3 = pd.read_csv('https://raw.githubusercontent.com/data602sps/datasetspractice/main/salarydata.csv')
df3.head()
df3.tail()
print(df3.shape)
print(df3.dtypes)
print(df3.describe())

# Lastly, I found another dataset from NYC that contains the department of education's disciplinary numbers
import pandas as pd

df4 = pd.read_csv('https://raw.githubusercontent.com/evanmclaughlin/DATA602/Assignment6/2020-2021_Student_Discipline_Annual_Report_-_All.csv')
df4.head()
df4.tail()
print(df4.shape)
print(df4.dtypes)
print(df4.describe())
