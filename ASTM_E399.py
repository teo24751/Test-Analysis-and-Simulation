import numpy as np
import DeterminingCompliance
from matplotlib import pyplot as plt
import readData

"""
get P_c from load-displacement curve
    get slope
    find intersection with 0.95 * slope

get K_IC from P_c, and a
"""

def K_IC_func(P_c, a, t=8, w=70):
    return (P_c * faw_func(a/w)) / (t * np.sqrt(w))

def faw_func(aw):
    return ((2 + aw) / ((1 - aw) ** (1.5))) * ((0.866) + (4.64 * aw) - (13.32 * (aw ** 2)) + (14.72 * (aw ** 3)) + (5.6 * (aw ** 4)))

def G_IC_lam(K_IC, E_x, E_y, G_xy, v_xy):
    return ((K_IC ** 2) / (np.sqrt(2 * E_x * E_y))) * np.sqrt(np.sqrt(E_x / E_y) + (E_x / (E_y * G_xy)) - v_xy)

def fracture_toughness(loaddisplacment):
    pv = 
    







# def fracture_toughness(a, loaddisplacement):
#     pv = loaddisplacement[30][0] / (loaddisplacement[30][1]-loaddisplacement[0][1])

#     for i in range(len(loaddisplacement)):
#         if loaddisplacement[i][0] <= 0.95 * pv * loaddisplacement[i][1]:
#             P_c = loaddisplacement[i][0]
#             break
    
#     return P_c
#     # return K_IC_func(P_c, a)

# if __name__ == "__main__":
#     # a = np.array([])
#     loaddisplacement = readData.load_displacement_curve(3)
#     # print(loaddisplacement)
#     # print(fracture_toughness(..., loaddisplacement))
    
#     x = 50 
#     P_c = fracture_toughness(..., loaddisplacement)
    
#     # Extract load and displacement values
#     load, displacement = zip(*loaddisplacement)
    
#     # Plot load-displacement curve
#     plt.plot(displacement, load, label='Load-Displacement Curve')
#     plt.xlabel('Displacement')
#     plt.plot(displacement, [0.95 * P_c * d for d in displacement], label='y = 0.95 * P_c * displacement', linestyle='--')
#     plt.ylabel('Load')
#     plt.title('Load vs Displacement')
#     plt.legend()
#     # Calculate the slope (tangent) at displacement = a
#     slope = (load[x + 1] - load[x - 1]) / (displacement[x + 1] - displacement[x - 1])
    
#     # Define the tangent line
#     tangent_line = [slope * (d - x) + load[x] for d in displacement]
    
#     # Plot the tangent line
#     plt.plot(displacement, tangent_line, label='Tangent at a', linestyle='-.')
#     # Highlight P_c on the plot
#     plt.scatter([displacement[load.index(P_c)]], [P_c], color='red', zorder=5)
#     plt.annotate(f'P_c = {P_c}', (displacement[load.index(P_c)], P_c), textcoords="offset points", xytext=(10,-10), ha='center')

#     plt.show()
