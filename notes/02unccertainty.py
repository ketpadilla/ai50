
### * UNCERTAINTY
## Used in AI to make inferences with incomplete information by using probaability.

## * PROBABILITY THEORY
# A branch of mathematics that deals with calculating the likelihood of events.
'''
    States that for a given event, there are many possible worlds (w), where each world has a probability (P(w)).
        - Every probability is between 0 and 1:     0 ≤ P(w) ≤ 1 (inclusive)
            1 - Certain
            0 - Impossible
        - The sum of all probabilities is 1:        ∑ P(w) = 1

        For a pair of events A and B:
            - each event may or may not have the same probability with other events
            - however, the sum of the probabilities will never be the same with other pairs of events

    UNCONDITIONAL PROBABILITY
    the degree of belief in a proposition (P(A)) without any other information
    calculates the probability of an event A by dividing the number of ways event A can occur by the total number of possible events
'''

## * CONDITIONAL PROBABILITY
# the degree of belief in a proposition (P(A|B)) given some other information (B) that is known
#! P(A|B) = P(A ^ B) / P(B)
#! P(B|A) = P(A ^ B) / P(A)
'''
    - P(A|B) is read as "the probability of A given B"
    
    derived formulas:
        P(A ^ B) = P(A|B) * P(B)
        P(A ^ B) = P(B|A) * P(A)

    RANDOM VARIABLE
    a variable in probability theory with a domain of possible values it can take on
    may take on non-boolean values

        e.g., Flight = {on time, delayed, cancelled}

    PROBABILITY DISTRITBUTION
    a table of probabilities for each possible value of a random variable

        e.g.,
            P(Flight = on time) = 0.6
            P(Flight = delayed) = 0.3
            P(Flight = cancelled) = 0.1

            or

            P(Flight) = {0.6, 0.3, 0.1}
    
    INDEPENDENCE
    the knowledge/idea that one event does not affect the probability of another event

        formula:
            P(A ^ B) = P(A) * P(B)
'''

## * BAYE'S RULE
# rule used to calculate the probibility of event B given event A
# ! P(B|A) = [P(A|B) * P(B)] / P(A)
'''
    derivation:
        given the formula for conditional probability:
            P(A ^ B) = P(A|B) * P(B)
            P(A ^ B) = P(B|A) * P(A)

        equating the two:
            P(A|B) * P(B) = P(B|A) * P(A)

        therefore, solving for P(B|A):
            P(B|A) = [P(A|B) * P(B)] / P(A)

    e.g.,
        Given clouds in the morning, what's the probability of rain in the afternoon?
        • 80% of rainy afternoons start wiht cloudy mornings.
        • 40% of days have cloudy mornings.
        • 10% of days have rainy afternoons.

        P(Rain|Clouds) = [P(Clouds|Rain) * P(Rain)] / P(Clouds)
                       = [0.8 * 0.1] / 0.4  
                       = 0.2
        
    * Knowing P(visible effect | unknown cause), we can calculate P(unknown cause | visible effect)
'''

## * JOINT PROBABILITY
# the probability of two or more events occurring together
'''
    e.g., 
        GIVEN:
            P(cloud) = 0.4
            P(not cloud) = 0.6
            P(rain) = 0.1
            P(not rain) = 0.9

            joint probability table:
                     | cloud | not cloud
            -----------------------------
            rain     | 0.08  | 0.32
            -----------------------------
            not rain | 0.02  | 0.58

        ? for P(cloud | rain):
            P(cloud | rain) = P(cloud ^ rain) / P(rain) 
                            = 0.08 / 0.1
                            = 0.8

                or
            
            P(cloud | rain) = a * P(cloud ^ rain)
                            = a<0.08, 0.02>
                            = <0.8, 0.2>

                    * a must be 10 for the sum of the probabilities to be 1
'''

## * OTHER PROBABILITY RULES
'''
    NEGATION
    the probability of an event not occuring
        P(¬A) = 1 - P(A)

    DISJUNCTION
    the probability of either one of two events occuring
    uses inclusion-exclusion principle:
        P(A v B) = P(A) + P(B) - P(A ^ B)

    MARGINALIZATION
    the probability of an event occuring using their joints probabilities with another event
        P(A) = P(A ^ B) + P(A ^ ¬B)

            e.g.,
                     | cloud | not cloud
            -----------------------------
            rain     | 0.08  | 0.32
            -----------------------------
            not rain | 0.02  | 0.58
    
            ? for P(cloud):
                P(cloud) = P(cloud ^ rain) + P(cloud ^ not rain)
                         = 0.08 + 0.02
                         = 0.1
    
    CONDITIONING
    the probability of an event occuring given their conditional probabilities with another event
        P(A) = P(A|B) * P(B) + P(A|¬B) * P(¬B)
'''

## * BAYESIAN NETWORK
# a probabilistic model
# data structure that represents the dependencies (joint probability) among random variables
'''
    Characteritics
        • a directed graph
        • each node represents a random variable
        • arrow from X to Y means X is a parent of Y
            -> P(X|Parents(X))

    e.g.,
                        Rain
                {none, light, heavy}
                    |           |
                    v           |
                Maintenance     |
                 {yes, no}      |
                    |           |   
                    v           V
                        Train
                 {on time, delayed}
                          |
                          V
                      Appointment
                    {attend, miss}
        
                
        * Appointment is dependent on Train which is dependent on Rain and Maintenance which is also dependent on Rain
            let P(Rain) = {0.7, 0.2, 0.1}   <- an unconditional probability distribution as it has no parents 

        * the rest are conditional probability distributions as they have parents
            let P(Maintenance):
                Rain    |   yes     |   no
                none    |   0.4     |   0.6
                light   |   0.2     |   0.8
                heavy   |   0.1     |   0.9
            
            let P(Train):
                Rain    |   Maintenance |   on time     |   delayed
                none    |   yes         |   0.8         |   0.2
                none    |   no          |   0.9         |   0.1
                light   |   yes         |   0.6         |   0.4
                light   |   no          |   0.7         |   0.3
                heavy   |   yes         |   0.4         |   0.6
                heavy   |   no          |   0.5         |   0.5

            let P(Appointment):
                Train   |   attend  |   miss
                on time |   0.9     |   0.1
                delayed |   0.6     |   0.4 


        COMPUTING JOINT PROBABILITIES
            ? P(light, no) = P(light) * P(no|light)
                           = 0.2 * 0.8
                           = 0.16

            ? P(light, no, delayed) = P(light) * P(no|light) * P(delayed|light, no)
                                    = 0.2 * 0.8 * 0.3
                                    = 0.048
            
            ? P(light, no, delayed, miss) = P(light) * P(no|light) * P(delayed|light, no) * P(miss|delayed)
                                          = 0.2 * 0.8 * 0.3 * 0.4
                                          = 0.0192        
'''

## * INFERENCE WITH PROBABILITY
'''
    Characteritics of Inference Probability Problems
        1. Query X: computes distribution
        2. Evidence E: observed variables for event e
        3. Hidden variables Y: non-evidence and non-query variables (inaccessible)
        4. Goal: Calculate P(X|e)

        e.g.,
            [hidden variable: maintenance and train]
                                ? P(Appointment|light, no)             
            []                       = a * P(Appointment, light, no)
            [marginalization]        = a * [P(Appointment, light, no, on time) + P(Appointment, light, no, delayed)]
    
    INFERENCE BY ENUMERATION
        P(X|e) = a * P(X, e) = a * ∑ P(X, e, y) for all y
    
    POMEGRANATE
    a Python library for probabilistic modeling that uses Bayesian networks

        • Node() - creates a node/variable
        • DiscreteDistribution() - creates an unconditional probability distribution
        • ConditionalProbabilityTable() - creates a conditional probability distribution   
        • BayesianNetwork() - creates a Bayesian network
        • .add_states() - adds nodes to a Bayesian network
        • .add_edge() - adds edges to a Bayesian network 
        • .bake() - finalizes the structure of a Bayesian network
        • .probability() - calculates the probability of a given set of events where all events are known
        • .predict_proba() - calculates the probability of a given set of events where one or more events are unknown
'''

## * APPROXIMATE INFERENCE
# to approximate the inference procedure
'''
    SAMPLING
    takes samples of all of the nodes in a Bayesian network to calculate the probability of the query node 

    REJECTION SAMPLING
    to eliminate samples that do not match the evidence and calculate the probability of the query node with the remaining samples

    * more samples = more accurate probability

    LIKELIHOOD WEIGHTING
    to create samples based on the evidence variables to calculate the probability of the query node
        1. fix the values for evidence variables
        2. sample the non-evidence variables using their conditional probability distributions in the Bayesian network
        3. weight each sample by its likelihood: the probability of all the evidence
'''

## * MARKOV MODELS
# a probabilistic model
# used to predict future events 
'''
    provides a random variable for each time step
        e.g., xt : weather at time t

    MARKOV ASSUMPTION
    to assume that the current state depends on only a finite fixed number of previous states
        e.g., today's weather depends only on yesterday's weather

    MARKOV CHAIN
    a sequence of random variables where their distribution follows the Markov assumption

    
'''



