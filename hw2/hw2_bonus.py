import numpy as np
import matplotlib.pyplot as plt

def gen_plots():
	data_a = np.loadtxt('hw02_problem2a.csv')
	data_b = np.loadtxt('hw02_problem2b.csv')
	data_c = np.loadtxt('hw02_problem2c.csv')
	# a
	sample = np.random.choice(data_a, 1000, replace = False)
	plt.hist(sample);
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Sample means for set a')
	plt.savefig('bonus_plots/a.png')
	print 'Plot A:\nMean of sample means =', np.mean(sample), ' Actual mean = ', np.mean(data_a)
	# b
	sample = np.random.choice(data_b, 1000, replace = False)
	plt.hist(sample);
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Sample means for set b')
	plt.savefig('bonus_plots/b.png')
	print 'Plot B:\nMean of sample means =', np.mean(sample), ' Actual mean = ', np.mean(data_b)
	# a
	sample = np.random.choice(data_c, 1000, replace = False)
	plt.hist(sample);
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Sample means for set c')
	plt.savefig('bonus_plots/c.png')
	print 'Plot C:\nMean of sample means =', np.mean(sample), ' Actual mean = ', np.mean(data_c)

if __name__ == '__main__':
	gen_plots()

