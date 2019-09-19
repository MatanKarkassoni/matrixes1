
# -*- coding: utf-8 -*-
"""
use numpy to add the min and max matrix
"""
import numpy as np
import copy

x = np.array([[1, 2, 3], [4, 5, 6]])  
"""
x =  1   2   3
     4   5   6
"""
y = np.array([[7, 8], [9, 10], [11, 12]])
"""
y =   7    8
      9   10
     11   12
""" 
# =========== small =============
min_rows = min(len(x), len(y))
min_cols = min(len(x[0]), len(y[0]))

max_rows = max(len(x), len(y))
max_cols = max(len(x[0]), len(y[0]))

small = np.zeros((min_rows, min_cols))
"""
small =  0   0
         0   0
"""

x2 = copy.deepcopy(x)
y2 = copy.deepcopy(y)

x2 = np.delete(x2, np.s_[min_rows:max_rows:1], 0)
x2 = np.delete(x2, np.s_[min_cols:max_cols:1], 1)

y2 = np.delete(y2, np.s_[min_rows:max_rows:1], 0)
y2 = np.delete(y2, np.s_[min_cols:max_cols:1], 1)

small = np.add(x2, y2)
print(small)
# =========== big =============

big = np.zeros((max_rows, max_cols))
"""
x =  0   0   0
     0   0   0
     0   0   0
"""

x2 = copy.deepcopy(x)
y2 = copy.deepcopy(y)

x2 = np.append(x2, np.zeros((max_rows - min_rows, len(x[0]))), 0)
y2 = np.append(y2, np.zeros((len(x) + 1 , max_cols - min_cols)), 1)

big = np.add(x2, y2)
print(big)






