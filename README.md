# Deep Structured Active Contours (DSAC)

This code allows to train a CNN model to predict a good map of penalizations for the different term of an Active Contour Model (ACM) such that the result gets close to a set of ground truth contours, as presented in [[1]](#marcos2018) (to appear in CVPR 2018). 

In this code, we combine the expressiveness of deep CNNs with the versatility of ACMs in a unified framework, which we call Deep Structured Active Contours (DSAC). In essence, we employ a CNN to learn the energy function that would allow an ACM to generate polygons close to a set of ground truth instances.


## Datasets

[Vaihingen buildings](https://drive.google.com/open?

## Usage

Download and unzip the datasets. Modify the dataset paths in the main file and run them with Python 3. Requires Tensorflow 1.4.
