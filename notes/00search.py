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

'''

## ! 56:02
# https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/block-v1:HarvardX+CS50AI+1T2020+type@sequential+block@a52582b244c849289b4745d601fa6d43/block-v1:HarvardX+CS50AI+1T2020+type@vertical+block@c52e9c5a2ffc4c658dbf2ead90eca070
