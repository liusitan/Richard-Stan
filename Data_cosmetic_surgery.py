from sklearn import decomposition
import random  
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import signal
np.random.seed(2017)
Spiking_Record = np.random.randint(0,high=2,size=(64,1000))
plt.plot(Spiking_Record[1], label='channel'+str(1))
def Cconversion_Continuous_Gaussian(W_gaussian,std_gaussian)#,dt)??
    Gaussian_window = signal.gaussian(M=100,std=4)#,sym=False)
    plt.plot(Gaussian_window)
    for i,value in enumerate(Spiking_Record):
        Spiking_Record[i,:] = signal.convolve(value,Gaussian_window)[:1000]
    plt.plot(Spiking_Record[1])
    plt.legend(loc='best')
    Spiking_Record=np.transpose(Spiking_Record)
    PCA_result=decomposition.PCA(n_components=3,whiten=True)
    pcs = PCA_result.fit(Spiking_Record).transform(Spiking_Record)
    #pcs = np.transpose(pcs)
    plt.plot(pcs)
