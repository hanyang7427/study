import numpy as np
import sklearn.preprocessing as sp
raw_labels = np.array(['audi', 'ford', 'audi', 'toyota',
	'ford', 'bmw', 'toyota', 'ford', 'audi'])
print(raw_labels)
codec = sp.LabelEncoder()
enc_labels = codec.fit_transform(raw_labels)
print(enc_labels)
dec_labels = codec.inverse_transform(enc_labels)
print(dec_labels)