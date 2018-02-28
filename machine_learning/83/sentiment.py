import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu
pdata = []
fileids = nc.movie_reviews.fileids('pos')
for fileid in fileids:
	feature = {}
	words = nc.movie_reviews.words(fileid)
	for word in words:
		feature[word] = True
	pdata.append((feature, 'POSITIVE'))
ndata = []
fileids = nc.movie_reviews.fileids('neg')
for fileid in fileids:
	feature = {}
	words = nc.movie_reviews.words(fileid)
	for word in words:
		feature[word] = True
	ndata.append((feature, 'NEGATIVE'))
pnumb, nnumb = int(0.8 * len(pdata)), int(0.8 * len(ndata))
train_data = pdata[:pnumb] + ndata[:nnumb]
test_data = pdata[pnumb:] + ndata[nnumb:]
model = cf.NaiveBayesClassifier.train(train_data)
tops = model.most_informative_features()
for top in tops[:10]:
	print(top[0])
reviews = [
	'Is is an amazing movie.',
	'This is a dull movie. I would never recommend it to anyone.',
	'The cinematography is pretty great in this movie.',
	'The direction was terrible and the story was all over the place.']
sents, probs = [], []
for review in reviews:
	feature = {}
	words = review.split()
	for word in words:
		feature[word] = True
	pcls = model.prob_classify(feature)
	sent = pcls.max()
	prob = pcls.prob(sent)
	sents.append(sent)
	probs.append(prob)
print(sents, probs, sep='\n')

