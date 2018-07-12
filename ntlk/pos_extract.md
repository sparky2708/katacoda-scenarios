
NLTK has a trained part of speech model that can be used:

`sent = "Geoff Boeing, a postdoc in the Urban Analytics Lab at the University California, Berkeley, has published a blog post that offers a fascinating look at the street orientation of major cities in the USA and around the world."`{{execute}}

We can invoke the Parts-Of-Speech tagger as follows:

`import nltk
word_list = nltk.word_tokenize(sent)
pos_tagged_tree = nltk.pos_tag(word_list)
print(pos_tagged_tree)`{{execute}}
