import numpy as np
import DeterminingCompliance
import scipy.interpolate as interp
import scipy.optimize as opt
from matplotlib import pyplot as plt
import P_C_linearized
import readData

def K_IC_func(P_c, a, t=0.008, w=0.070):
    return (P_c * faw_func(a/w)) / (t * np.sqrt(w))


def faw_func(aw):
    return ((2 + aw) / ((1 - aw) ** (1.5))) * ((0.866) + (4.64 * aw) - (13.32 * (aw ** 2)) + (14.72 * (aw ** 3)) + (5.6 * (aw ** 4)))


def G_IC_lam(K_IC, E_x, E_y, G_xy, v_xy):
    return ((K_IC ** 2) / (np.sqrt(2 * E_x * E_y))) * np.sqrt(np.sqrt(E_x / E_y) + (E_x / (E_y * G_xy)) - v_xy)


def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    xy_mean = np.mean(x * y)
    xx_mean = np.mean(x * x)
    
    slope = (xy_mean - x_mean * y_mean) / (xx_mean - x_mean ** 2)
    intercept = y_mean - slope * x_mean
    
    return slope, intercept


def intersection(slope, intercept, loaddisplacement):
    newloaddisplacement = [point for point in loaddisplacement if point[1] > 2]

    load = np.array([point[0] for point in newloaddisplacement])
    displacement = np.array([point[1] for point in newloaddisplacement])

    unique_displacement, unique_indices = np.unique(displacement, return_index=True)
    unique_load = load[unique_indices]
    curve = interp.interp1d(unique_displacement, unique_load, kind='cubic', fill_value='extrapolate')

    def objective(x):
        return curve(x) - (slope * x + intercept)

    intersection_x = opt.fsolve(objective, x0=2)[0]
    P_C = curve(intersection_x)

    return P_C, intersection_x


def main(loaddisplacement): # TODO: rename to fracture_toughness
    lin_start = 1
    lin_end = 3
    linear_interval = [point for point in loaddisplacement if lin_start <= point[1] <= lin_end]

    displacement = np.array([point[1] for point in linear_interval])
    load = np.array([point[0] for point in linear_interval])

    slope, intercept = linear_regression(displacement, load)

    P_C, intersection_x = intersection(0.95 * slope, intercept, loaddisplacement)

    return P_C, slope, intercept, intersection_x


def fracture_toughness(data, crack_curve):
    load = list(data[:,0])
    displacement = list(data[:,1])
    max_load = max(load)
    displacement_at_max_load = displacement[load.index(max_load)]
    crack_tip = crack_curve[:,0]
    crack_length = crack_tip[load.index(max_load)]

    intersection_load,intersection_displacement,original_intersection_load,original_intersection_displacement = P_C_linearized.intersection_load(displacement,load)
    displacement_at_max_load=displacement[load.index(max_load)]

    if displacement_at_max_load < original_intersection_displacement or displacement_at_max_load > intersection_displacement:
        P_Q = intersection_load
    else:
        P_Q = max_load

    K_IC = K_IC_func(P_Q, crack_length)
    G_IC = G_IC_lam(K_IC, 614e06, 614e06, 0.3, 0.3)

    return K_IC, G_IC


if __name__ == "__main__":
    # # a = np.array([])
    data = readData.load_displacement_curve(1)
    crack_curve = readData.crack_curve(1)
    print(fracture_toughness(data, crack_curve))