text = "my name is Peter , and i can see with my eyes"
import nltk
from nltk.tokenize import word_tokenize


words = word_tokenize(text)
tagged_words = nltk.pos_tag(words, tagset='universal')

for t in tagged_words:
	print(t)