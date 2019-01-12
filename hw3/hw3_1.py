from pprint import pprint as pp
from csv_reader import readData
import numpy as np
from scipy.stats import norm

data = readData('hw03.csv')
alpha = 0.05

def getTraining():
	return filter (lambda x: x[10] == 'T', data)

def getTesting():
	return filter (lambda x: x[10] == 'F', data)

def getLen(t_or_f):
	return len(getTraining()) if t_or_f == 'T' else len(getTesting())
	
def getMu(feature, t_or_f): #'B' is for both
	if t_or_f == 'T':
		points = map(lambda x: x[feature], getTraining())
	if t_or_f == 'F':
		points = map(lambda x: x[feature], getTesting())
	if t_or_f == 'B':
		points = map(lambda x: x[feature], data)
	return np.mean(points)

def getSigma(feature, t_or_f):  # feature should be between 1 and 9, inclusive
	if t_or_f == 'T':
		points = map(lambda x: x[feature], getTraining())
	if t_or_f == 'F':
		points = map(lambda x: x[feature], getTesting())
	if t_or_f == 'B':
		points = map(lambda x: x[feature], data)
	return np.std(points)

def compareMean(feature):
	term1 = float(pow(getSigma(feature, 'T'), 2))/getLen('T')
	term2 = float(pow(getSigma(feature, 'F'), 2))/getLen('F')
	#print 'sigma0 = {}'.format(getSigma(feature, 'T'))
	#print 'sigma1 = {}'.format(getSigma(feature, 'F'))
	sigma_hat = pow(term1 + term2, 0.5)
	#print 'sigma_hat = {}'.format(sigma_hat)
	z = float(getMu(feature, 'T') - getMu(feature, 'F')) / sigma_hat
	z_alpha = norm.ppf(alpha, 0, 1)
	return (z, z_alpha)

def main():
	for i in range(1, 9):
		ans = compareMean(i)
		#print '|z|-|z_apha| for feature {} = {}'.format(i, abs(ans[0]) - abs(ans[1]))
		print 'z{} = {}'.format(i, ans[0])

if __name__ == '__main__':
	main()

