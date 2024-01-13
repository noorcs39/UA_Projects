import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df =pd.read_csv("/home/noor/UA_Local_Proejcts/UA_Projects/Fault Detection/Dataset/Cleaned_data_after_processing.csv")


#Data_Preprocessing
#print(df.head())
print(df.columns)
#print(df['event type'])


#Data counting 
# Count total number of non-null values for each column
# column_counts = df.count()
# print(column_counts)

# Sum the counts across all columns
total_counts = df.apply(lambda x: x.value_counts().sum())

# Create a bar graph
# plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
# total_counts.sort_index().plot(kind='bar', color='skyblue')
# plt.title('Total count for each column')
# plt.xlabel('Column')
# plt.ylabel('Total Count')
# plt.show()


# Create a bar graph for 'event type'
# plt.figure(figsize=(8, 5))  # Adjust the figure size as needed
# df['event type'].value_counts().sort_index().plot(kind='bar', color=['green', 'red'])
# plt.title('Normal Event vs Faluty')
# plt.xlabel('Event Type')
# plt.ylabel('Total Events')
# plt.xticks([0, 1], ['Normal (0)', 'Fault (1)'], rotation=0)
# plt.savefig('bar.jpg')
# plt.show()

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=0)

print(y_test)

