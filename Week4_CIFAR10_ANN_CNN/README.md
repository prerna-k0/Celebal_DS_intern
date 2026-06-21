# CIFAR-10 Image Classification Learning Project

## Objective
Build and compare ANN and CNN models on the CIFAR-10 dataset and analyze their performance.

## Dataset
CIFAR-10 contains 60,000 color images of size 32×32 across 10 classes.

## Models Implemented
- Artificial Neural Network (ANN)
- Convolutional Neural Network (CNN)

## Results

| Model | Test Accuracy |
|---------|---------|
| ANN | 41.57% |
| CNN | 70.68% |

## Key Findings
- ANN achieved moderate performance but lost spatial information after flattening images.
- CNN significantly outperformed ANN by learning spatial and hierarchical image features.
- Batch Normalization and Dropout improved training stability and generalization.
- EarlyStopping prevented unnecessary training and reduced overfitting.

## Conclusion
CNN proved to be far more effective than ANN for image classification on CIFAR-10 due to its ability to preserve and learn spatial features.
