
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

#! 49:13

