import numpy as np
import math
import scipy as sp
import matplotlib.pyplot as plt
from DeterminingCompliance import calculate_compliance
import readData as rd

P_crit = 10000 # Newton
thickness = 0.008 # meter

def func(a,alpha,beta,chi):
    return (alpha * a + beta)**chi

xdata = [0,1,2,3,5,7,8,9,9,10,11,20,23,25]
ydata = [0,1,2,3,4,6,6,7,8,9,15,16,17,20]

epic = sp.optimize.curve_fit(func, xdata, ydata, maxfev = 1000)

#print(epic)
t = np.arange(0.0, max(xdata)+1, 0.02)
plt.plot(xdata,ydata)

alpha = epic[0][0]
beta = epic[0][1]
chi = epic[0][2]
plt.plot(t, (alpha * t + beta)**chi, 'r--')
plt.show()
a = 0.02

alpha = float(alpha)
beta = float(beta)
chi = float(chi)

def G_IC(a, P_crit, alpha, beta, chi, thickness):

    return (P_crit ** 2) / (2 * thickness) * alpha * chi * (alpha * a + beta) ** (chi -1)


# MODIFIED PART
print(f"alpha: {alpha}, beta: {beta}, chi: {chi}")
compliance = calculate_compliance()
print(f"compliance: {compliance}")

def a_eff(C, n, alpha, beta, chi):
    return (C[n]**(1/chi) - beta)/alpha

a_effective = []
for i in range(len(compliance)):
    a_effective.append(a_eff(compliance, i, alpha, beta, chi))
print(f"Effective crack length: {a_effective}")

def G_IC_modified(a_effective, P_crit, alpha, beta, chi, thickness):
    return (P_crit ** 2) / (2*thickness) * alpha * chi * ((alpha * a_effective+beta) ** (chi-1))

