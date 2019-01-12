import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def plot_each(data, name, plot_name):
	fig = stats.probplot(data, dist = plot_name, plot = plt)
	plt.savefig('prob2_plots/' + name + '_' + plot_name + '.png')
	plt.clf()
	

def qqplots(data, name):
	plot_each(data, name, 'norm')
	plot_each(data, name, 'cauchy')
	plot_each(data, name, 'cosine')
	plot_each(data, name, 'expon')
	plot_each(data, name, 'uniform')
	plot_each(data, name, 'laplace')
	plot_each(data, name, 'wald')
	plot_each(data, name, 'rayleigh')
	
def analyze(part):
	data = np.loadtxt('hw02_problem2' + part +'.csv')
	'''plt.hist(data)
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Problem 2 part ' + part)
	plt.savefig('prob2_plots/hist_' + part + '.png')'''
	qqplots(data, part)

	

if __name__ == '__main__':
	analyze('a')
	#analyze('b')
	#analyze('c')
	'''data = np.loadtxt('hw02_problem2c.csv')
	plt.hist(data, bins = 70)
	plt.show()'''
