import scipy.stats as stats
from csv_reader import readData
import matplotlib.pyplot as plt

def part_1(data):
	score, color1, color2 = zip(*data)
	plt.hist(score)
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Scores')
	plt.savefig('prob3_plots/part1.png')

def plot_color(data, color_reqd, number):
	color_plt = 'gray' if color_reqd == 'white' else color_reqd
	filtered = filter(lambda x: x[number] == color_reqd, data)
	plt.hist(zip(*filtered)[0], color = color_plt)
	plt.xlabel('bins'); plt.ylabel('frequencies'); plt.title('Filtered ' + color_reqd)
	plt.savefig('prob3_plots/filtered_' + color_reqd + '.png')
	#plt.show()
	plt.clf()

def plot_sum_colors(data, color1_reqd, color2_reqd, number1, number2):
	color1_plt = 'gray' if color1_reqd == 'white' else color1_reqd
	color2_plt = 'gray' if color2_reqd == 'white' else color2_reqd
	filtered1 = filter(lambda x: x[number1] == color1_reqd, data)
	filtered2 = filter(lambda x: x[number2] == color2_reqd, data)
	

def part_2(data):
	plot_color(data, 'red', 1)
	plot_color(data, 'green', 1)
	plot_color(data, 'black', 2)
	plot_color(data, 'white', 2)
	

if __name__ == '__main__':
	data = readData('hw02_problem3.csv')
	#part_1(data)
	#part_2(data)
	filtered_green = filter(lambda x: x[1] == 'green', data)
	stats.probplot(zip(*filtered_green)[0], dist = 'norm', plot = plt)
	plt.savefig('prob3_plots/green_normal.png')
	plt.clf()
