import json
import numpy as np
with open('ratings.json', 'r') as f:
	ratings = json.loads(f.read())
users, scmat = list(ratings.keys()), []
for user1 in users:
	scrow = []
	for user2 in users:
		movies = set()
		for movie in ratings[user1]:
			if movie in ratings[user2]:
				movies.add(movie)
		if len(movies) == 0:
			score = 0
		else:
			x, y = [], []
			for movie in movies:
				x.append(ratings[user1][movie])
				y.append(ratings[user2][movie])
			x = np.array(x)
			y = np.array(y)
			score = np.corrcoef(x, y)[0, 1]
		scrow.append(score)
	scmat.append(scrow)
users = np.array(users)
scmat = np.array(scmat)
print('{:>17}'.format(''), ' '.join(
	'{:>17}'.format(user) for user in users))
for user, scrow in zip(users, scmat):
	print('{:>17}'.format(user), ' '.join(
		'{:>17.2f}'.format(score) for score in scrow))
for user in users:
	user_index = np.where(users == user)[0][0]
	sorted_indices = scmat[user_index].argsort()[::-1]
	similar_indices = sorted_indices[sorted_indices != user_index]
	similar_users = users[similar_indices]
	similar_scores = scmat[user_index, similar_indices]
	#print(user, similar_users, similar_scores)
	positive_mask = similar_scores > 0
	similar_users = similar_users[positive_mask]
	similar_scores = similar_scores[positive_mask]
	score_sums, weight_sums = {}, {}
	for similar_user, similar_score in zip(
		similar_users, similar_scores):
		for movie, score in ratings[similar_user].items():
			if movie not in ratings[user].keys():
				if movie not in score_sums.keys():
					score_sums[movie] = 0
				score_sums[movie] += score * similar_score
				if movie not in weight_sums.keys():
					weight_sums[movie] = 0
				weight_sums[movie] += similar_score
	movie_ranks = {movie: score_sum / weight_sums[movie]
		for movie, score_sum in score_sums.items()}
	sorted_indices = np.array(list(
		movie_ranks.values())).argsort()[::-1]
	recommendations = np.array(list(
		movie_ranks.keys()))[sorted_indices]
	print(user, recommendations)
