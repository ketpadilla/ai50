# TRAFFIC
### Screencast
https://youtu.be/74ZUTHL9VRE

### Experimentation Process
Since we are using the same Python Library from the lectures, I began with using the convolutional neural network shown during the time. The said neural network had:
* a convolution layer
* a max pooling layer
* a flattening layer
* a dense hidden layer with 128 nuerons; and
* 1 dropout layer set at 0.5

The initial results were: **loss: 3.4962 - accuracy: 0.050 (5.09%)**

Before changing anything from the neural network, I first optimized the rate for the droupout layer.

Increasing the dropout rate (to 0.7) yielded worse results: **loss: 3.5145 - accuracy: 0.0563 (5.63%)**. Therefore, the dropoutrate should be reduce to optimize the neural network. At a rate of 0.3, the network outputted: **loss: 3.4959 - accuracy: 0.0543(5.43%)**. So far, the difference of the results to the training results are about: _loss: ±0.004 - accuracy: ±0.002_. Thus, there should be no overffiting of data.

Results of other lower dropout rates are as follows:
* (0.25):
  - performance: _loss: 1.3460 - accuracy: 0.5565_ 
  - training: _loss: 1.8042 - accuracy: 0.4467_
* (0.2):
  - performance: _loss: 0.5118 - accuracy: 0.8623_ 
  - training: _loss: 0.8793 - accuracy: 0.7392_
* (0.15):
  - performance: _loss: 0.4617 - accuracy: 0.0.8842_ 
  - training: _loss: 0.5279 - accuracy: 0.8462_
* (0.1):
  - performance: _loss: 0.3221 - accuracy: 0.9219_
  - training: _loss: 0.3601 - accuracy: 0.8994_ 
* (0.05): 
  - performance: _loss: 0.1483 - accuracy: 0.9700_
  - training: _loss: 0.1483 - accuracy: 0.9244 _

Based on the results, using a dropout rate lower than 0.2 (2.0%) seems to begin to overfit the training data. While, using a dropout rate higher than that decreases the performance of the nueral network. Thus, a drouput rate of 0.2 would be used from here on out.

Now, adding another convolution and max pooling layer yielded the following results: **loss: 0.2425 - accuracy: 0.9520**. Adding another, for a total of three convolution and max pooling layers, yielded worse results: **loss: 0.2662 - accuracy: 0.9419**. Therefore, two convolution and max pooling layers should be enough for the neural network. 

Adding another hidden layer with dropout yielded far worse results: **loss: 0.3705 - accuracy: 0.9002**. Therefore, the number of hidden layers with dropouts should be one (1).

From this point on, possible optimizations would come from increasing or decreasing the number of neurons and/or pool sizes from the layers. No increase od decrease in neurons or pool size yielded better results. 

Therefore, the following neural network specifications serves best for the project:
* two convolution layers (with 32 neurons at a size of 3x3)
* two max pooling layers (with a size of 2x2)
* a flattening layer
* a dense hidden layer with 128 nuerons; and
* 1 dropout layer set at 0.2