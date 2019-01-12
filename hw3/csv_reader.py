import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def readData(filename) :
	data = pd.read_csv(filename, skipinitialspace=True)
	return [d for d in data.itertuples(index=False, name=None)]

if __name__ == '__main__':
	print(len(readData('hw03.csv')))
