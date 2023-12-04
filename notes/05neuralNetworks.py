
### * NEURAL NETWORKS
## * ARTIFICIAL NEURAL NETWORK
# a mathematical model for learning inspired by biological neural networks
'''
  models a mathematical function mappping inputs to outputss based on the network's structure and parameters

  ACTIVATION FUNCTION
  function calculating a node's output (refer to learning algorithms)
    e.g., 
      1. Step Function
        g(x) = 1 if x ≥ 0, else 0
        * can represent "OR" (with -1 bias) and "AND" (with -2 bias)

      2. Logistic Sigmoid
        g(x) = e^x / (e^x + 1)

      3. Rectified Linear Unit (ReLU)
        g(x) = max(0, x)
      
  used -> hw(x) = g(w • x)
  * weights are also called "biases"

  SIMPLE NEURAL NETWORK
  consists of single layer of:
    • input nodes
    • output nodes
    • activation function
'''


## * GRADIENT DESCENT
# algorithm for minimizing loss in training neural networks
'''
  OUTLINE
    1. initialize weights randomly
    2. repeat:
      • calculate gradient baseed on all data points that will lead to drop in loss
      • update weights according to gradient

  -> time complexity: O(n^2)

  STOCHASTIC GRADIENT DESCENT
  calculates gradient based on ONE data point (during iteration)
  -> time complexity: O(n) 
  -> less accurate than gradient descent

  MINI-BATCH GRADIENT DESCENT
  calculates gradient based on a subset of data points (during iteration)
  -> time complexity: O(n)
  -> more accurate than stochastic gradient descent but less accurate than gradient descent

  * activation functions can be used to output probabilities that can be used to classify data (i.e., supervised learning)
'''

## * PERCEPTRON
# a single layer neural network
# only capable of learning linearly separable decision boundaries

## * MULTI-LAYER PERCEPTRON
# aritificial neural network with:
'''
  • an input layer
  • one or more hidden layers
  • an output layer

  uses backpropagation 
    PSEUDOCODE:
      • start with random weights
      • repeat:
        • calculate error for output layer
        • for each layer, starting with output layer and moving inwards towards earliest hidden layer:
          • propagate error backwards
          • update weights

  allows for more complex decision boundaries
  risk of overfitting increases with number of hidden layers
'''

## * DROPOUT
# technique to reduce overfitting 
# temporarily remove selected/random units from a neural network to prevent over-reliance on certain units

## * TENSORFLOW
# Google's open source library to create and train neural networks
'''
  playground.tensorflow.org

  * more hidden layers -> more complex decision boundaries 

'''

## * COMPUTER VISION
# computational methods for analyzing and understanding digital images
'''
  IMAGE CONVOLUTION
  use a filter that addds each pixel value of an image to its neighbors, weighted by a kernel matrix
  
    KERNEL MATRIX
    a matrix of weights
    -> multiply each pixel value by its corresponding weight in the kernel matrix then take their sum
    -> sum of:
        0 -> no change (black)
        255 -> maximum change (white)

  POOLING 
  reduce input size by sampling from regions of the input/image (i.e., downsampling)

    MAX POOLING
    choose maximum value from each region
'''

## * CONVOLUTIONAL NEURAL NETWORK
# neural networks that use convolution and pooling to analyze images\
'''
  GENERAL STRUCTURE:
  convolution -> pooling -> flattening -> input layer -> ...
    * repeat convolution and pooling layers as needed 
'''

## * FEED-FORWARD NEURAL NETWORK
# neural networks that has connections only in one direction
'''
  input -> network -> output
'''

## * RECURRENT NEURAL NETWORK
# neural networks that has connections in both directions (forward and backward)
'''
           |<----
           |    ^
           v    |
  input -> network -> output

  * useful for analyzing sequences of data
  * allows for one-to-many relationships (e.g., image captioning)
'''