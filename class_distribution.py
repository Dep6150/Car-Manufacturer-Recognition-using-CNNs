import pandas as pd
import matplotlib.pyplot as plt

# Load the training data
df_train = pd.read_csv("Data/annotations_test_grouped.csv")

# Count the occurrences of each class
class_counts = df_train["class"].value_counts()

# Calculate the percentage of each class
class_percentages = class_counts / len(df_train) * 100

# Print the class distribution
print("Class Distribution:")
print(class_percentages)

# Plot the class distribution
plt.figure(figsize=(10, 5))
plt.bar(class_percentages.index, class_percentages.values)
plt.xlabel("Class")
plt.ylabel("Percentage of Samples")
plt.title("Class Distribution in Training Data")
plt.show()