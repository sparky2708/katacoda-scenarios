
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

NLTK also implements a Lemmatizer based on the WordNet searchable database:

`from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()`{{execute}}

**Let's see how the lemmatizer deals with the same cases:**

`wordnet_lemmatizer.lemmatize("run")
wordnet_lemmatizer.lemmatize("ran")
wordnet_lemmatizer.lemmatize("running")
wordnet_lemmatizer.lemmatize("geese")
wordnet_lemmatizer.lemmatize("goose")`{{execute}}

**Let's observe how a combination of these approaches would work:**

`porter_stemmer.stem(wordnet_lemmatizer.lemmatize("run"))
porter_stemmer.stem(wordnet_lemmatizer.lemmatize("ran"))
porter_stemmer.stem(wordnet_lemmatizer.lemmatize("running"))
porter_stemmer.stem(wordnet_lemmatizer.lemmatize("geese"))
porter_stemmer.stem(wordnet_lemmatizer.lemmatize("goose"))`{{execute}}
