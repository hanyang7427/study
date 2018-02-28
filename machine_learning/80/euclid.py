import json
import numpy as np
with open('ratings.json', 'r') as f:
	ratings = json.loads(f.read())
users, esmat = list(ratings.keys()), []
for user1 in users:
	esrow = []
	for user2 in users:
		movies = set()
		for movie in ratings[user1]:
			if movie in ratings[user2]:
				movies.add(movie)
		if len(movies) == 0:
			es = 0
		else:
			diffs = []
			for movie in movies:
				diffs.append(np.square(ratings[user1][movie] - \
					ratings[user2][movie]))
			diffs = np.array(diffs)
			es = 1 / (1 + np.sqrt(diffs.sum()))
		esrow.append(es)
	esmat.append(esrow)
print(esmat)
