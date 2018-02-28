import nltk.stem as ns
words=['table', 'probably', 'wolves', 'playing', 'is', 'dog',
	   'the ', 'beeches', 'grounded', 'dreamt', 'envision']
lemmatizer = ns.WordNetLemmatizer()
for word in words:
	lemma = lemmatizer.lemmatize(word, pos='n')
	print(lemma)
print('-' * 80)
lemmatizer = ns.WordNetLemmatizer()
for word in words:
	lemma = lemmatizer.lemmatize(word, pos='v')
	print(lemma)
print('-' * 80)
