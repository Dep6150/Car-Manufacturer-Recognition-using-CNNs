import pandas as pd

# Load the class names
class_names = pd.read_csv("class_names.csv")

# Load the grouped class names
df_grouped = pd.read_csv("class_names_manufacturer_country_region_grouped.csv")

# Create a dictionary mapping car models to manufacturer indices
class_map = {}
for i, row in class_names.iterrows():
    car_model = row['class_names']
    for j, man in df_grouped.iterrows():
        if man['manufacturer'] in car_model:
            class_map[i + 1] = j  # Add 1 to i to match MATLAB's 1-based indexing
            break

# Load the test and train annotations
df_test = pd.read_csv("annotations_test.csv")
df_train = pd.read_csv("annotations_train.csv")

# Map the classes
df_test["class"] = df_test["class"].map(class_map)
df_train["class"] = df_train["class"].map(class_map)

# Save the updated annotations
df_test.to_csv("annotations_test_grouped.csv", index=False)
df_train.to_csv("annotations_train_grouped.csv", index=False)