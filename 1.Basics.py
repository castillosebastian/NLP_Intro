print("hello world")
import nltk
nltk.download('book')
from nltk.book import text1
text1 = nltk.book.text1
text1.concordance('monstrous') # busca concordancias en el text1
text1.similar('monstrous')
text2 = nltk.book.text2
text2.similar('monstrous')
text2.common_contexts(["monstrous", "very"])
text1.common_contexts(["monstrous", "whale"])
nltk.book.text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
nltk.book.text3.generate()

# Counting Vocabulary
len(text1)
len(text2)

# Tokens (individual unit of text) and Vocabulary (distinct unit)
len(nltk.book.text3) # count tokens
len(set(nltk.book.text3)) # vocabulary

#   lexical richnes of a text
len(set(text2)) / len(text2)

# Function
def lexical_diversity(text):
    return len(set(text)) / len(text)

# List
nltk.book.sent1

# Frequency Distributions
from nltk import FreqDist
fdist1 = FreqDist(text1)

# Como generar descriptores del texto. Las palabras más repetidas
# Frequency Distribution Plot cumulative.
fdist1.plot(50, cumulative=True)

# Las palabras menos repetidas
fdist1.hapaxes()


# Long Words using len(w)
# "the set of all w such that w is an element of V (the vocabulary) and w has property P".
V = text1
long_words = [w for w in V if len(w) > 15]
sorted(long_words)

# Long words and frecuenty words to typifing text
fdist5 = FreqDist(nltk.book.text5)
sorted(w for w in set(nltk.book.text5) if len(w) > 7 and fdist5[w] > 7)


# Bigrams
from nltk.util import bigrams
list(bigrams(['more', 'is', 'said', 'than', 'done']))

# Complex function
len(set(word.lower() for word in text1 if   word.isalpha()))