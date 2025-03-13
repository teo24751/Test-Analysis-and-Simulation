import numpy as np
import DeterminingCompliance
import readData


def K_IC_func(P_c, a, t=8, w=70):
    return (P_c * faw_func(a/w)) / (t * np.sqrt(w))

def faw_func(aw):
    return ((2 + aw) / ((1 - aw) ** (1.5))) * ((0.866) + (4.64 * aw) - (13.32 * (aw ** 2)) + (14.72 * (aw ** 3)) + (5.6 * (aw ** 4)))

def G_IC_lam(K_IC, E_x, E_y, G_xy, v_xy):
    return ((K_IC ** 2) / (np.sqrt(2 * E_x * E_y))) * np.sqrt(np.sqrt(E_x / E_y) + (E_x / (E_y * G_xy)) - v_xy)

def fracture_toughness(a,):
    P_c = ...
    return K_IC_func(P_c, a)

if __name__ == "__main__":
    print(fracture_toughness())
