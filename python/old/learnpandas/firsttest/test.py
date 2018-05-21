import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series
data = {'a': 'aa', 'b' : 'bb'}
s = pd.Series(data)
# print(s)


s = pd.Series(np.random.randn(5))
# print(s)

s = pd.Series(np.random.randn(5), index={'a', 'b', 'c', 'd', 'e'})
# print(s)
print(s.index)