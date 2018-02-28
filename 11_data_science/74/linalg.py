import numpy as np
a = np.array([
	[1, 2, 3],
	[8, 9, 4],
	[7, 6, 5]], dtype=float)
print(a)
b = np.linalg.inv(a)
print(b)
c = np.mat(a) * np.mat(b)
print(c)
d = np.array([
	[ 1, -2,  1],
	[ 0,  2, -8],
	[-4,  5,  9]])
e = np.array([0, 8, -9])
f = np.linalg.solve(d, e)
print(f)
print(np.mat(d) * np.mat(f.reshape(-1,1)))
g = np.array([
	[3, -2],
	[1,  0]])
print(g)
h = np.linalg.eigvals(g)
print(h)
i, j = np.linalg.eig(g)
print(i, j, sep='\n')
print(np.mat(g) * np.mat(j[:,0].reshape(-1, 1)))
print(i[0] * j[:,0])
print(np.mat(g) * np.mat(j[:,1].reshape(-1, 1)))
print(i[1] * j[:,1])
k = np.array([
	[11, 12, 13, 14],
	[20, 21, 22, 15],
	[19, 18, 17, 16]], dtype=float)
l = np.linalg.pinv(k)
print(l)
print(np.mat(k) * np.mat(l))
m = np.array([
	[3, 2, 1],
	[4, 9, 8],
	[5, 6, 7]])
n = np.linalg.det(m)
print(n)
