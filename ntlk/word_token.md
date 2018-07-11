
In order to do word tokenization we have a few choices:

We can use the Penn TreeBank word tokenizer which uses regular expressions to tokenize text:

`from nltk.tokenize import TreebankWordTokenizer
treebank_word_tokenizer = TreebankWordTokenizer()
treebank_word_tokenizer.tokenize("That's all folks")`{{execute}}

or we can use the WordPuncTokenizer that splits all punctuations into separate tokens:

`from nltk.tokenize import WordPunctTokenizer
word_punct_tokenizer = WordPunctTokenizer()
word_punct_tokenizer.tokenize("That's all folks")`{{execute}}


