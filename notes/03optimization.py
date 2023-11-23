
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
    
        * never makes a "worse" move
'''

## * SIMULATED ANNEALING
# technique used to dislodge from a local maximum/minimum by allowing worse moves
'''
    Basic Idea:
        1. Early on, allow more moves that is worse than the current state (higher temperature)
        2. Later on, allow fewer worse moves (lower temperature)

    Psuedocode:
    • defined function SIMULATED-ANNEALING(problem, max-tries)
        1. initialize current to track the initial/current state
        2. for t = 1 to max-tries:
            2.1. initialize T to track the "temperature" of the system (T = TEMPERATURE(t))
            2.2. initialize neighbor to track a random neighbor of current
            2.3. initialize ∆E to track the difference in value between current and neighbor
            2.4. if ∆E > 0:
                    current = neighbor
                 with probability e^(∆E/T), set current = neighbor
        3. return current
'''

## * TRAVELING SALESMAN PROBLEM (TSP)
# a problem where a salesman must visit each city in a set of cities exactly once and return to the starting city
# the goal is to find the global minimum-cost path

## * LINEAR PROGRAMMING
# used to optimize a mathematical function
'''
    GOAL
        • Minimize a cost function c1x1 + c2x2 + ... + cnxn
        • Subject to constraints:
            a1x1 + a2x2 + ... + anxn <= b
                or
            a1x1 + a2x2 + ... + anxn = b
        • With bounds for each variable 1i <= xi <= ui

        * Contrainst and bounds are linear functions

    ALGORITHMS USED
        1. Simplex
        2. Interior-Point

    PYTHON LIBRARY: scipy 
'''

## * CONSTRAINT SATISFACTION PROBLEM (CSP)
# a problem where a set of variables must be assigned values that satisfy a set of constraints
''' 
    COMPONENTS:
        • Set of variables (X1, X2, ..., Xn)
        • Set of domains for each variable (D1, D2, ..., Dn)
        • Set of constraints (C)

        e.g., Sudoku
            Variables: 81 squares
            Domains: {1, ..., 9} for each square
            Contraints: empty squares cannot have the same value as any other square in the same row, column, or 3x3 subgrid
    
    CONSTRAINT GRAPH 
        representation the constraints of a CSP
        edges represent constraints
        nodes represent variables

    TYPES OF CONSTRAINTS
        1. Hard - must be satisfied
        2. Soft - preferred but not required to be satisfied

    CATEGORIES OF CONSTRAINTS                               e.g.,
        1. Unary - constaints only one variable             A ≠ Monday
        2. Binary - constraints two variables               A ≠ B

    NODE CONSISTENCY
        when all values in a variable's domain satisfy its unary constraints
        to remove values from a domain that do not satisfy its unary constraints

    ARC CONSISTENCY
        node consistency for binary constraints
        to remove values from domain X until every choice for X has a possible choice for Y in its domain

    PSEUDOCODE:
    • define function REVISE(csp, X, Y):    # will make X arc-consistent with Y
        1. initialize revised to track whether a domain has been revised (revised = false)
        2. for each x in X.domain:
            2.1. if no y in Y.domain satisfies the constraint for (X, Y):
                    delete x from X.domain
                    revised = true
        3. return revised

    • define function AC-3(csp):            # will make all variables arc-consistent
        1. initialize queue to track all arcs in csp (queue = all arcs in csp)
        2. while queue non-empty:
            2.1. (X, Y) = DEQUEUE(queue)
            2.2. if REVISE(csp, X, Y):
                    if X.domain == 0: 
                        return false
                    for each Z in X.neighbors - {Y}:
                        ENQUEUE(queue, (Z, X))
        3. return true
'''

## * CSPs AS SEARCH PROBLEMS
'''
    INITIAL STATE
    empty assignment (no variables)

    ACTIONS
    add a {variable = value} to the assignment

    TRANSITION MODEL
    shows how addign an assignment changes the assignment

    GOAL TEST
    check if all variables assigned and all constraints satisfied

    PATH COST FUNCTION
    all paths have same cost
'''

## * BACKTRACKING SEARCH
# search algorithm that makes assignments from variables to values, backtracks when a variable has no legal values left to assign, and takes another path
'''
    PSEUDOCODE:
    function BACKTRACK(assignment, csp):
        if assginment complete: 
            return assignment
        var = SELECT-UNASSIGNED-VARIABLE(assignment, csp)
        for value in DOMAIN-VALUES(var, assignment, csp):
            if value consistent with assignment:
                add {var = value} to assignment
                result = BACKTRACK(assignment, csp)
                if result ≠ failure:
                    return result
            remove {var = value} from assignment
        return failure

    PYTHON LIBRARY: constraint (pip install python-constraint)
'''

## * MAINtAINING ARC-CONSISTENCY
# algorithm that maintains arc-consistency when there's a new assignment via interleaving inference and search
'''
    when new assignment is made:
        call AC-3
        start with a queue of all arcs where they are neighbors of the variable that was just assigned

    REVISED PSEODOCODE:
    function BACKTRACK(assignment, csp):
        if assginment complete: 
            return assignment
        var = SELECT-UNASSIGNED-VARIABLE(assignment, csp)
        for value in DOMAIN-VALUES(var, assignment, csp):
            if value consistent with assignment:
                add {var = value} to assignment
                inferences = INFERENCE(assignment, csp)
                if inferences ≠ failure:
                    add inferences to assignment
                result = BACKTRACK(assignment, csp)
                if result ≠ failure:
                    return result
            remove {var = value} and inference from assignment
        return failure

    * backtracking is done less by making inferences
'''

## * OTHER OPTIMIZATIONS
'''
    SELECT-UNASSIGNED-VARIABLE
    choose a random unassigned variable

        Alternatives
            1. minimum remaining values (MRV) - choose the variable with the smallest domain

            2. degree heuristic - choose the variable with the highest degree (most constraints)

    DOMAIN-VALUES
    choose a random value from the domain

        Alternatives
            1. least-constraining value - return variables in order by nymber of choices that are ruled out for neighboring variables
                * try least-constraining values first
'''