import numpy as np
import scipy as sp
import main
import readData
import matplotlib.pyplot as plt
import math
import P_C_linearized

def f(x):
    return ((2+x)*(0.886+4.64*x-13.32*x**2+14.72*x**3-5.6*x**4))/(1-x)**1.5

def K_Q(P_Q,thickness,width,x):
    return P_Q/thickness/math.sqrt(width)*f(x)

#def fracture_toughness(displacements,loads,crack_lengths):
  #  return

def phi(x):
    return (1.9118+19.118*x-2.5122*x**2-23.226*x**3+20.54*x**4)*(1-x)/((19.118-5.0244*x-69.678*x**2+82.16*x**3)*(1-x)+2*(1.9118+19.118*x-2.5122*x**2-23.226*x**3+20.54*x**4))

def energy_integration(loads,displacements):
    return np.trapz(loads, x=displacements, axis=-1)

def G_Q(thickness,width,loads,displacements,x):
    U=energy_integration(loads,displacements)
    return U/thickness/width/phi(x)

def fracture_toughness():
    return K_IC



#Initial values

width=10 #to be modified
thickness=1 #to be modified
crack_length=1 #to be modified
x=crack_length/width
yield_stress=1
ligament=width-crack_length


for i in range(1,4):
    sample_number=i
    loads=list(readData.load_displacement_curve(sample_number)[:,0])
    displacements=list(readData.load_displacement_curve(sample_number)[:,1])
    frames=list(readData.load_displacement_curve(sample_number)[:,2])
    crack_tip_length=list(readData.crack_curve(sample_number)[:,0])
    crack_tip_to_edge_length=list(readData.crack_curve(sample_number)[:,1])
    y_displacement=list(readData.crack_curve(sample_number)[:,2]) #twice the displacement 

    maximum_load=max(loads)
    displacement_at_max_load=displacements[loads.index(maximum_load)]
    intersection_load,intersection_displacement,original_intersection_load,original_intersection_displacement=P_C_linearized(displacements,loads)
    
    if maximum_load/intersection_load>1.1:
        print("Test ",sample_number, " is invalid!")
    elif displacement_at_max_load>original_intersection_displacement and displacement_at_max_load<intersection_displacement:
        P_Q=maximum_load
    else:
        P_Q=intersection_load

    control_parameter=2.5*(K_Q(P_Q,thickness,width,x)/yield_stress)**2
    if control_parameter<thickness and control_parameter<ligament and control_parameter<crack_length:
        K_IC=K_Q(P_Q,thickness,width,x)
    else:
        print("Test ",sample_number, " is invalid!")

    energy_release_rate=G_Q(thickness,width,loads,displacements,x)

    K_IC, energy_release_rate






#Now the appropriate load has to be determined:
#if intersection_load/max(loads)>1.1:
  #  print('The test is invalid!')
#elif intersection_displacement<>:

#else:
#    P_Q=intersection_load