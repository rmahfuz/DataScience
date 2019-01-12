import numpy as np

ratio = 0.9; train_ratio = int(ratio*50)
feature_name = ['annual police funding in $/resident', '% of people 25 years+ with 4 yrs. of high school', '% of 16 to 19 year-olds not in highschool and not highschool graduates', '% of 18 to 24 year-olds in college', '% of people 25 years+ with at least 4 years of college']
train_x = []; test_x = []; train_total = []; test_total = []; train_violent = []; test_violent = []
with open('data.txt', 'r') as to_read:
	did_read = to_read.readlines()
	for line in did_read[:int(ratio*50)]:
		train_x.append(map(lambda x: np.float64(x), line.split()[2:]))
		train_total.append(np.float64(line.split()[0]))
		train_violent.append(np.float64(line.split()[1]))
	for line in did_read[int(ratio*50):]:
		test_x.append(map(lambda x: np.float64(x), line.split()[2:]))
		test_total.append(np.float64(line.split()[0]))
		test_violent.append(np.float64(line.split()[1]))

#print("test_total:"); print(test_total); print(type(test_total))
train_x = np.matrix([d for d in train_x], dtype = float)
test_x = np.matrix([d for d in test_x], dtype = float)
train_total = np.matrix([d for d in train_total], dtype = float)
train_violent = np.matrix([d for d in train_violent], dtype = float)
test_total = np.matrix([d for d in test_total], dtype = float)
test_violent = np.matrix([d for d in test_violent], dtype = float)
#train_x = np.matrix(train_x)
#print(train_x_temp == train_x)
#test_x = np.matrix(test_x)
#train_total = np.matrix(train_total)
#test_total = np.matrix(test_total)
#train_violent = np.matrix(train_violent)
#test_violent = np.matrix(test_violent)
#print("test_total:"); print(test_total); print(type(test_total))


train_x -= np.mean(train_x, 0)
train_x /= np.sqrt(np.sum(np.square(train_x), 0))
test_x -= np.mean(test_x, 0)
test_x /= np.sqrt(np.sum(np.square(test_x), 0))

train_total -= np.mean(train_total)
train_violent -= np.mean(train_violent)
test_total -= np.mean(test_total)
test_violent -= np.mean(test_violent)

#-------------------------------------------------------------------------------------------------------------
def calc_beta(test_given, train_given):
	beta = np.zeros((1000, 5, 1), dtype = float)
	#y = np.zeros((1000, len(test_given), 1), dtype = float)
	y = []
	mse = np.zeros((1000, 1), dtype = float)
	lambdas = np.logspace(-10, 1, 1000)
	#print('train length = {}, test length = {}'.format(len(train_x), len(test_x)))

	for i in range(len(lambdas)):
		beta[i] = (train_x.T*train_x + lambdas[i]*np.identity(5)).I*train_x.T*train_given.T
		#print('beta[i] = ', beta[i].shape, type(beta[i]))
		#print('test_given.shape = ',test_given.shape, type(test_given))
		#print('test_x.shape = ',test_x.shape, type(test_x))
		#y[i] = test_given*beta[i]
		#y[i] = test_x*beta[i]
		to_app = []
		for j in range(5):
			tmp = 0
			for k in range(5):
				tmp += (float(test_x.item(j,k)) * float(beta[i][k]))
			to_app.append(tmp)
		y.append(to_app)
		#to_app = map(lambda x:[x], to_app)
		#print('to_app:', to_app, type(to_app))
		#y[i] = np.matrix(to_app)
		#print(y[i])	
		#print('np.square(y[i].shape: '),;print(np.square(y[i]).shape)
		#print('test_given.T.shape'),; print(test_given.T.shape)
		acc = []
		for j in range(5):
			acc.append(y[i][j] - test_given.item(j))
		mse[i]= sum(np.square(acc))
		#mse[i] = sum(np.square(y[i] - test_given.T))/len(test_given)

	idx = np.argmin(mse)
	#print(mse)
	#print 'mse: ',; print(mse[idx]); print 'lambda',; print(lambdas[idx])
	return beta[idx]
#-------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	beta = calc_beta(test_total, train_total)
	#print('test_x: '); print(test_x); print('')
	#print('beta: '); print(beta); print('')
	#print('test_total: '); print(test_total); print('')
	err = 0; abs_err = 0
	print('Total overall reported crime rate per 1 million residents predictions:')
	for i in range(len(np.array(test_total)[0])):
		predicted = 0
		for j in range(5):
			predicted += (beta[j] * test_x.item(i,j))
		err += (np.array(test_total)[0][i] - predicted[0])
		abs_err += abs(np.array(test_total)[0][i] - predicted[0])
		print('actual value: {}, predicted value: {}'.format(np.array(test_total)[0][i], predicted[0]))
	print('Total signed error: {}, absolute error per prediction: {}'.format(err, abs_err/5))
	print 'Prediction coefficients: '
	for i in range(5):
		print('{}) {}: {}'.format(i+1, feature_name[i], beta[i][0]))
	print('----------------------------------------------------------------------------------------------------')	
	beta = calc_beta(test_violent, train_violent)
	err = 0; abs_err = 0
	print('Reported violent crime rate per 100,000 residents predictions:')
	for i in range(len(np.array(test_total)[0])):
		predicted = 0
		for j in range(5):
			predicted += (beta[j] * test_x.item(i,j))
		err += (np.array(test_violent)[0][i] - predicted[0])
		abs_err += abs(np.array(test_violent)[0][i] - predicted[0])
		print('actual value: {}, predicted value: {}'.format(np.array(test_violent)[0][i], predicted[0]))
	print('Total signed error: {}, absolute error per prediction: {}'.format(err, abs_err/5))
	print 'Prediction coefficients: '
	for i in range(5):
		print('{}) {}: {}'.format(i+1, feature_name[i], beta[i][0]))
