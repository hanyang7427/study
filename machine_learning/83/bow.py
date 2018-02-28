import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
doc = 'The brown dog is running. ' \
	'The black dog is in the black room. ' \
	'Running in the room is forbidden.'
print(doc)
sentences = tk.sent_tokenize(doc)
cv = ft.CountVectorizer()
tfmat = cv.fit_transform(sentences).toarray()
words = cv.get_feature_names()
print(words, tfmat)