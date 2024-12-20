# Car-Manufacturer-Recognition-using-CNNs

## Project Type

Image Classification and Analysis

## Team Members

*   Daniel Puig - Dep6150

## Project Description

This project develops a Convolutional Neural Network (CNN) model to identify the manufacturer of a car from an image. It uses the Stanford Cars Dataset, containing images of 196 different car models. The project explores various CNN architectures and hyperparameters to achieve optimal accuracy in car manufacturer recognition.

Beyond just recognizing the manufacturer, this project delves into the research question: **Do distinct design languages exist across different manufacturers, and do these design languages cluster based on regional or national origins?**

The project analyzes the learned features of the CNN model to determine whether it can effectively cluster car manufacturers based on their design features. Further analysis investigates if these clusters align with regional or national origins, providing insights into the potential influence of geographic location on car design aesthetics.

## Notebooks

*   **`guided_notebook.ipynb`**: This notebook provides a guided presentation of the project, including data overview, preprocessing steps, model training, evaluation, and visualization of results. It's recommended for users who want to understand the project's workflow and findings.
*   **`exploration_notebook.ipynb`**: This notebook contains the initial code and explorations of different models and approaches considered during the project's development. It might be helpful for users interested in the experimental process and alternative approaches.

## Dependencies

*   Python
*   TensorFlow
*   Keras
*   OpenCV
*   Pandas
*   Scikit-learn
*   Matplotlib

## Results


The project achieved 93.9% accuracy on a representative sample of the test set using a fine-tuned VGG16 model. This model was trained for 50 epochs with data augmentation and early stopping.

The analysis of the model's learned features, visualized through t-SNE and PCA dimensionality reduction techniques, revealed the following insights:

*   There is evidence to suggest that distinct design languages exist across different car manufacturers, as indicated by some degree of clustering based on countries.
*   However, the clustering is not perfect, and there is overlap between clusters, suggesting that global design trends also play a significant role.
*   Quantitative analysis using Silhouette Score and Davies-Bouldin Index confirmed that the clustering is not very distinct, especially with PCA. t-SNE provided slightly better-defined clusters.

These results suggest that both regional and global factors contribute to the design languages of different car manufacturers.

## Acknowledgments

*   The Stanford Cars Dataset creators for providing the data.
*   The Keras and TensorFlow teams for developing the deep learning libraries.

## Dataset

The dataset used for this project is the Stanford Cars Dataset, sourced from:

*   [https://github.com/jhpohovey/StanfordCars-Dataset](https://github.com/jhpohovey/StanfordCars-Dataset)