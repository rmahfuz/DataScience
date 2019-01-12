import numpy as np

"""Data: 57 features, 4601 data points"""
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

"""print(0, int(round(ratio*len(yes), 0))-1)
print(int(round(ratio*len(yes), 0)), int(round(len(yes), 0))-1)
print(len(yes), int(round(len(yes) + ratio*len(no), 0))-1)
print(int(round(len(yes) + ratio*len(no), 0)), int(round(len(yes) + len(no), 0))-1)"""

#Indices:
ind1 = 0
ind2 = int(round(ratio*len(yes), 0))
ind3 = int(round(len(yes), 0))
ind4 = int(round(len(yes) + ratio*len(no), 0))
ind5 = int(round(len(yes) + len(no), 0))

train_yes = yes[:ind2]; train_yes = np.transpose(train_yes)
train_no  = no [:int(round(ratio*len(no),0))]; train_no = np.transpose(train_no)
outcome_test = outcome[ind2:ind3] + outcome[ind4:ind5]
test_yes = yes[ind2:]; test_no = no [int(round(ratio*len(no),0)):]

"""train_yes = yes[:int(round(.8*len(yes), 0))]; train_yes = np.transpose(train_yes)
train_no  = no [:int(round(.8*len(no ), 0))]; train_no  = np.transpose(train_no )
outcome_test = outcome[1450:1813] + outcome[4043:4601]
test_yes = yes[int(round(.8*len(yes), 0)):] ; test_no  = no [int(round(.8*len(no ), 0)):]"""
print("len(yes) = {}, len(train_yes) = {}, len(test_yes) = {}\nlen(no ) = {}, len(train_no ) = {}, len(test_no ) = {}".format(len(yes), np.shape(train_yes)[1], len(test_yes), len(no), np.shape(train_no)[1], len(test_no)))
mean_yes = np.mean(train_yes, 1); mean_no  = np.mean(train_no, 1)
cov_yes = np.cov(train_yes); cov_no  = np.cov(train_no)

Y = test_yes + test_no
#print("Y.shape = {}x{}".format(len(Y), len(Y[0])))
output = []
p_yes = float(len(yes))/(len(yes) + len(no)); p_no  = float(len(no ))/(len(yes) + len(no))
term1 = -1*(len(Y[0])/2) * np.log10(2*np.pi)
term2_yes = -0.5* np.log10(np.linalg.det(cov_yes)); term12_yes = term1 + term2_yes
term2_no  = -0.5* np.log10(np.linalg.det(cov_no)) ; term12_no  = term1 + term2_no
cov_inv_yes = np.linalg.inv(cov_yes)
cov_inv_no  = np.linalg.inv(cov_no )

for point in Y:
	term3_yes = np.matmul(np.transpose(point - mean_yes), cov_inv_yes)
	term3_yes = -0.5 * np.matmul(term3_yes, point - mean_yes) + p_yes
	term3_no  = np.matmul(np.transpose(point - mean_no ), cov_inv_no )
	term3_no  = -0.5 * np.matmul(term3_no, point - mean_no ) + p_no
	if (term12_yes + term3_yes >= term12_no + term3_no):
		output.append(1)
	else:
		output.append(0)
wrong_spam  = 0; wrong_non_spam = 0
for i in range(len(output)):
	if outcome_test[i] == 1 and output[i] == 0:
		wrong_non_spam += 1
	if outcome_test[i] == 0 and output[i] == 1:
		wrong_spam += 1
error = np.float64(wrong_spam + wrong_non_spam)
print("Result: With training:testing ratio of {}, accuracy = 1 - {}/{} = {}".format(ratio, error, len(Y), 1-(error/len(Y))))
print("Fraction of non-spam incorrectly detected as spam = {}, fraction of spam incorrectly detected as non-spam = {}".format(np.float64(wrong_spam)/len(test_no), np.float64(wrong_non_spam)/len(test_yes)))


"""With ration = 0.8, 
len(yes) = 1813, len(train_yes) = 1450, len(test_yes) = 363
len(no ) = 2788, len(train_no ) = 2230, len(test_no ) = 558
cov_yes.shape = (57, 57)
Y.shape = 921x57
p_yes = 0.394044772875, p_no = 0.605955227125
"""
