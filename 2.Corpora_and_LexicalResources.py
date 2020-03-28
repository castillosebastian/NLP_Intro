# Accessing Text Corpora and Lexical Resources
import nltk
ema = nltk.corpus.gutenberg.words('austen-emma.txt')
len(ema)
from nltk.corpus import gutenberg
gutenberg.fileids()
#Program for extract information of gutenberg files
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences[1116]
# len de la sentencia más larga
longest_len = max(len(s) for s in macbeth_sentences)
# Extraccion de la sentencia más larga
[s for s in macbeth_sentences if len(s) == longest_len]

# Brown corpus
from nltk.corpus import brown
brown.categories()
brown.words(categories = 'news')
brown.words(fileids = ['cg22'])
brown.sents(categories=['news', 'editorial', 'reviews'])

# Explore the modals
# The Brown Corpus is a convenient resource for studying systematic differences between genres,
# a kind of linguistic inquiry known as stylistics.Let's compare genres in their usage of modal verbs.
# The first step is to produce the counts for a particular genre. Remember to import nltk before doing the following:
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']

for m in modals:
    print(m + ':', fdist[m], end=' ')

# Loading your own Corpus
# If you have your own collection of text files that you would like to
# access using the above methods, you can easily load them with the help of NLTK's PlaintextCorpusReader.
# Check the location of your files on your file system; in the following example,
# we have taken this to be the directory /usr/share/dict. Whatever the location, set this to be the value of corpus_root [1].
# The second parameter of the PlaintextCorpusReader initializer [2] can be a list of fileids, like ['a.txt', 'test / b.txt'],
# or a pattern that matches all fileids, like '[abc] /.* \.txt' (see 3.4 for information about regular expressions).

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/home/sebacastillo/Documentos/STJER/STJER - Medición Penal - OMA_vCORREGIDA.odt'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

# WordNet
# Semantically-oriented dictionary