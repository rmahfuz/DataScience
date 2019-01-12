import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.pyplot as plt
from helper import plotHisto
#from pprint import pprint as pp

#INPUTS
#data: list of data points
#numbins: number of bins in the output histogram
#minimum: the minimum value of the histogram range
#maximum: the maximum value of the histogram range
#
#RETURNS:
#histo: a list of length numbins, with each entry containing the number of data points in the corresponding histogram bin

"""def inRange(num, low, high):
	return num >= low and num < high"""

def buildHisto (data, numbins, minimum, maximum):

# 1. FILL IN

	mrange = maximum - minimum
	binsize = mrange / numbins

	starts = [binsize*i + minimum for i in range(numbins)]
	#print(starts)
	#histo = [len(filter(inRange, data, i , i+binsize)) for i in starts]
	histo = []
	#big_bag = []
	for i in range(numbins):
		cnt = 0
		#bag = []
		for point in data:
			if point >= starts[i] and point < starts[i] + binsize:
				cnt += 1
				#bag.append(point)
			else:
				if i == numbins-1 and point == starts[i] + binsize:
					cnt += 1
					#bag.append(point)
		histo.append(cnt)
		#big_bag.append(bag)
		
	"""for i in range(len(big_bag)):
		bag = big_bag[i]
		print(starts[i], min(bag), ", ", max(bag))"""
	#print(big_bag)
	return histo
	

data = np.loadtxt('math_scores.txt')

def sum_squares(li):
	to_ret = 0
	for item in li:
		to_ret += item*item
	return to_ret	

# 2. Build and plot histogram with 10 bins
minimum = 0.0
maximum = 100.0
histo = buildHisto(data, 10, 0.0, 100.0)
print("10 bins: ", sum_squares(histo))
#print(histo)
#plotHisto(histo, 'hist1.png', minimum, maximum)

# 3. Build and plot histogram with 200 bins
histo = buildHisto(data, 200, 0.0, 100.0)
print("200 bins: ", sum_squares(histo))
#plotHisto(histo, 'hist2.png', minimum, maximum)

# 4.0 Build and plot histogram with 100 bins
histo = buildHisto(data, 100, 0.0, 100.0)
print("100 bins: ", sum_squares(histo))
#plotHisto(histo, 'hist3.png', minimum, maximum)

# 4.1 Build and plot histogram with 50 bins
histo = buildHisto(data, 50, 0.0, 100.0)
print("50 bins: ", sum_squares(histo))

# 4.2 Build and plot histogram with 150 bins
histo = buildHisto(data, 150, 0.0, 100.0)
print("150 bins: ", sum_squares(histo))
#plotHisto(histo, 'hist3.png', minimum, maximum)
"""
# 3. Build and plot histogram with 200 bins
histo = buildHisto(data, 130, 0.0, 100.0)
print("130 bins: ", sum_squares(histo))

# 3. Build and plot histogram with 200 bins
histo = buildHisto(data, 160, 0.0, 100.0)
print("160 bins: ", sum_squares(histo))

# 3. Build and plot histogram with 200 bins
histo = buildHisto(data, 157, 0.0, 100.0)
print("157 bins: ", sum_squares(histo))

histo = buildHisto(data, 158, 0.0, 100.0)
print("158 bins: ", sum_squares(histo))



new_data = np.random.choice(data, size = len(data)/10, replace = False)
# new_data with 150 bins:
histo = buildHisto(new_data, 150, 0.0, 100.0)
#plotHisto(histo, 'hist4.png', minimum, maximum)
# new_data with 1000 bins:
histo = buildHisto(new_data, 1000, 0.0, 100.0)
#plotHisto(histo, 'hist5.png', minimum, maximum)
"""
# Cross-validatio code:
j = []
n = 50000.0 #number of data points
for m in range(498, 502): #m is number of bins
	histo = buildHisto(data, m, 0.0, 100.0)
	h = n/m
	j.append((2.0/49999.0*h) - ((n+1)/((n-1)*h))*(reduce(lambda x,y: x+y, map(lambda x: x*x, histo))))

print('minimum score: ', min(j), 'optimal number of bins: ', 498 + j.index(min(j)))
plt.plot(range(498, 502), j)
plt.show()



