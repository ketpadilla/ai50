# https://cs50.harvard.edu/ai/2023/notes/0/

## * Artificial Intelligence
'''
    techniques that enable computers to mimic human behavior
    e.g.,
        - search: find solutions to problems
        - knowledge: understand, represent, and draw inferences from information
        - uncertainty: deal with uncertain event/information using probability
        - optimization: find the better best solutions
        - learning: improve machine performance based on access to data and experience
        - neural networks: program stucture inspired by the brain to perform tasks effectively
        - language: process natural language
'''

## * Search
# involve an agent given an initial and goal states that reutrns a solution (or failure) path between the two states
'''
    sample problems: mazes and puzzles

    terminology:
    AGENT - entity that perceives its environment and acts upon that environment

    STATE - configuration of the agent and its environment
        • INITIAL STATE - state in which the agent begins
        • GOAL STATE - state in which the agent wants to end

    ACTIONS - choices that can be made in a state
        * function ACTIONS(state) returns set of actions that can be executed in state "s"

    TRANSITION MODEL - model that describes the state that was reached from another state by performing an action
        * function RESULT(state, action) returns the state resulting from performing action "a" in state "s"

    STATE SPACE - set of all states reachable from the initial state by any sequence of actions (representable as nodes in a graph)

    GOAL TEST - a function/condition that determines whether a given state is a goal state

    PATH COST - numerical cost associated with a given path (used to determine the best path)   
'''

## * Solving Search Problems
'''
    SEARCH PROBLEM
    consists of:
        1. initial state
        2. actions
        3. transition model
        4. goal test
        5. path cost function
    
    SOLUTION - sequence of actions that leads from the initial state to the goal state
        • OPTIMAL SOLUTION - solution with the lowest path cost
    
    NODE - data structure that keeps track of:
        1. state
        2. parent (previous node; node that generated this node)
        3. action (action done; action applied to parent to get node)
        4. path cost (from initial state to node)
    
    FRONTIER - set of all possible unexplored nodes from a given state
'''

    # ! ** SEARCH ALGORITHM **
    # 1. Start with a frontier that contains the initial state (one state)
    # 2. Start with an empty explored set (no states)
    # 3. Repeat:
    #     a. if the frontier is empty, then no solution
    #     b. remove a node from the frontier
    #     c. if the removed node contains goal state, return the solution
    #     d. else, add the current node to the explored set
    #     e. and expand the node
    #     f. add resulting nodes not in the explored set to the frontier
    
    # * keep track of explored states and do not add them to the frontier to avoid infinite loops between reversible actions and states
    # * it is important to determine how nodes are added and removed from the frontier

'''
    STACK 
    - data structure that follows the LIFO (last-in, first-out) principle
    - used for adding and removing nodes from the frontier

    QUEUE
    - data structure that follows the FIFO (first-in, first-out) principle
    - used for adding and removing nodes from the frontier

    Types of Search Algorithms:
        DEPTH-FIRST SEARCH (DFS) - search algorithm that uses a stack
            * faster but may not find the optimal solution
        BREADTH-FIRST SEARCH (BFS) - search algorithm that first expands the shallowest nodes in the frontier (uses a queue)
            * slower but will find the optimal solution
'''

## * Classes
# template for creating objects
'''
    TEMPLATE
        class Name:
            def __init__(self, var1, var2):
                self.var1 = var1
                self.var2 = var2

            def method(self, var3):
                return var3
''' ## ! TEMPLATE FOR SEARCH ALGORITHM
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = [] ## empty list
    
    def add(self, node):
        self.frontier.append(node) ## add node to the end of the list

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier) ## check if any node in the frontier has the same state as the given state
    
    def empty(self):
        return len(self.frontier) == 0 ## check if the frontier is empty
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier") 
        else:
            node = self.frontier[-1] ## get the last node in the frontier
            self.frontier = self.frontier[:-1] ## remove the last node in the frontier
            return node

class QueueFrontier(StackFrontier):
    # inherits functions from StackFrontier but overrides its remove function
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

## ! refer to src0/maze.py for sample implementation of solving, goal test, and path cost using search algorithm

## * Searches (Cont.)
'''
    Uninformed sesarch - does not use any problem-specific knowledge
        1. Breadth-First Search (BFS)
        2. Depth-First Search (DFS)

    Informed search - uses problem-specific knowledge to find solutions more efficiently
        1. Greedy Best-First Search
        2. A* Search

'''

## * Greedy Best-First Search
# expands the node closest to the goal based on a heuristic function "h(n)"
'''
    h(n):
    estimates the cost of the cheapest path from the state at node "n" to a goal state

    Manhattan Distance 
    - calculates the distance between two vectors along axes at right angles, ignoring any features
    - sum of distances between x and y coordinates

    For Greedy Best-First Search: first expands the node with the smallest value of its heuristic function
        • quality of algorithm will depend on the quality of its heuristic 
        • may not always find the optimal solution as it finds the optimal choice locally (hence greedy)
'''

## * A* Search
# algorithm that uses a heuristic function h(n) and cost function g(n)
'''
    • g(n) - cost to reach current node
    • h(n) - estimated cost/distance to goal

    first expands the node with the lowest value of g(n) + h(n)

    only optimal if:
    1. h(n) is admissible; never overestimate
    2. h(n) is consistent [h(n) of current state should not be greater than h(n) + g(n) of the next state

    alternatives exists that uses less memory 
'''

## * Adversarial Search
# algorithm faces another agent with the opposite goal
'''
    possible outcomes:
        - -1 (opponent wins)
        - 0 (tie)
        - 1 (user wins)
'''

## * Minimax
# recursive algorithm that simulates all possible choices (between all participating agents) that take place from a current state until a terminal state is reached and choices the one with the desired outcome
'''
    Max - aims to maximize score
    Min - aims to minimize score

    e.g., TicTacToe (classes req.)
        S0 - initial state
        Player(s) - returns which player to move in state s
        Actions(s) - returns legal moves in state s
        Result(s,a) - returns state after action a taken in state s
        Terminal(s) - check if state s is a terminal state (when a player reaches their goal)
        Utility(s) - final numerical value for terminal state s

    • Result(s,a) is the transition model

    • Given a state s, MAX picks action a in Actions(s) that produces the highest value of Min-Value(Result(s,a)) : vice versa for MIN
        - MAX/MIN considers the result its counterpart will choose
'''

## * Alpha-Beta Pruning
# optimizes Minimax by skipping recursive computations that are decidedly unfavorable
'''
    MAX: skips nodes when current node (beta) is less than saved node (alpha); saves for the reversed condition
    
    MIN: skips nodes when current node (beta) is greater than saved node (alpha); saves for the reversed condition  
'''

## * Depth-Limited Minimax
# sets a limit of steps to look into to reduce computation load and uses an evaluation function to determine most optimal step
'''
    evaluation function - estimates the expected utility of the game from a given state

    • quality of algorithm depends on the quality of the evaluation function
'''

## ! Search algorithms - used when AI is tasked to make a decision

## * Quiz 1
'''
    1. BFS will sometimes, but not always, find a shorter path than DFS
    2. ___
    3. Depth-limited minimax can arrive at a decision more quickly because it explores fewer states
    4. 5
'''