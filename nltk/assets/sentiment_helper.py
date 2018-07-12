from nltk.corpus import stopwords
import string

def clean_all_words(all_words):
    all_words_clean = []
    stopwords_english = stopwords.words('english')
    
    for word in all_words:
        if word not in stopwords_english and word not in string.punctuation:
            all_words_clean.append(word)
 
    return all_words_clean
