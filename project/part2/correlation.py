import numpy as np

def pearson(x, y):
	n = len(x)
	xy = np.multiply(x,y)
	x2 = np.square(x)
	y2 = np.square(y)
	num = n*np.sum(xy) - (np.sum(x) * np.sum(y))
	term1 = n*np.sum(x2) - np.square(np.sum(x))
	term2 = n*np.sum(y2) - np.square(np.sum(y))
	return num/np.sqrt(term1*term2)

def kendall(x, y):
	#print(np.array(x)[0].tolist())
	conc = 0; disc = 0
	n = len(x)
	idx = np.argsort(x)
	for i in idx:
		for j in range(i+1, n):
			#print('comparing {} and {}'.format(y[i], y[j]))
			if (y[i] < y[j]):
				conc += 1
			else:
				disc += 1
	#print(conc, disc)
	return float(conc-disc)/float(conc+disc)


ratio = 1.0; train_ratio = int(ratio*50)
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

train_x = np.matrix(train_x)
test_x = np.matrix(test_x)
train_total = np.matrix(train_total)
test_total = np.matrix(test_total)
train_violent = np.matrix(train_violent)
test_violent = np.matrix(test_violent)


train_x -= np.mean(train_x, 0)
train_x /= np.sqrt(np.sum(np.square(train_x), 0))
test_x -= np.mean(test_x, 0)
test_x /= np.sqrt(np.sum(np.square(test_x), 0))

train_total -= np.mean(train_total)
train_violent -= np.mean(train_violent)
test_total -= np.mean(test_total)
test_violent -= np.mean(test_violent)

if __name__ == '__main__':
	#print(train_x)
	#print(''); print(train_total); print('')
	#print(map(lambda x: x.item(2), train_x))
	#-------------------------------------------------------------------------------------------------------------
	print('------------------------------------------------------------------------------------------------------------')
	print("According to pearson's formula, correlation of total overall reported crime rate per 1 million residents with:")
	print('1) annual police funding in $/resident: '),
	print(pearson(train_total[0], map(lambda x: x.item(0), train_x)))
	print('2) % of people 25 years+ with 4 yrs. of high school: '),
	print(pearson(train_total[0], map(lambda x: x.item(1), train_x)))
	print('3) % of 16 to 19 year-olds not in highschool and not highschool graduates'),
	print(pearson(train_total[0], map(lambda x: x.item(2), train_x)))
	print('4) % of 18 to 24 year-olds in college: '),
	print(pearson(train_total[0], map(lambda x: x.item(3), train_x)))
	print('5) % of people 25 years+ with at least 4 years of college: '),
	print(pearson(train_total[0], map(lambda x: x.item(4), train_x)))
	#-------------------------------------------------------------------------------------------------------------
	print('------------------------------------------------------------------------------------------------------------')
	print("According to pearson's formula, correlation of reported violent crime rate per 100,000 residents with:")
	print('1) annual police funding in $/resident: '),
	print(pearson(train_violent[0], map(lambda x: x.item(0), train_x)))
	print('2) % of people 25 years+ with 4 yrs. of high school: '),
	print(pearson(train_violent[0], map(lambda x: x.item(1), train_x)))
	print('3) % of 16 to 19 year-olds not in highschool and not highschool graduates'),
	print(pearson(train_violent[0], map(lambda x: x.item(2), train_x)))
	print('4) % of 18 to 24 year-olds in college: '),
	print(pearson(train_violent[0], map(lambda x: x.item(3), train_x)))
	print('5) % of people 25 years+ with at least 4 years of college: '),
	print(pearson(train_violent[0], map(lambda x: x.item(4), train_x)))
	print('------------------------------------------------------------------------------------------------------------')
	#print(kendall([1,2,3,4], [8,7,6,5]))
	print('------------------------------------------------------------------------------------------------------------')
	print("According to kendall's formula, correlation of total overall reported crime rate per 1 million residents with:")
	print('1) annual police funding in $/resident: '),
	print(kendall(np.array(train_total)[0].tolist(), map(lambda x: x.item(0), train_x)))
	print('2) % of people 25 years+ with 4 yrs. of high school: '),
	print(kendall(np.array(train_total)[0].tolist(), map(lambda x: x.item(1), train_x)))
	print('3) % of 16 to 19 year-olds not in highschool and not highschool graduates'),
	print(kendall(np.array(train_total)[0].tolist(), map(lambda x: x.item(2), train_x)))
	print('4) % of 18 to 24 year-olds in college: '),
	print(kendall(np.array(train_total)[0].tolist(), map(lambda x: x.item(3), train_x)))
	print('5) % of people 25 years+ with at least 4 years of college: '),
	print(kendall(np.array(train_total)[0].tolist(), map(lambda x: x.item(4), train_x)))
	print('------------------------------------------------------------------------------------------------------------')
	print("According to kendall's formula, correlation of reported violent crime rate per 100,000 residents with:")
	print('1) annual police funding in $/resident: '),
	print(kendall(np.array(train_violent)[0].tolist(), map(lambda x: x.item(0), train_x)))
	print('2) % of people 25 years+ with 4 yrs. of high school: '),
	print(kendall(np.array(train_violent)[0].tolist(), map(lambda x: x.item(1), train_x)))
	print('3) % of 16 to 19 year-olds not in highschool and not highschool graduates'),
	print(kendall(np.array(train_violent)[0].tolist(), map(lambda x: x.item(2), train_x)))
	print('4) % of 18 to 24 year-olds in college: '),
	print(kendall(np.array(train_violent)[0].tolist(), map(lambda x: x.item(3), train_x)))
	print('5) % of people 25 years+ with at least 4 years of college: '),
	print(kendall(np.array(train_violent)[0].tolist(), map(lambda x: x.item(4), train_x)))
