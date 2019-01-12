import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('hw02_problem1.csv')

def gen_plots():
	# 50 data points
	sample = np.random.choice(data, 50, replace = False)
	plt.hist(sample);
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Attempt 3 of problem 1 with 50 points')
	plt.savefig('prob1_50points_attempt3.png')

	# 200 data points
	sample = np.random.choice(data, 200, replace = False)
	plt.hist(sample);
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Attempt 3 of problem 1 with 200 points')
	plt.savefig('prob1_200points_attempt3.png')

	# 1000 data points
	sample = np.random.choice(data, 1000, replace = False)
	plt.hist(sample);
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Attempt 3 of problem 1 with 1000 points')
	plt.savefig('prob1_1000points_attempt3.png')

	# 5000 data points
	sample = np.random.choice(data, 5000, replace = False)
	plt.hist(sample);
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Attempt 3 of problem 1 with 5000 points')
	plt.savefig('prob1_5000points_attempt3.png')

	# 10000 data points
	plt.hist(data)
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Attempt 3 of problem 1 with all 10000 points')
	plt.savefig('prob1_10000points_attempt3.png')

def sampleMean(data_set, k):
	sample = np.random.choice(data_set, k, replace = False)
	return np.mean(sample)

def part_5():
	means = []
	for i in range(10000):
		means.append(sampleMean(data, 100))
	plt.hist(means)
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('10000 Means of samples of size 100')
	plt.savefig('prob1_10000MeansOfSamples.png')
	print('Mean of the means of samples = ', np.mean(means))
	print('Variance of the means of samples = ', np.var(means))
	print('Mean of the entire data set = ', np.mean(data))

if __name__ == '__main__':
	#gen_plots()
	part_5()

