
NLTK implements a number stemmers. The popular "Porter Stemmer" which we will examine below as well as other stemmers including the "Lancaster Stemmer" and the "Snowball Stemmer". 

**Let's take a look at the Porter Stemmer**:

`from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()`{{execute}}

Let's see how the porter stemmer would stem:

`porter_stemmer.stem("run")
porter_stemmer.stem("ran")
porter_stemmer.stem("running")
porter_stemmer.stem("geese")
porter_stemmer.stem("goose")`{{execute}}

**NLTK also implements a Lemmatizer based on the WordNet searchable database:**

`from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()`{{execute}}

Let's see how the lemmatizer deals with the same cases:

`from nltk.corpus import wordnet
wordnet_lemmatizer.lemmatize("run", wordnet.VERB)
wordnet_lemmatizer.lemmatize("ran", wordnet.VERB)
wordnet_lemmatizer.lemmatize("running", wordnet.VERB)
wordnet_lemmatizer.lemmatize("geese")
wordnet_lemmatizer.lemmatize("goose")`{{execute}}

