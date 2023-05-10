import matplotlib.pyplot as plt
import pandas as pd

url = "https://data.cityofnewyork.us/resource/h9gi-nx95.csv"
df = pd.read_csv(url)

# Part 1
# Summary statistics, including median and missing values information
summary_stats = df.describe()
median = df['number_of_persons_injured'].median()
missing_values = df.isnull().sum()
num_rows = df.shape[0]
num_columns = df.shape[1]
print(summary_stats)
print(missing_values)
print(num_rows)
print(num_columns)
print(median)


df = df.drop(columns=['collision_id', 'vehicle_type_code1', 'vehicle_type_code2'])
df['crash_date'] = pd.to_datetime(df['crash_date'])
df['crash_time'] = pd.to_datetime(df['crash_time'], format='%H:%M')
df['day'] = df['crash_date'].dt.day
df['month'] = df['crash_date'].dt.month
df['year'] = df['crash_date'].dt.year

# Grouping and Summarizing
summary_by_borough = df.groupby('borough').agg({'number_of_persons_injured': 'sum', 'number_of_persons_killed': 'sum'})
print("\nSummary by Borough:")
print(summary_by_borough)

# Filter accidents that occurred in the morning, afternoon, evening, and at night

# Convert crash_time to datetime format
df['crash_time'] = pd.to_datetime(df['crash_time'])

# Define time ranges for the buckets and Convert crash_time column to datetime format
df['crash_time'] = pd.to_datetime(df['crash_time'])

# New column for time buckets
df['time_bucket'] = pd.cut(df['crash_time'].dt.hour,
                             bins=[0, 6, 12, 18, 24],
                             labels=['late night', 'morning', 'afternoon', 'evening'],
                             right=False)

# Calculate the number of persons injured for each bucket of time
injured_counts = df.groupby('time_bucket')['number_of_persons_injured'].sum()
print(injured_counts)

plt.bar(injured_counts.index, injured_counts.values)
plt.xlabel('Time Bucket')
plt.ylabel('Number of Persons Injured')
plt.title('Number of Persons Injured by Time Bucket')
plt.show()

# Now let's alter the boxplot per some of the specifications included in the assignment
# Annotations
fig, ax = plt.subplots()

ax.bar(injured_counts.index, injured_counts.values, color='orange', linewidth=2)

for i, v in enumerate(injured_counts.values):
    ax.text(i, v, str(v), ha='center', va='center')

# Title and labels
ax.set_title('Number of Persons Injured by Time of Day')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Number of Persons Injured')

# Now let's change the legend characteristics and margins
legend = ax.legend(['Injured'], fontsize='medium')
legend.set_title('Legend', prop={'size': 'medium'})
ax.add_artist(legend)
plt.margins(y=0.1)
plt.show()

# The bar chart shows us that afternoon represents the time when most people are getting injured in automobile accidents.
# This is somewhat intuitive, given that people are often commuting home and might be distracted or speeding.

# Part 2 - Now let's look at how Seaborn handles the same dataset and the relevant tasks

import seaborn as sns
df2 = pd.read_csv('https://data.cityofnewyork.us/resource/h9gi-nx95.csv')
df2['crash_time'] = pd.to_datetime(df2['crash_time'])

# Create a new column for time buckets
df2['time_bucket'] = pd.cut(df2['crash_time'].dt.hour,
                             bins=[0, 6, 12, 18, 24],
                             labels=['night', 'morning', 'afternoon', 'evening'],
                             right=False)
injured_counts = df2.groupby('time_bucket')['number_of_persons_injured'].sum().reset_index()
sns.set(style='dark')
ax = sns.barplot(x='time_bucket', y='number_of_persons_injured', data=injured_counts, color='skyblue')
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'bottom', xytext = (0, 5), textcoords = 'offset points')
ax.set_title('Number of Persons Injured by Time Bucket')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Number of Persons Injured')
plt.margins(y=0.1)
plt.show()

# Part 3 - The overall product looks roughly the same. Predefined color / style palettes help cut down the amount of code needed
# produce the plot. The sns.barplot() groups and presents the data automatically. Aesthetically,
# # they look similar, but matplotlib is a bit more manual.

# Conclusions - the graphics present an adequate picture automobile accidents and the resulting injuries. I might have
# expected more injuries in the evening than the afternoons, due to less visibility. My question might be if the
# relatively lower number of injuries in the morning might be due to fewer accident or less severity of those accidents.
