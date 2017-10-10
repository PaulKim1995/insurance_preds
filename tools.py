from scipy.stats import chisquare
import numpy as np
from scipy.stats import norm


def chisquaretest(data, target, by):
    data1 = target[by == 0]
    data2 = target[by == 1]
    data1, data1counts = np.unique(data1, return_counts=True)
    data2, data2counts = np.unique(data2, return_counts=True)
    assert np.all(data1 == data2), 'input array categories are not identical'
    
    data1freq = data1counts / np.sum(data1counts)
    data2freq = data2counts / np.sum(data2counts)
    
    return chisquare(data2freq, f_exp=data1freq)
    
    
def zTest(X1, X2, mudiff, sd1, sd2, n1, n2):
    pooledSE = np.sqrt(sd1**2/n1 + sd2**2/n2)
    z = ((X1 - X2) - mudiff)/pooledSE
    pval = 2*(1 - norm.cdf(np.abs(z)))
    return np.round(z, 3), np.round(pval, 4)


def twoSampleZ(d1, d2):
    u1 = np.mean(d1)
    u2 = np.mean(d2)
    mudiff = u1-u2
    sd1 = np.sqrt(np.var(d1))
    sd2 = np.sqrt(np.var(d2))
    n1 = len(d1)
    n2 = len(d2)
    print(u1, u2, mudiff, sd1, sd2, n1, n2)
    return zTest(u1, u2, mudiff, sd1, sd2, n1, n2)
