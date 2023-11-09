# https://cs50.harvard.edu/ai/2023/notes/1/

## * Knoweldge-Based Agents
# agents that reason and operate on based internal representations of knowledge
'''
    SENTENCE
    - assertence about the world in a knowledge representation language

    KNOWLEDGE REPRESENTATION LANGUAGE
    - a way to represent information in AI

    PROPOSITIONAL LOGIC 
        Proposition Symbols - represent sentences (P, Q, R, ...)
        Logical Connectives - connect sentences
            1. NOT (¬)
            2. AND (^)
            3. OR (v)
            4. IMPLICATION (=>)
            5. BICONDITIONAL (<=>)
'''

    ## ! NOT (¬)
    # inverts the truth value of a sentence
    # ex. P is true, ¬P is false

    ## ! AND (^)
    # combines two sentences into one
    # ex. P ^ Q is true only if both P and Q are true

    ## ! OR (v)
    # combines two sentences where one or both are true
    # ex. P v Q is true if either P or Q is true

    ## ! IMPLICATION (=>)
    # one sentence implies another 
    # if one sentence is true, then the other is true,
    # if the implication is false, then it makes no claim about the truth of the other sentence
'''  table:
        P | Q | P => Q
        T | T | T
        T | F | F
        F | T | T
        F | F | T
'''

    ## ! BICONDITIONAL (<=>)
    # two sentences are true or false together (if and only if)
'''  table:
        P | Q | P <=> Q
        T | T | T
        T | F | F
        F | T | F
        F | F | T
'''

## * Model
# assignment of truth values (true or false) to all proposition symbols in a knowledge base
# equates to a "possible world"

## * Knowledge Base
# a set of sentences known by a knowledge-based agent to be true (or false)

## * Entailment (|=)
# a |= b (alpha entails beta)
# in every model where alpha is true, then beta is also true 

## * Inference
# the process of deriving new sentences from old ones
# !! 19:02

