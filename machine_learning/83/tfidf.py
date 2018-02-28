import numpy as np
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
cld = {
	'misc.forsale': 'SALE',
	'rec.motorcycles': 'MOTORECYCLES',
	'rec.sport.baseball': 'BASEBALL',
	'sci.crypt': 'CRYPTONGRAPHY',
	'sci.space': 'SPACE'}
train = sd.fetch_20newsgroups(subset='train', categories=cld.keys(),
	shuffle=True, random_state=7)
train_data = train.data
train_y = train.target
categories = train.target_names
cv = ft.CountVectorizer()
train_tfmat = cv.fit_transform(train_data)
# TFIDF - Term Frequency Inverse Document Frequency
#         词频逆文档频率
tf = ft.TfidfTransformer()
train_x = tf.fit_transform(train_tfmat)
model = nb.MultinomialNB()
model.fit(train_x, train_y)
test_data=[
	'Caesar cipher is an ancient form of encryption',
	'This two-wheeler is really good on slippery roads',
	'The curveballs of right handed pitchers tend to curve to the left']
test_tfmat = cv.transform(test_data)
test_x = tf.transform(test_tfmat)
pred_test_y = model.predict(test_x)
print([cld[key] for key in np.array(categories)[pred_test_y]])