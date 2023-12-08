
### * LANGUAGE

'''
LANGUAGE
NATURAL LANGUAGE PROCESSING
to make computers understand our language
Tasks involved:
- automatic summarization
- information extraction
- machine translation
- question answering
- text classification
Parts of Language to consider
- Syntax - its structure 
- Semantics - its meaning

FORMAL GRAMMAR
a system of rules for generating sentences in a language

Context-Free Grammar
Terminal Symbol - can only be generated once
Non-terminal Symbol - can generate terminal symbols
e.g., N (noun), V (verb), D (determiner), P (preposition), ADJ (adjective)
*Non-terminal symbols can help replaced by non-terminal symbols

nltk LIBRARY
python library for processing natural language

n-gram
a contiguous sequence of n items for a sample of text
*can be used to provide the computer information for what sequences of words normally go together
*uses tokenization

TOKENIZATION
task of splitting a sequence of characters into pieces (tokens)
*can be used to make Markov chains (predict what words will come after a sequence of words)

BAG-OF-WORDS MODEL
model that represents text as an unordered collection of words
*used to do sentiment analysis to classify text
*used to create a naive bayes

NAIVE BAYES
tool used to classify text on Bayes rule
(refer to probability lecture)
assumed all the words are independent to each other
*may not calculate probabilities correctly if a word is not part of the training data

ADDITIVE SMOOTHING
adding a value “a” to each value in a distribution to smooth the data

Laplace Smooth
“a” = 1, assume we have seen each value one more time than we actually have

WORD REPRESENTATION
to convert words into numbers

One-hot Representation
represent words as a vector with a single 1, and the rest as 0
*cannot represent words with similar meanings
*may create vectors that are too long to accommodate many words 

Distributed Representation
represent words/meanings by distribution across multiple values (in vectors)

WORD2VEC
model for generating word vectors, grouping words with similar meanings or used in similar contexts
*similar words have similar vector representations 
*can also determine the relationship between words by calculating the distance between its vector representations

LANGUAGE TRANSLATION
uses word representations (word2vec) and (recurrent) neural networks to translate words from one language to another
Process:
- Encoding
- Decoding
*storing information in encoding phase becomes more difficult as sequence of words increases

alternative: ATTENTION
provide a value to words based on its importance 
*both processes are difficult to parallelize since it depends on previous runs of the recurrent neural network 

TRANSFORMERS
independently processes each word (allowing for parallelization) during the encoding phase 
*loses ordering: positional encoding may be used to remember the order of words
*Self-Attention component: Attention to the other input words to determine its attention value

Encoding Process:
- Input word + Positional Encoding
- Self-attention
- Feed-forward Neural Network
- Encoded Representation 

Multi-Headed Attention - multiple self-attention components are used simultaneously to pay attention to multiple inputs 

Decoding Process:
- Previous output word + positional encoding 
- Self-attention
- Attention (pay attention to encoded representations)
- Feed-forward Neural Network 
- Next output word
'''