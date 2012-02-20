import nltk

###
#   Simple example of tokenize and POS tag with NLTK
###
text = "All that is gold does not glitter. not all those that wander are lost."

sentences = nltk.sent_tokenize(text)

for sent in sentences:
    tokens = nltk.word_tokenize(sent)
    pos_tags = nltk.pos_tag(tokens)
    print pos_tags
