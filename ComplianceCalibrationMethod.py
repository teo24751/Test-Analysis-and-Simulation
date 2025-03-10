import numpy as np
import math
import scipy as sp

P_crit = 10000 # Newton
thickness = 0.008 # meter

def func(x,alpha,beta,chi):
    return (alpha * x + beta)**chi

xdata = [1,2,3,5]
ydata = [4,2,5,5]

epic = sp.optimize.curve_fit(func, xdata, ydata)

print(epic)