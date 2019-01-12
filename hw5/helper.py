import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

def patch2col(g, win) :
    M, N = np.shape(g)
    gpad = np.pad(g, (win,win), 'symmetric')
    
    G = np.zeros([M, N, (2*win)**2]);
    for i in range(2*win) :
        for j in range(2*win) :
            k = np.ravel_multi_index([j, i], (2*win, 2*win))
            G[:,:,k] = gpad[i:i+M, j:j+N]
    
    G = np.reshape(np.transpose(G,(2,0,1)), ((2*win)**2, M*N))
    return G

def preprocess_data(Y) : 
    d = 64
    Ycol = patch2col(Y,4)
    Ymean = np.tile(np.mean(Ycol, 0), (d, 1))
    Ystd = np.tile(np.std(Ycol, 0, ddof = 1), (d, 1))
    Ynew = np.divide(np.subtract(Ycol, Ymean), Ystd)
    
    return Ynew
