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
    # reger to tables above for examples

## * Knowledge Base (KB)
# a set of sentences known by a knowledge-based agent to be true (or false)
# sentences combined via proprositional logic

## * Entailment (|=)
# a |= b (alpha entails beta)
# in every model where alpha is true, then beta is also true 

## * Inference
# the process of deriving new sentences from old ones
'''
    INFERENCE ALGORITHM
        answers questions about entailment
        aims to determine if KB |= alpha (query)

    MODEL CHECKING
        enumerate all possible models
        checks where KB and alpha are true in all models, if it exists, then KB |= alpha
        * inefficient for large knowledge bases
'''

## * Application
''' 
    Create a class for:
        • sentences (to use as a data type)
        • symbols (P, Q, etc.) (can only be true or false)
        • logical connections (Not, And, etc.)
        • algorithm that takes in knowledge and query (model checking)

    Knowledge is declared as a variable with value type Sentence
        e.g, knowledge = And(Or(P, Q), Not(R), ...)
    
    Query is declared as a variable with value type Sentence

    Loops may be used to declare multiple sentences of similar structure
        e.g., Each person belongs to a house:
            for person in people:
                knowledge.add(Or(
                    Symbol(f"{person}Gryffindor"),
                    Symbol(f"{person}Hufflepuff"),
                    Symbol(f"{person}Ravenclaw"),
                    Symbol(f"{person}Slytherin")
                ))
'''

## * Knowledge Engineering
# process of determining the logical symbols to use on sentences to encode knowledge

## * INFERENCE RULES
# rules that allows to use existing knowledge to derive new knowledge
    # premise (existing knowledge)
    # conclusion (new knowledge after applying logic)
# alternative to model checking
'''
    MODUS PONENS (application of implication)
        if a => b and a is true, then b is true
        diagram:
            a => b
              a
            ------
              b

        * does not refer to any specific "world"

    AND ELIMINATION
        if a ^ b is true, then a is true and b is true
        diagram:
            a ^ b
            ------
              a
              b

    DOUBLE NEGATION INTRODUCTION
        if not not a is true, then a is true
        diagram:
            ¬¬a
            ------
              a

        e.g., it is not true that it is not raining, thus it is raining

    IMPLICATION ELIMINATION (Convert if-then to or)
        if a => b, then not a or b
        diagram:
            a => b
            ------
            ¬a v b

    BICONDITIONAL ELIMINATION (Convert if-and-only-if to and)
        if a <=> b, then (a => b) ^ (b => a)
        diagram:
            a <=> b
            ------
            (a => b) ^ (b => a)

    DE MORGAN'S LAWS (convert not-and to or-not and vice versa)
        not-add -> or: 
            if not (a ^ b), then not a or not b
            diagram:
                ¬(a ^ b)
                ------
                ¬a v ¬b
            
            e.g., it is not true that it is raining and sunny, thus it is not raining or not sunny

        not-or -> and:
            if not (a v b), then not a and not b
            diagram:
                ¬(a v b)
                ------
                ¬a ^ ¬b
            
            e.g., it is not true that it is raining or sunny, thus it is not raining and not sunny
'''

# !! 1:13:40