import numpy as np
from pprint import pprint as pp

yes = []; no = []; outcome = []
ratio = 0.8
#Reading the data from data.txt:
with open('data.txt', 'r') as data:
	for line in data.readlines():
		#train_cat.append(map(lambda x: np.float64(x), line.split(',')))
		point = (map(lambda x: np.float64(x), line.split(' ')))
		outcome.append(point[-1])
		if point[-1] == 1:
			yes.append(point[:len(point)-1])
		else:
			no.append(point[:len(point)-1])
#Indices:
ind1 = 0
ind2 = int(round(ratio*len(yes), 0))
ind3 = int(round(len(yes), 0))
ind4 = int(round(len(yes) + ratio*len(no), 0))
ind5 = int(round(len(yes) + len(no), 0))

train_yes = yes[:ind2]; #train_yes = np.transpose(train_yes)
train_no  = no [:int(round(ratio*len(no),0))]; #train_no = np.transpose(train_no)
outcome_test = outcome[ind2:ind3] + outcome[ind4:ind5]
test_yes = yes[ind2:]; test_no = no [int(round(ratio*len(no),0)):]

print("len(yes) = {}, len(train_yes) = {}, len(test_yes) = {}\nlen(no ) = {}, len(train_no ) = {}, len(test_no ) = {}".format(len(yes), np.shape(train_yes)[1], len(test_yes), len(no), np.shape(train_no)[1], len(test_no)))

Y = test_yes + test_no
output = []; idx = 0

for point in Y:  #runs 187500 times
	dist = []
	for feature in train_yes:   #runs 500 times
		#print(type(point), type(feature), len(point), len(feature))
		diff = np.array(point)-np.array(feature)    #list of 57 items
		dist.append((np.dot(diff, diff), 'Y'))  #appends a tuple (distance, 'C')
	for feature in train_no : #runs 500 times
		diff = np.array(point)-np.array(feature)
		dist.append((np.dot(diff, diff), 'N'))
	cnt = 0
	for i in np.argsort(map(lambda x: x[0], dist))[:5]:
		if dist[i][1] == 'Y':
			cnt += 1
		else:
			cnt -= 1
	output.append(int(cnt > 0))
	idx +=1
	if idx%1000 == 0:
		print idx

wrong_spam = 0; wrong_non_spam = 0
for i in range(len(output)):
	if outcome_test[i] == 1 and output[i] == 0:
		wrong_non_spam += 1
	if outcome_test[i] == 0 and output[i] == 1:
		wrong_spam += 1
error = np.float64(wrong_spam + wrong_non_spam)
print("Result: With training:testing ratio of {}, accuracy = 1 - {}/{} = {}".format(ratio, error, len(Y), 1-(error/len(Y))))
print("Fraction of non-spam incorrectly detected as spam = {}, fraction of spam incorrectly detected as non-spam = {}".format(np.float64(wrong_spam)/len(test_no), np.float64(wrong_non_spam)/len(test_yes)))
