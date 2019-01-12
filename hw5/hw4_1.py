import numpy as np
from matplotlib.pyplot import imread, imsave
from helper import preprocess_data

train_cat = []; train_grass = []
with open('hw5_cat.txt', 'r') as cat:
	for line in cat.readlines():
		train_cat.append(map(lambda x: np.float64(x), line.split(',')))
mean_cat = np.mean(train_cat, 1)
cov_cat = np.cov(train_cat)

with open('hw5_grass.txt', 'r') as grass:
	for line in grass.readlines():
		train_grass.append(map(lambda x: np.float64(x), line.split(',')))
mean_grass = np.mean(train_grass, 1)
cov_grass = np.cov(train_grass)

Y = np.transpose(preprocess_data(imread('cat_grass.png')))
output = []

term1 = -1*(np.shape(Y[0])[0]/2) * np.log10(2*np.pi)
print(np.shape(Y[0])[0])
term2_cat   = -0.5* np.log10(np.linalg.det(cov_cat  )); term12_cat   = term1 + term2_cat
term2_grass = -0.5* np.log10(np.linalg.det(cov_grass)); term12_grass = term1 + term2_grass
cov_inv_cat   = np.linalg.inv(cov_cat  )
cov_inv_grass = np.linalg.inv(cov_grass)

for pixel in Y:
	term3_cat   = np.matmul(np.transpose(pixel - mean_cat  ), cov_inv_cat  )
	term3_cat   = -0.5 * np.matmul(term3_cat  , pixel - mean_cat  )
	term3_grass = np.matmul(np.transpose(pixel - mean_grass), cov_inv_grass)
	term3_grass = -0.5 * np.matmul(term3_grass, pixel - mean_grass)
	if (term12_cat + term3_cat >= term12_grass + term3_grass):
		output.append(1)
	else:
		output.append(0)

output = np.reshape(output, (375, 500))
imsave('result_bayes.png', output)
