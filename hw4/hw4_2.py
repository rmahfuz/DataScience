import numpy as np
from matplotlib import pyplot as plt
from pprint import pprint as pp

with open('google_stock_train.txt', 'r') as fil:
	google_data = map(lambda x: np.float(x.strip()), fil.readlines())
with open('nvs_stock_train.txt', 'r') as fil:
	nvs_data = map(lambda x: np.float(x.strip()), fil.readlines())

def get_beta(data):
	k = 25
	y = np.matrix(data = data[k:], dtype = np.float); y = y.T
	#print(y); print(y.shape)
	x = []
	for i in range(k, len(data)):
		if i == k:
			to_app = data[i-1::-1]
		else:
			to_app = data[i-1:i-k-1:-1]
		#print('{}: {}  i = {}, len(app) = {}'.format(i-1,i-26, i, len(to_app)))
		x.append(to_app)
	x = np.matrix(np.array(x))
	#print(x.shape)
	return ((x.T*x).I)*x.T*y

def predict(data, beta):
	#construct x:
	k = 25; x = []
	for i in range(k, len(data)):
		if i == k:
			to_app = data[i-1::-1]
		else:
			to_app = data[i-1:i-k-1:-1]
		#print('{}: {}  i = {}, len(app) = {}'.format(i-1,i-26, i, len(to_app)))
		x.append(to_app)
	x = np.matrix(data = x, dtype = np.float32); ans = []
	p = len(data);#200 
	for i in range(30):
		new = 0
		for j in range(1, k+1):
			#print('{}, {}'.format(p+i-j, j-1))
			new += data[p+i-j]*beta[j-1]
		data.append(new); ans.append(new)
		#changing x and beta:
		x = x.tolist()
		x = x[1:]
		to_app = new.tolist()[0] #this is a list
		to_app.extend(x[-1][:k-1])
		x.append(to_app)
		x = np.matrix(data = x, dtype = np.float32)
		#print(x.shape)
		y = data[-1:-176:-1][::-1];
		#print('type(y) = {}'.format(type(y)))
		y = np.matrix(data= y, dtype = np.float32); y = y.T
		#beta = (x.T*x).I*x.T*y
		beta = (x.T*x).I
		beta = beta*x.T
		beta = beta*y
		
		#print('y.shape = {}, x.shape = {}, beta.shape = {}'.format(y.shape, x.shape, beta.shape))
	return ans




if __name__ == '__main__':
	google_beta = get_beta(google_data)
	google_prediction = map(lambda x: x.tolist()[0][0], predict(google_data, google_beta))
	print('google prediction:'); pp(list(enumerate(google_prediction)))
	plt.plot(range(200), google_data[:200], 'b'); 
	plt.plot(range(200, 230), google_prediction, 'r'); 
	plt.xlabel('Day number'); plt.ylabel('Stock value'); plt.title('Google stock prediction'); plt.show()
	#-----------------------------------------------------------------------------------------------
	'''nvs_beta = get_beta(nvs_data)
	nvs_prediction = map(lambda x: x.tolist()[0][0], predict(nvs_data, nvs_beta))
	print('nvs prediction:'); pp(list(enumerate(nvs_prediction)))
	plt.plot(range(200), nvs_data[:200], 'b'); 
	plt.plot(range(200, 230), nvs_prediction, 'r'); 
	plt.xlabel('Day number'); plt.ylabel('Stock value'); plt.title('NVS stock prediction'); plt.show()'''
