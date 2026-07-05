# 📘 Week 6 – Image Denoising using Autoencoder on MNIST

## Project Overview

This project implements a Convolutional Autoencoder to remove noise from handwritten digit images from the MNIST dataset. The model learns compressed image representations through an encoder and reconstructs cleaner images using a decoder.

## Objectives

* Load and preprocess the MNIST dataset.
* Add Gaussian noise to handwritten digit images.
* Build a Convolutional Autoencoder using TensorFlow/Keras.
* Train the model to reconstruct clean images from noisy inputs.
* Compare original, noisy, and reconstructed images.

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Matplotlib

## Files

* `Week6_Image_Denoising_Autoencoder_MNIST.ipynb`
* `README.md`
* `requirements.txt`

## Results

The autoencoder successfully reduced noise while preserving the essential structure of handwritten digits. The reconstructed images demonstrate the ability of encoder-decoder architectures to perform image denoising effectively.

## Learning Outcomes

* Image preprocessing
* Gaussian noise generation
* Convolutional Neural Networks (CNN)
* Autoencoders
* Encoder–Decoder architecture
* Image reconstruction
* Image denoising
