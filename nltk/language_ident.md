Let's create a text string we will use for determining language

**ENGLISH**:
`text="Just once I'd like someone to call me 'sir' without adding 'you're making a scene.'"`{{execute}}
**FRENCH**:
`text="Après avoir rencontré Theresa May, le président américain devait rejoindre le palais de Windsor pour prendre le thé avec la reine Elizabeth II."`{{execute}}
**RUSSIAN**:
`text="Более 50 тысяч старых квартир выставили на продажу в Подмосковье"`{{execute}}

Now, let's tokenize the text using the WordPunct tokenizer because we would like the punctuation marks to be exluded from the words:

`from nltk import wordpunct_tokenize
wordpunct_tokenize(text)`{{execute}}

In order to build our language analyzer we will look at stop words that are present in different languages but let's see
which languages nltk supports right from the box:

`from nltk.corpus import stopwords
stopwords.fileids()`{{execute}}

Let's take a closer look at the words that are present in the English language:

`stopwords.words('english')[0:10]`{{execute}}

Using the stopwords let's build a simple language identifier that will count how many words in our sentence appear in
a particular language's stop word list as stop words are very common generally:

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
    
Let's see how the language detector scored our sentence:

`languages_ratios`{{execute}}

And for completeness let's just select the language with the biggest score:

`most_applicable_language = max(languages_ratios, key=languages_ratios.get)
most_applicable_language`{{execute}}
