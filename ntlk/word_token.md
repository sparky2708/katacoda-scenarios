
In order to do word tokenization we have a few choices:

We can use the PunktWordTokenizer which splits on punctuation but keeps it with the word:

`from nltk.tokenize import PunktWordTokenizer
punkt_word_tokenizer = PunktWordTokenizer()
punkt_word_tokenizer.tokenize("That's all folks")`{{execute}}

or we can use the WordPuncTokenizer that splits all punctuations into separate tokens:

`from nltk.tokenize import WordPunctTokenizer
word_punct_tokenizer = WordPunctTokenizer()
word_punct_tokenizer.tokenize("That's all folks")`{{execute}}

or we can use the Penn TreeBank word tokenizer which uses regular expressions to tokenize text:

`from nltk.tokenize import TreebankWordTokenizer
treebank_word_tokenizer = TreebankWordTokenizer()
treebank_word_tokenizer.tokenize("That's all folks")`{{execute}}

