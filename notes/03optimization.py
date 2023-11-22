
### * OPTIMIZATION
## Choosing the best option from a set of options

## * LOCAL SEARCH
# a search algorithm that only maintains a single node and searches by moving to a neighboring node
'''
    it does not simultaneously explore multiple paths

    useful for problems where only the solution matters 
'''

## * STATE SPACE LANDSCAPE
# a visualization (diagram) of the cost (in vertical bars) of each state in a search problem
'''
    calculated by a heuristic function
    
    can be used to determine the global maximum/minimum of an objective/cost function
'''

##! Strategy for Local Search
# * take a state, maintaining some current node, and move in a state-space landscape to find a global maximum/minimum

## * HILL CLIMBING
# to move to a neighboring state with a lower/higher value to find a global minimum/maximum
'''
    Psuedocode:
    • define function HILL-CLIMB(problem) 
        1. initialize current to track the initial/current state
        2. repeat:
            2.1. initialize neighbor to track the highest/lowest-valued neighbor of current
            2.2. if neighbor is not better/worse than current: 
                    return current
                 current = neighbor
    
    * may not always find the optimal solution as it may get stuck in a local maximum/minimum (local optima)

    Shoulder - a region of a state-space landscape that is flat (no change in value) but can be overcome by a large enough step size

    Plateau - a region of a state-space landscape that is flat that cannot be overcome by a large enough step size

    VARIANTS:
        1. Steepest-Ascent - choose the highest-valued neighbor
        2. Stochastic - choose a random neighbor from a set of higher-valued neighbors
        3. First-choice - choose the first higher-valued neighbor
        4. Random-restart - conduct hill-climbing multiple times 
        5. Local beam search - choose the k highest-valued neighbors (k = beam width)
        6. 

'''

#! 21:04