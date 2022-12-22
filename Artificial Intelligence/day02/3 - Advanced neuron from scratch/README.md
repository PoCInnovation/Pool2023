# Module 3 : Advanced neuron from scratch :computer:

Welcome to the third day of the AI Pool. Today we will discover the neuron from scratch. We will see how to create a neuron and how to train it. We will also see how to create a neural network with multiple neurons and multiple layers.

# Before starting

Please do all installations in [this document](./SETUP.md)

# Introduction

<div align="center">
    <img src="./img/neural_network.png" width="500px" alt="Neural network"/>
</div>

Multi-layer neural networks are a type of machine learning model used for pattern recognition, classification and prediction. They are inspired by the functioning of the human brain and are composed of several layers of interconnected neurons.

The first layer, called the input layer, takes input from the external environment and passes it to the next layer. Each successive layer processes this data in a more complex way, using processing algorithms and learning from the previously presented examples. The last layer, called the output layer, finally produces an answer or prediction based on the previously processed data.

Neural networks with multiple layers are particularly useful for complex tasks requiring high data processing capacity, such as speech or image recognition. They have also been widely used in many fields, including finance, healthcare and transportation.

It is important to note that neural networks with multiple layers require a considerable amount of training data and can be difficult to implement due to their complexity. However, they are often considered one of the most successful models in machine learning and have therefore been widely used in many applications.

# Submit :trophy:

You must submit your work in the `day02/3 - Advanced neuron from scratch` folder in file `advanced_neuron_from_scratch.py`

# Instructions

## Step 1 - Make a dataset

In this step, we will create a dataset. We will use sklearn to create a dataset. The dataset could be make with a circles and should look like this:

![dataset.png](img/dataset.png)

The dimension of the dataset should be in X: 2, 1500 and in Y: 1, 1500.

We will print the dataset with dimensions to see if it is correct.

# Resources :book:

- [Doc scikit-learn](https://scikit-learn.org/stable/)
- [Doc numpy](https://numpy.org/doc/stable/)
- [Doc matplotlib](https://matplotlib.org/3.3.3/contents.html)
- [Doc tqdm](https://tqdm.github.io/docs/tqdm/)
