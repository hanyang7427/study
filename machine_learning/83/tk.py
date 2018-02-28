import nltk.tokenize as tk
doc = "Are you curious about tokenization? " \
	"Let's see how it works! " \
	"Web neek to analyze a coupl of sentences " \
	"with punctuations to see it in acction."
print('-' * 80)
tokens = tk.sent_tokenize(doc)
for token in tokens:
	print(token)
print('-' * 80)
tokens = tk.word_tokenize(doc)
for token in tokens:
	print(token)
tokenizer = tk.WordPunctTokenizer()
for token in tokens:
	print(token)
