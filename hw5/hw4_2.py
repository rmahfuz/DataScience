import numpy as np
from matplotlib.pyplot import imread, imsave
from pprint import pprint as pp
from helper import preprocess_data

train_cat = []; train_grass = []
with open('hw5_cat.txt', 'r') as cat:
	for line in cat.readlines():
		train_cat.append(map(lambda x: np.float64(x), line.split(',')))
train_cat = np.transpose(train_cat)

with open('hw5_grass.txt', 'r') as grass:
	for line in grass.readlines():
		train_grass.append(map(lambda x: np.float64(x), line.split(',')))
train_grass = np.transpose(train_grass)

Y = np.transpose(preprocess_data(imread('cat_grass.png')))
output = []; idx = 0

for pixel in Y:  #runs 187500 times
	dist = []
	for feature in train_cat:   #runs 500 times
		diff = pixel-feature    #list of 64 items
		dist.append((np.dot(diff, diff), 'C'))  #appends a tuple (distance, 'C')
	for feature in train_grass: #runs 500 times
		diff = pixel-feature
		dist.append((np.dot(diff, diff), 'G'))
	cnt = 0
	for i in np.argsort(map(lambda x: x[0], dist))[:5]:
		if dist[i][1] == 'C':
			cnt += 1
		else:
			cnt -= 1
	output.append(int(cnt > 0))
	idx +=1
	if idx%1000 == 0:
		print idx

output = np.reshape(output, (375, 500))
print(output.shape)
imsave('result_knn.png', output)
