
Create a list of words that are found in all the reviews:

`all_words = data_reader.get_all_words(reviews)
print (all_words[:10])`{{execute}}

Let's look at the frequency distribution of all the words:

`from nltk import FreqDist
all_words_freq = FreqDist(all_words)
print (all_words_freq)
print (all_words_freq.most_common(10))`{{execute}}
 
Since our most frequent words are not very helpful we should clean the data a bit
and remove stopwords and puctuation

`all_cleaned_words = data_reader.clean_all_words(all_words)`{{execute}}

Let's look at the frequency distribution again:

`from nltk import FreqDist
all_cleaned_words_freq = FreqDist(all_cleaned_words)
print (all_cleaned_words_freq)
print (all_cleaned_words_freq.most_common(10))`{{execute}}
 
 
