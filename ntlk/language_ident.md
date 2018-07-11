Let's create a text string we will use for determining language

`text="That's thirty minutes away. I'll be there in ten."`{{execute}}

Now, let's tokenize the text using the WordPunct tokenizer because we would like the punctuation marks to be exluded from the words:

`from nltk import wordpunct_tokenize
wordpunct_tokenize(text)`{{execute}}

In order to build our language analyzer we will look at stop words that are present in different languages but let's see
which languages nltk supports right from the box:

`from nltk.corpus import stopwords
stopwords.fileids()`{{execute}}

Let's take a closer look at the words that are present in the English language:

`stopwords.words('english')[0:10]`{{execute}}

Using the stopwords let's build a simple language identifier that will count how many words in our sentence are found
in each of the stop word lists. i.e. let's examine each word in our sentence to see how many stop words it contains:

`from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
languages_ratios = {}
tokens = wordpunct_tokenize(text)
words = [word.lower() for word in tokens]
for language in stopwords.fileids():
    stopwords_set = set(stopwords.words(language))
    words_set = set(words)
    common_elements = words_set.intersection(stopwords_set)
    languages_ratios[language] = len(common_elements) # language "score"`{{execute}}
    
Let's see how it scored our sentence:

`language_ratios`{{execute}}

And for completeness let's just select the language with the biggest score:

`most_applicable_language = max(languages_ratios, key=languages_ratios.get)
most_applicable_language`{{execute}}
