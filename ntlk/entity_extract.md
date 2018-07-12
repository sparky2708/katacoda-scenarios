
out-of-the-box, NLTK provides a classifier that has been trained to recognize named entities.

Let's take a look at the following sentence:
`sentence = "Anderson says the Baillie Gifford firm still supports Elon Musk's efforts in the United States to promote clean energy but would like peace and execution at this stage"`{{execute}}

Let's see if NLTK's pre-trained model will be able to decipher the entities in this sentence:
`import nltk
word_list = nltk.word_tokenize(sentence )
pos_tagged_tree = nltk.pos_tag(word_list)
entity_tree =  nltk.ne_chunk(pos_tagged_tree, binary=False)`{{execute}}
