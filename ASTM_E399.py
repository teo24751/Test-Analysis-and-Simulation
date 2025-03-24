import numpy as np
import DeterminingCompliance
import scipy.interpolate as interp
import scipy.optimize as opt
from matplotlib import pyplot as plt
import P_C_linearized
import readData

def K_IC_func(P_c, a, t=8e-3, w=0.070):
def K_IC_func(P_c, a, t=8e-3, w=0.070):
    return (P_c * faw_func(a/w)) / (t * np.sqrt(w))


def faw_func(aw):
    return ((2 + aw) / ((1 - aw) ** (1.5))) * ((0.866) + (4.64 * aw) - (13.32 * (aw ** 2)) + (14.72 * (aw ** 3)) + (5.6 * (aw ** 4)))


def G_IC_lam(K_IC, E, v):
    return ((K_IC ** 2) / (E / (1 - v ** 2)))
    # return ((K_IC ** 2) / (np.sqrt(2 * E_x * E_y))) * np.sqrt(np.sqrt(E_x / E_y) + (E_x / (E_y * G_xy)) - v_xy)


def fracture_toughness(data, crack_curve, E=614e06, v=0.3):
    load = list(data[:,0])
    displacement = list(data[:,1])
    max_load = max(load)
    displacement_at_max_load = displacement[load.index(max_load)]
    crack_tip = crack_curve[:,0]
    crack_length = crack_tip[np.ceil(load.index(max_load)/5)]
    
    load_new = []
    displacement_new = []
    for i in range(20,451,5):
        load_new.append(load[i])
        displacement_new.append(displacement[i])

    # intersection_load,intersection_displacement,_,original_intersection_displacement = P_C_linearized.intersection_load(displacement,load)
    # displacement_at_max_load=displacement[load.index(max_load)]

    # if displacement_at_max_load > original_intersection_displacement and displacement_at_max_load < intersection_displacement:
    #     print("Max load")
    #     P_Q = max_load
    # else:
    #     print("Intersection load")
    #     P_Q = intersection_load
    # if displacement_at_max_load > original_intersection_displacement and displacement_at_max_load < intersection_displacement:
    #     print("Max load")
    #     P_Q = max_load
    # else:
    #     print("Intersection load")
    #     P_Q = intersection_load

    # print(f"P_Q: {P_Q}")
    # print(f"P_Q: {P_Q}")

    # K_IC = K_IC_func(P_Q, crack_length)
    K_IC = K_IC_func(load_new, crack_tip)
    # K_IC = K_IC_func(P_Q, crack_length)
    K_IC = K_IC_func(load_new, crack_tip)
    G_IC = G_IC_lam(K_IC, E, v)

    return K_IC, G_IC


if __name__ == "__main__":
    sample = 3
    sample = 3
    data = readData.load_displacement_curve(sample)
    crack_curve = readData.crack_curve(sample)
    K_IC, G_IC = fracture_toughness(data, crack_curve)
    print(K_IC, G_IC)
    # print(f"fracture tougness: {K_IC} Pa m^0.5")
    # print(f"energy release rate: {G_IC} J/m^2")
    # print(f"E = { (K_IC ** 2) / G_IC }")
    print(K_IC, G_IC)
    # print(f"fracture tougness: {K_IC} Pa m^0.5")
    # print(f"energy release rate: {G_IC} J/m^2")
    # print(f"E = { (K_IC ** 2) / G_IC }")
    