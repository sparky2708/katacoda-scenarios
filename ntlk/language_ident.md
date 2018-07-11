
`from nltk import wordpunct_tokenize
wordpunct_tokenize("That's thirty minutes away. I'll be there in ten.")`{{execute}}

`from nltk.corpus import stopwords
stopwords.fileids()` {{execute}}
['danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'norwegian', 'portuguese', 'russian', 'spanish', 'swedish', 'turkish']

`stopwords.words('english')[0:10]`{{execute}}
['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your']

Some text goes here

`languages_ratios = {}
tokens = wordpunct_tokenize(text)
words = [word.lower() for word in tokens]
for language in stopwords.fileids():
    stopwords_set = set(stopwords.words(language))
    words_set = set(words)
    common_elements = words_set.intersection(stopwords_set)
    languages_ratios[language] = len(common_elements) # language "score"`{{execute}}

Some text

languages_ratios
{'swedish': 1, 'danish': 1, 'hungarian': 2, 'finnish': 0, 'portuguese': 0, 'german': 1, 'dutch': 1, 'french': 1, 'spanish': 0, 'norwegian': 1, 'english': 6, 'russian': 0, 'turkish': 0, 'italian': 2}
