import scipy.io as sio
import pandas as pd
import os
from scipy.io.matlab import mat_struct

#originally the downloaded .mat file from kaggle had both annotations and class names within it. Function was made then, but the .mat file from kaggle had some issues with classes they were incorrectly labeled
#still works with the updated .mat files from the cited github repo, just run this script 3 times updating the mat_file, annotations_csv, and class_names_csv paths as needed.
def mat_to_csvs(mat_filepath, annotations_csv_filepath, class_names_csv_filepath):
    """Converts a .mat file with 'annotations' and 'class_names' to two .csv files.

    Args:
        mat_filepath: Path to the .mat file.
        annotations_csv_filepath: Path to save the annotations .csv file.
        class_names_csv_filepath: Path to save the class_names .csv file.
    """
    try:
        mat_data = sio.loadmat(mat_filepath, struct_as_record=False, squeeze_me=True)

        for key in list(mat_data.keys()):
            if key.startswith('__'):
                del mat_data[key]

        annotations_data = mat_data.get('annotations', None)
        class_names_data = mat_data.get('class_names', None)

        if annotations_data is not None:

            if isinstance(annotations_data, mat_struct):
                df_annotations = pd.DataFrame.from_records([annotations_data.__dict__])
            elif all(isinstance(item, mat_struct) for item in annotations_data):
                df_annotations = pd.DataFrame.from_records([item.__dict__ for item in annotations_data])
            else:
                print("Annotations data was not in expected format (an array of structs or a single struct)")
                return

            df_annotations.to_csv(annotations_csv_filepath, index=False)
            print(f"Annotations saved to: {annotations_csv_filepath}")

        else:
            print("Warning: 'annotations' not found in the .mat file.")


        if class_names_data is not None:
            if isinstance(class_names_data, (list,)):
                df_class_names = pd.DataFrame(class_names_data, columns=['class_names'])
            else:
                df_class_names = pd.DataFrame({'class_names': class_names_data})

            df_class_names.to_csv(class_names_csv_filepath, index=False)
            print(f"Class names saved to: {class_names_csv_filepath}")
        else:
            print("Warning: 'class_names' not found in the .mat file.")


    except FileNotFoundError:
        print(f"Error: .mat file not found at {mat_filepath}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

#cars_train_annos.mat has annotations for training data set
mat_file = r"cars_train_annos.mat"
annotations_csv = r"annotations_train.csv"
class_names_csv = r"class_names.csv"

#cars_test_annos_withlabels.mat has annotations for test data set
#mat_file = r"cars_test_annos_withlabels.mat"
#annotations_csv = r"annotations_test.csv"
#class_names_csv = r"class_names.csv"

#cars_meta.mat has the class names
#mat_file = r"cars_meta.mat"
#annotations_csv = r"annotations_test.csv"
#class_names_csv = r"class_names.csv"

mat_to_csvs(mat_file, annotations_csv, class_names_csv)

