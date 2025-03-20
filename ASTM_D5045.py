import math
import numpy as np
import readData
import P_C_linearized

#Initial values
width=70/1000 #m
thickness=8/1000 #m
yield_stress=67*10**6 #Pa

def f(x):
    return ((2+x)*(0.886+4.64*x-13.32*x**2+14.72*x**3-5.6*x**4))/(1-x)**1.5

def K_Q(P_Q,thickness,width,x):
    return P_Q/(thickness)/math.sqrt(width)*f(x)

def phi(x):
    phi=(1.9118+19.118*x-2.5122*x**2-23.226*x**3+20.54*x**4)*(1-x)/((19.118-5.0244*x-69.678*x**2+82.16*x**3)*(1-x)+2*(1.9118+19.118*x-2.5122*x**2-23.226*x**3+20.54*x**4))
    print('Phi: ',phi)
    return phi

def energy_integration(loads,displacements):
    return np.trapz(loads, x=displacements, axis=-1)

def G_Q(thickness,width,loads,displacements,x):
    U=energy_integration(loads,displacements)
    print('Integration value: ',U)
    return U/(thickness)/(width)/phi(x)

def fracture_toughness(sample_number):
    return sample(sample_number)[0]

def energy_release_rate(sample_number):
    return sample(sample_number)[1]



def sample(sample_number):
    error=0
    loads=list(readData.load_displacement_curve(sample_number)[:,0]) #N
    displacements=list(readData.load_displacement_curve(sample_number)[:,1]) #mm
    #frames=list(readData.load_displacement_curve(sample_number)[:,2])
    crack_tip_length=list(readData.crack_curve(sample_number)[:,0]) #m
    
    
    intersection_load,intersection_displacement,original_intersection_load,original_intersection_displacement=P_C_linearized.intersection_load(displacements,loads)
    print("Crack array length: ",len(crack_tip_length))
    print("Loads array length: ",len(loads))
    loads_new=[]
    displacements_new=[]
    for i in range(20,451,5):
        loads_new.append(loads[i])
        displacements_new.append(displacements[i])
    loads=loads_new
    displacements=displacements_new
    
    #crack_tip_to_edge_length=list(readData.crack_curve(sample_number)[:,1])

    maximum_load=max(loads)
    print('Maximum load: ',maximum_load)
    crack_length=crack_tip_length[loads.index(maximum_load)]
    displacement_at_max_load=displacements[loads.index(maximum_load)]#mm
    
    x=crack_length/width
    print('x: ',x)
    #ligament=width-crack_length


    #if maximum_load/intersection_load>1.1:
       # print("Test ",sample_number, " is invalid due to max load!")
    print(maximum_load/intersection_load)
       # error=1
        #return(error)
        
    if displacement_at_max_load>original_intersection_displacement and displacement_at_max_load<intersection_displacement:
        P_Q=maximum_load
        print('P_Q: ',P_Q)
        control_parameter=2.5*(K_Q(P_Q,thickness,width,x)/yield_stress)**2
        #if control_parameter<thickness and control_parameter<ligament and control_parameter<crack_length:
        K_IC=K_Q(P_Q,thickness,width,x)
        G_IC=G_Q(thickness,width,loads,list(np.array(displacements)/1000),x)
        return K_IC,G_IC
        #else:
            #print("Test ",sample_number, " is invalid!")
            #error=1
            #return(error)
    else:
        P_Q=intersection_load
        print('P_Q: ',P_Q)
        control_parameter=2.5*(K_Q(P_Q,thickness,width,x)/yield_stress)**2
        #if control_parameter<thickness and control_parameter<ligament and control_parameter<crack_length:
        K_IC=K_Q(P_Q,thickness,width,x)
        G_IC=G_Q(thickness,width,loads,list(np.array(displacements)/1000),x)
        return K_IC,G_IC
        #else:
            #print("Test ",sample_number, " is invalid!")
            #error=1
            #return(error)

print('Fracture toughness [MPa*sqrt(m)]: ',fracture_toughness(3)*10**(-6))
print('Critical energy release rate: ',energy_release_rate(3))