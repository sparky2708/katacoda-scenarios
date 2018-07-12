
In order to do word tokenization we have a few choices of tokenizer.
Let's set a sentence we will try to tokenize:

`sent = "NATO countries did not commit to Trump's call for 4% spending, sources says"`{{execute}}

We can use the Penn TreeBank word tokenizer which uses regular expressions to tokenize text:

`from nltk.tokenize import TreebankWordTokenizer
sent = 
treebank_word_tokenizer = TreebankWordTokenizer()
treebank_word_tokenizer.tokenize(sent)`{{execute}}

or we can use the WordPuncTokenizer that splits all punctuations into separate tokens:

`from nltk.tokenize import WordPunctTokenizer
word_punct_tokenizer = WordPunctTokenizer()
word_punct_tokenizer.tokenize(sent)`{{execute}}

There is also a tokenizer specialized to parsing Tweets. 
Let's pick a sample tweet:

`tweet = "@remy: This is waaaaayyyy too much for you!!!!!! :-P"`{{execute}}

and let's try to run the tweet through the tweet tokenizer
`from nltk.tokenize import TweetTokenizer
tweet_tokenizer = TweetTokenizer()
tweet_tokenizer.tokenize(tweet)`{{execute}}
