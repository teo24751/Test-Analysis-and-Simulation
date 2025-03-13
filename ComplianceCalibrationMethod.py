import numpy as np
import math
import scipy as sp
import matplotlib.pyplot as plt

#from ASTM_D5045 import crack_lengths
from DeterminingCompliance import calculate_compliance
import readData as rd

P_crit = 1000 # Newton
thickness = 0.008 # meter
compliance = calculate_compliance()
def func(a,alpha,beta,chi):
    return (alpha * a + beta)**chi
crack_lengths = np.arange(0.0, len(compliance), 1)
xdata = [0,1,2,3,4,5,6,7,8,10]
ydata = [0,1,2,3,4,5,6,7,8,10]

#print(len(xdata), len(ydata))
epic = sp.optimize.curve_fit(func, xdata, ydata, maxfev = 1000)

#print(epic)
t = np.arange(0.01, max(xdata)+1, 0.02)
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

G_IC_list = []

for i in range(len(compliance)):
    G_IC_list.append(G_IC(crack_lengths[i]/1000, P_crit, alpha, beta, chi, thickness))



# MODIFIED PART
print(f"alpha: {alpha}, beta: {beta}, chi: {chi}")

#print(f"compliance: {compliance}")

def a_eff(C, n, alpha, beta, chi):
    return (C[n]**(1/chi) - beta)/alpha

a_effective = []
for i in range(len(compliance)):
    a_effective.append(a_eff(compliance, i, alpha, beta, chi))
#print(f"Effective crack length: {a_effective}")

def G_IC_modified(a_effective, n, P_crit, alpha, beta, chi, thickness):
    return (P_crit ** 2) / (2*thickness) * alpha * chi * ((alpha * a_effective[n] + beta) ** (chi-1))

G_IC_mod = []
for i in range(len(a_effective)):
    G_IC_mod.append(G_IC_modified(a_effective, i, P_crit, alpha, beta, chi, thickness))
#print('Toughness:', G_IC_mod)

#plt.plot(crack_lengths/1000, G_IC_mod)
plt.plot(crack_lengths/1000, G_IC_list)
plt.show()

for i in range(0,500,10):
    print(G_IC_list[i])