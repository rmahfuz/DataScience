from hw3_1 import *

z_alpha = 1

def getDirectConfInt(feature):  #get confidence interval
	mu = getMu(feature, 'B')
	sigma = getSigma(feature, 'B')
	length = len(data)
	first = mu - (z_alpha * sigma * pow(length, -0.5))
	last  = mu + (z_alpha * sigma * pow(length, -0.5))
	return (round(first,6), round(last,6))

def bootstrap_mu_sigma(feature, func): #return variance. func is mean or median
	coll = []  # collection
	local_data = map(lambda x: x[feature], data)
	n = len(local_data)
	for i in range(10000):
		points = np.random.choice(local_data, n, replace = True)
		coll.append(func(points))
	return (np.mean(coll), np.std(coll))

def getBootstrapConfInt(feature, func):
	mu, sigma = bootstrap_mu_sigma(feature, func)
	#print 'mu = {}, sigma = {}.Standard error for feature {} = {}'.format(mu, sigma, feature, mu/sigma)
	print 'Standard error for feature {} = {}'.format(feature, mu/sigma)
	first = mu - z_alpha*sigma
	last  = mu + z_alpha*sigma
	return (round(first, 6), round(last,6))
		
def mean_bootstrap():
	#print 'Confidence intervals for mean:'
	for i in range(1,9):
		direct = getDirectConfInt(i)
		boot = getBootstrapConfInt(i, np.mean)
		diff = abs(direct[0] - boot[0]) + abs(direct[1] - boot[1])
		#print 'For feature {}, diff = ({}, {})'.format(i, direct[0] - boot[0], direct[1] - boot[1])
		#print 'For feature {}, Direct ConfInt : {}, Bootstrapped ConfInt : {}, difference : ({}, {})'.format(i, direct, boot, direct[0] - boot[0], direct[1] - boot[1])
		#print 'For feature {}, Direct ConfInt : {}, Bootstrapped ConfInt : {}, difference : {}'.format(i, direct, boot, diff)
		print 'For feature {}, Direct ConfInt : {}, Bootstrapped ConfInt : {}'.format(i, direct, boot)

def median_bootstrap():
	print 'Confidence intervals for median:'
	for i in range(1,9):
		boot = getBootstrapConfInt(i, np.median)
		#print 'For feature {}, bootstrapped confidence interval: {}'.format(i, boot)


def main():
	#mean_bootstrap()
	median_bootstrap()

if __name__ == '__main__':
	main()
