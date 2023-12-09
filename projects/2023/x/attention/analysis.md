# Analysis

## Layer 3, Head 1

The text used was:
"It was as tall as the [MASK]." 

Looking through the 144 diagrams representaion the attention layers of BERT in anaylzing the provided sentence, head 1 of layer 3 clearly dsiplays the what words are attending strongly to specific words. 

The layer and head shows that each it is attending strongly to the word following it. "It" is attending strongly to "was" as it is attending strongly to "as" and so on and so forth.

This is should a reasonable inference in making sense of the text. The text describes an object, "it" to be similar in height or "as tall as" as another object "[MASK]." Therefore, for the computer to understand this comparative nature, it should understand that each word is as important in meaning independently and jointly with the word succeeding it in determining the meaning of the text. 

Layer 3, Head 10 also shows these attention values.

Example Sentences:
- It was as tall as the others.
- It was as tall as the other.
- It was as tall as the moon.

## Layer 4, Head 6

The text used was:
"Holmes ran [MASK]."

Heads 1 and 10 of Layer 3 also showed a similar nature for the text provided now compared to the previous text. The reason why I used a shorter text is because I wish to assume that the verb "ran" would focus on the noun "Holmes" to make sense of the text. By having the verb attending stronly to the noun, the computer can understand that the noun is doing the verb. However, the manner by which it is doing the verb was still unclear. That is, Holmes did ran, but did he ran away, ran furiously, or anything of similar note?

In this case, the most common words to be attached to a text like this is "away," "off," and "out." 

In Layer 4, head 6, the word "ran" is attending strongly to the word "Holmes" as "[MASK]" is attending strongly to "ran." We can interpret this as the word "ran" knowing that is it describing "Holmes" as "[MASK]" knowing it that is is describing "ran." 

Example Sentences:
- Holmes ran away.
- Holmes ran off.
- Holmes ran out.

