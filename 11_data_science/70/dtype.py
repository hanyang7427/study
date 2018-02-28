import numpy as np
a = np.array([(
	(( 1, 2, 3, 4), ( 5, 6, 7, 8), ( 9,10,11,12)),
	((13,14,15,16), (17,18,19,20), (21,22,23,24))
	)], dtype='>(2,3)4i4')
print(a)
b = np.array(['Unicode String'], dtype=(np.str_, 14))
print(b)
c = np.array([(.1,.2,.3)], dtype=(np.float32, 3))
print(c)
d = np.array([('Unicode String', (.1,.2,.3),
	((1,2,3),(4,5,6)))], dtype='U14,3f4,(2,3)u8')
print(d)
print(d[0]['f0'])
print(d[0]['f1'])
print(d[0]['f2'])
print(d[0]['f2'][1][1])
e = np.array([('Unicode String', (.1,.2,.3),
	((1,2,3),(4,5,6)))], dtype=[('st',np.str_,14),
	('vt',np.float32,3),('mt',np.uint64,(2,3))])
print(e)
print(e[0]['st'])
print(e[0]['vt'])
print(e[0]['mt'])
print(e[0]['mt'][1][1])
f=np.array([0x1234], dtype=('u2',
	[('low',np.uint8), ('high',np.uint8)]))
print('{:#2x}'.format(f['low'][0]),
	'{:#2x}'.format(f['high'][0]))
g=np.array(['你好，派森！'], dtype=('U6',
	[('codes',np.uint32,6)]))
print(g[0])
print('{:08x}'.format(g['codes'][0][0]))
print('{:08x}'.format(g['codes'][0][1]))
print('{:08x}'.format(g['codes'][0][2]))
print('{:08x}'.format(g['codes'][0][3]))
print('{:08x}'.format(g['codes'][0][4]))
print('{:08x}'.format(g['codes'][0][5]))


