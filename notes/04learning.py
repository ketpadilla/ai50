
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
    adds a regularization term to the loss function
        • lambda -> y; regularization parameter
        • complexity(h) -> complexity of hypothesis function h

    HOLDOUT CROSS-VALIDATION
    splits data set into:
        1. training set - where learning occurs
        2. testing set - where evaluation occurs

    K-FOLD CROSS-VALIDATION
    splits data into k sets
    experiments k times, using each set as a test set once and the rest as training sets
'''

## * SCIKIT-LEARN
# a machine learning library for Python

## * REINFORCEMENT LEARNING
# an agent that learns what actions to take in an environment based on rewards and punishments
'''
    MARKOV DECISION PROCESS
    model for decision-making, consisting of:
        1. states -> s
        2. actions -> ACTIONS(s)
        3. transition model -> P(s' | s, a)
        4. reward function -> R(s, a, s')
'''

## * Q-LEARNING
# to learn a function -> Q(s, a) that estimates the value of taking action a in state s
'''
    Overview
        1. initialize Q(s, a) to 0 for all s, a
        2. when action is taken and reward is received:
            • Estimate the value of Q(s, a) using current and expected future rewards
            • Update Q(s, a) to take into account old and new estimates

            -> Q(s,a) = Q(s,a) + a(new estimate - old estimate)
            -> Q(s,a) = Q(s,a) + a((r + y*max(Q(s',a')) - Q(s,a))
    

    EXPLORE-EXPLOIT TRADEOFF
        Explore - explores unknown information to maximize reward
        Exploit - uses known information to maximize reward

        * AI that only exploits may miss out on better rewards
    
    E-GREEDY
    set e (epsilon) to how often to explore (choose random action)
        • set probability e - 1 to exploit (choose estimated best action)
    
    FUNCTION APPROXIMATION
    approximates Q(s, a) using a function than storing a value for every state-action pair
        • reduces memory usage from training data
'''

## * UNSUPERVISED LEARNING
# given input data without labels, to learn patterns and structure

## * CLUSTERING
# group a set of objects with similar objects in the same group
'''
    Applications:
        1. Genetic research
        2. Image segmentation
        3. Market research
        4. Medical imaging
        5. Social network analysis
'''

## * K-MEANS CLUSTERING
# group data points into k clusters, reassigning points to the closest cluster center, repeating until convergence