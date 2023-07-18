- [Best Article by Christopher Olah](https://colah.github.io/posts/2015-08-Backprop/)
- [27. Backpropagation: Find Partial Derivatives](https://www.youtube.com/watch?v=lZrIPRnoGQQ)

# Automatic Differentiation

Set of techniques to evaluate the partial derivative of a function specified by a computer program

By applying the chain rule repeatedly, partial derivatives of arbitrary order can be computed automatically

## Types

- forward accumulation
- reverse accumulation

Backpropagation in a multilayer perceptron is a special case of **reverse accumulation**

Forward gave us the derivative of our ouput with respect to a single input, but reverse mode-differentiation gives us all of them

## Why learn backprop

- Composite of functions = multiplication of gradients
- Automatic differentiation is implemented in modern machine learning tools
- Learn concepts of calculations of gradients

