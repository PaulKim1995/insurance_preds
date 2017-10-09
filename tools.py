from scipy.stats import chisquare
import numpy as np


def chisquaretest(data, target, by):
    data1 = target[by == 0]
    data2 = target[by == 1]
    data1, data1counts = np.unique(data1, return_counts=True)
    data2, data2counts = np.unique(data2, return_counts=True)
    assert np.all(data1 == data2), 'input array categories are not identical'
    
    data1freq = data1counts / np.sum(data1counts)
    data2freq = data2counts / np.sum(data2counts)
    
    return chisquare(data2freq, f_exp=data1freq)
    