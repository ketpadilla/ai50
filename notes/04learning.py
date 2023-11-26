
### ! LEARNING
## * MACHINE LEARNING
# to provide computers access to data to learn how to do something

## * SUPERVISED LEARNING
# given a data set of input-output pairs, learn a function to map inputs to outputs

## * CLASSIFICATION
# learns a hypothesis function h(x) to map inputs into discrete categories
'''
    h(x) approximates f(x)
    f(x) is the true function that is usually complex and unknown

    NEAREST-NEIGHBOR CLASSIFICATION
        given an input, chooses the class of data point nearest to it

    K-NEAREST-NEIGHBOR CLASSIFICATION
        nearest-neighbor classification but with k (k > 1) nearest neighbors

    LINEAR REGRESSION
        to find a line that best fits the data points (2D)
        
            * not all data sets are linearly separable (can be separated by a line)

        Implementation
            hw(x) = 1 if (w • x) >= 0
                  = 0 otherwise
            
                    • h -> hypothesis function
                    • w -> weight vector
                    • x -> input vector

                uses dot product to determine h(x) as a weighted sum for linear regression
        
        Weight Vector (w)
        the vector being estimated
        -> w0, w1, ..., wn

        Input Vector (x)
        -> 1, x1, x2, ..., xn
        
    PERCEPTRON LEARNING RULE
    given data point (x, y), update each weight:
        wi = wi + a(y - hw(x))xi

            • wi -> weight vector at index i
            • a -> learning rate
            • y -> actual output
            • hw(x) -> estimated value
            • xi -> input vector at index i
'''

## * THRESHOLD FUNCTION
# implmentation of the perceptron learning rule
'''
    HARD THRESHOLD 
    only outputs 1 or 0 
    used by linear regression

    SOFT THRESHOLD
    outputs a value between 0 and 1
    provide a gradient for weaker estimations
    used by logistic regression 
'''

## * SUPPORT VECTOR MACHINES
# a classfication algorithm
# uses a support vector near the decision boundary to classify data points
'''
    can work in higher dimensions to separata non-linearly separable data sets
    
    MAXIMUM MARGIN SEPARATOR
    boundary (line) maximizing the distance between data points
'''

## * REGRESSION
# learns a hypothesis function to map inputs to continuous outputs
'''
    can also use linear and logistic regressions 
    
    similar to optimization problems:
        minimizes...
            LOSS FUNCTION
            measures the error of the hypothesis function

        maximizes...
    
    0-1 LOSS FUNCTION
    L(actual, estimated) = 0 if actual == estimated 
                         = 1 otherwise

        outputs the sum of misclassified data points

    L1 LOSS FUNCTION
    L(actual, estimated) = |actual - estimated|

        outputs the sum of absolute differences between actual and estimated
        used for regression

    L2 LOSS FUNCTION
    L(actual, estimated) = (actual - estimated)^2

        outputs the sum of squared differences between actual and estimated
        used for regression
        minimizes outliers
'''

## * OVERFITTING
# when a model fits too closely to a data set, failing to generalize to future data

## * REGULARIZATION
# penalizes more complex hypotheses, favoring simpler, more general ones
# helps prevent overfitting
'''
    cost(h) = loss(h) + y*complexity(h)

'''
#! 56:20