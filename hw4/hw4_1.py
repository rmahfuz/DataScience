import numpy as np
from matplotlib import pyplot as plt
from csv_reader import readData

def getTraining(data):
	return filter (lambda x: x[10] == 'T', data)

def getTesting(data):
	return filter (lambda x: x[10] == 'F', data)

def getLen(data, t_or_f):
	return len(getTraining(data)) if t_or_f == 'T' else len(getTesting(data))

def preprocess(data):
	new_data = []
	for item in data:
		item2 = []
		for point in item[0:10]:
			item2.append(float(point))
		item2.append(item[10])
		new_data.append(list(item2))
	#new_data = np.matrix(new_data)
	# make avg of columns 1-9 (y and all columns in X) in data 0
	for i in range(1, 10):
		obs = []
		for line in new_data:
			obs.append(line[i])
		avg = np.mean(obs)
		for line in new_data:
			line[i] = line[i] - avg
	# make sum of squares of columns 1-8 (each column in X) in data 1
	for i in range(1, 9):
		obs = [line[i] for line in new_data]
		ss = 0
		for item in obs:
			ss += (item*item)
		ss = pow(ss, 0.5)
		for line in new_data:
			line[i] = line[i] / ss
	return new_data
		
def verify_preprocess(p_data):
	for i in range(1,10):
		obs = [p[i] for p in p_data]
		print np.mean(obs)
	for i in range(1, 9):
		ss = 0
		for item in p_data:
			ss += pow(item[i], 2)
		print(ss)
def find_beta(data, lambdaa):
	x_idx = []; y_idx = []
	for i in range(np.shape(data)[0]):
		x_idx.append(range((11*i)+1, (11*i)+9))
		y_idx.append(11*i+9)
	x = np.matrix(data = np.take(data, x_idx), dtype = np.float32)
	y = np.matrix(data = np.take(data, y_idx), dtype = np.float32)
	y = y.T
	first_1 = x.T*x
	first_2 = np.identity(np.shape(x)[1])*lambdaa
	first = (first_1 + first_2).I
	second = first * x.T
	return second * y

def least_sq(data):
	betas = []
	lambdas = np.logspace(-10, 10, 1000)
	for lambdaa in lambdas:
		betas.append(find_beta(data, lambdaa))
	for i in range(len(betas)):
		betas[i] = betas[i].tolist()
	fig = plt.figure(); ax = plt.subplot(111)
	with open('hw04.csv', 'r') as to_read:
		lines = to_read.readlines()
		name = lines[0].split(',')
	print(name)
	for i in range(len(betas[0])):
		feature = map(lambda x: x[i], betas)
		ax.semilogx(lambdas, feature, label = name[i+1])
	plt.xlabel('log(lambda)'); plt.ylabel('beta'); plt.title('Trajectory of beta as lambda changes')
	ax.legend()
	plt.show()
	
def find_mse(data, lambdaa, beta):
	x_idx = []; y_idx = []
	for i in range(np.shape(data)[0]):
		x_idx.append(range((11*i)+1, (11*i)+9))
		y_idx.append((11*i)+9)
	x = np.matrix(data = np.take(data, x_idx), dtype = np.float32)
	y = np.matrix(data = np.take(data, y_idx), dtype = np.float32)
	y = y.T
	#print(x[:3])
	#print('')
	ans = y-(x*beta)
	ans = ans.tolist()
	ss = 0.0
	print 'lambda = {}, beta = \n{},\n printing sum of square after each addition:'.format(lambdaa, beta)
	for item in ans:
		ss += pow(np.float(item[0]), 2)
		print(ss)
	print('')
	return ss/len(ans)
	
def cross_validate(data):
	mses = []; lambdas = np.logspace(-10, 10, 1000)
	'''for lambdaa in lambdas:
		beta = np.matrix(find_beta(getTraining(data), lambdaa) )
		mses.append(find_mse(getTesting(data), lambdaa, beta))'''
	beta = np.matrix(find_beta(getTraining(data), lambdas[0]) )
	print(beta)
	#print(mses)
	#plt.semilogx(lambdas, mses, xlabel = 'lambda', ylabel = 'mean squared error', title = 'Mean squared error as a function of lambda')
	'''
	plt.semilogx(lambdas, mses)
	plt.xlabel('Lambda'); plt.ylabel('Mean squared error'); plt.title('Mean squared error as a function of lambda')
	plt.show()'''
	# plot mses vs. lambdas
	
	

	
	

if __name__ == '__main__':
	data = readData('hw04.csv')
	p_data = preprocess(data)
	#verify_preprocess(p_data)
	#least_sq(getTraining(p_data))
	cross_validate(p_data)
	'''
	lambdaa = 1
	find_beta(lambdaa)
	beta_arr = []
	lambdas = np.logspace(-10, 10, 1000)
	for i in lambdas:
		beta_arr.append(find_beta(i))
	cross_validate()
	#plot beta_arrr vs. lambdas
	'''
	
