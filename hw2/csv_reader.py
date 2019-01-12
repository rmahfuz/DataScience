import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def readData(filename) :
	data = pd.read_csv(filename, header=None, skipinitialspace=True)
	return [d for d in data.itertuples(index=False, name=None)]
	