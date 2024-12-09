import pandas as pd
import matplotlib.pyplot as plt

#Script to generate some double bar charts to view the distribution of the data between train/test when looking at manufacturers, countries, and regions


df_train = pd.read_csv("Data/annotations_train_grouped.csv")
df_test = pd.read_csv("Data/annotations_test_grouped.csv")
df_classes = pd.read_csv("Data/class_names_manufacturer_country_region_grouped.csv")
df_train = df_train.merge(df_classes, left_on='class', right_index=True)
df_test = df_test.merge(df_classes, left_on='class', right_index=True)

# Function to create double bar charts
def plot_double_bar(df_train, df_test, column, title):
    train_counts = df_train[column].value_counts().sort_index()
    test_counts = df_test[column].value_counts().sort_index()

    plot_data = pd.DataFrame({'Train': train_counts, 'Test': test_counts}).fillna(0)

    plot_data.plot(kind='bar', figsize=(14, 7), color=['skyblue', 'lightcoral'])
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Plot distribution of manufacturers
plot_double_bar(df_train, df_test, 'manufacturer', 'Distribution of Manufacturers')

# Plot distribution of countries
plot_double_bar(df_train, df_test, 'country', 'Distribution of Countries')

# Plot distribution of regions
plot_double_bar(df_train, df_test, 'region', 'Distribution of Regions')

