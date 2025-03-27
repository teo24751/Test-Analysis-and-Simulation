import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import readData as rd
from P_C_linearized import intersection_load
# from DeterminingCompliance import sample_number


def fracture_toughnesses(sample_number):
    array = rd.load_displacement_curve(sample_number)
    def compliance(n,arr):
        return arr[n][1]/arr[n][0]

    compl = []

    for i in range(6,len(array)-2):
        compl.append(compliance(i,array)/1000)

    def calculate_compliance():
        return compl



    # Initial values and constants
    E = 0.614 * 10 ** 9 # Pa - Young's modulus
    h = 0.00001
    thickness = 0.008 # meter
    compliance_init = calculate_compliance()
    crack_lengths = [] # x data
    compliance = [] # y data

    # Determine the critical load
    loads=list(rd.load_displacement_curve(sample_number)[:,0])
    displacements=list(rd.load_displacement_curve(sample_number)[:,1])
    P_crit = intersection_load(displacements,loads)[0] # Newton
    crack_tip_length=list(rd.crack_curve(sample_number)[:,0]) # m
    maximum_load=max(loads)
    critical_crack_length=crack_tip_length[loads.index(maximum_load)]

    loads_new=[]
    displacements_new=[]
    for i in range(20,451,5):
        loads_new.append(loads[i])
        displacements_new.append(displacements[i])
    loads=loads_new
    displacements=displacements_new

    amazing = rd.crack_curve(sample_number)

    for i in range(len(amazing)):
        crack_lengths.append(amazing[i][0])

    for i in range(20, 451, 5):
        compliance.append(compliance_init[i])

    '''
    print("Displacements: ", displacements_new)
    print("Loads New: ", loads_new)
    print("Cack Lengths", crack_lengths)
    print("Critical crack length: ", critical_crack_length, "m")
    print("Critical Load", P_crit, "N")
    print("Compliance", compliance)
    print("HERE", crack_lengths[72], loads[72])
    '''

    # Curve fitting
    def func(a,alpha,beta,chi):
        return (alpha * a + beta)**chi

    epic = sp.optimize.curve_fit(func, crack_lengths, compliance, maxfev = 100000)
    alpha, beta, chi = float(epic[0][0]), float(epic[0][1]), float(epic[0][2])
    t = np.arange(0.000, max(crack_lengths)+0.001, 0.001)
    #print(f"alpha: {alpha}, beta: {beta}, chi: {chi}")

    # Plots the data and the fitted model
    ###plt.plot(crack_lengths,compliance, label='Data', linewidth=2, color="gray")
    ###plt.plot(t, (alpha * t + beta)**chi, 'r--', label='Fitted model')
    ###plt.title('Crack-length - Compliance curve')
    ###plt.legend()
    ###plt.xlabel('Crack length')
    ###plt.ylabel('Compliance')
    ###plt.show()

    def derivative(a,alpha,beta,chi,h):
        return (func(a+h, alpha, beta, chi)-func(a,alpha,beta,chi))/(h)


    # Calculates G_IC (energy release rate) from the fitted model
    def G_IC(a, P_crit, alpha, beta, chi, thickness):
        return (P_crit ** 2) / (2 * thickness) * derivative(a,alpha,beta,chi,h)          # * alpha * chi * (alpha * a + beta) ** (chi -1)
    #print(f"Critical load {P_crit} N")
    G_IC_list = []

    for i in range(len(compliance)):
        G_IC_list.append(G_IC(crack_lengths[i], P_crit, alpha, beta, chi, thickness))


    # Determine K_IC from G_IC
    def fracture_toughness(G_IC, E, v):
        return np.sqrt((E * G_IC)/(1-v**2)) # NOTE THAT THIS FORMULA ASSUMES LINEARITY OF THE STRESS STRAIN CURVE, AND THIS COULD NOT BE THE CASE FOR THE MATERIAL UNDER STUDY

    # Find the index of the maximum load
    max_load_index = loads.index(max(loads))

    K_ICs = []
    for i in range(len(loads)):
        G = G_IC(crack_lengths[i], loads_new[i], alpha, beta, chi, thickness)
        K_ICs.append(fracture_toughness(G, E, 0.3)/(10 ** 6))

    iter = []
    for i in range(len(K_ICs)):
        iter.append(i)

    ###plt.plot(iter, K_ICs)
    ###plt.title(f'Crack-length - Energy release rate curve')
    ###plt.xlabel('Crack length [m]')
    ###plt.ylabel('Energy release rate [J/m^2]')
    ###plt.show()


    # CRITICAL G_IC AND K_IC VALUES
    crit_G_IC = (P_crit ** 2) / (2 * thickness) * derivative(critical_crack_length,alpha,beta,chi,h)
    crit_K_IC = fracture_toughness(crit_G_IC, E, 0.3)

    #print(f"Critical crack length is {critical_crack_length} m")
    #print(f"Critical G_IC: {crit_G_IC} J/m^2. Critical K_IC: {crit_K_IC/(10**6)} MPam^0.5")


    return K_ICs



'''
NOTES:
- assumed linearity of the stress-strain curve to convert G_IC to K_IC
'''

'''
MODIFIED COMPLIANCE CALIBRATION METHOD:
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
##print('Toughness:', G_IC_mod)
'''
