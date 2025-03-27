import numpy as np
from matplotlib import pyplot as plt
import readData

def G_IC(short_data, t=0.008, v = 0.3):#Calculates the energy release rate G_IC
    disp = short_data[:,0]
    load = short_data[:,1]
    crack = short_data[:,2]
    frame = short_data[:,3]
    gic = np.zeros((frame.shape[0],2))
    i=0
    while i < (frame.shape[0]-1):
        while crack[i+1] - crack[i] == 0:
            gic[i,1] = frame[i]
            gic[i,0] = gic[i-1,0]
            i += 1
        gic[i,0] = abs(((load[i]*disp[i+1] - load[i+1]*disp[i]) /( 2*t* (crack[i+1]-crack[i]))))
        gic[i,1] = frame[i]
        i+=1
    #print("G_C DATA")
    #print(gic)
    return gic

def fracture_toughness(short_data, E = 614e6, v=0.3):
    ePrime = E/(1-v*v)
    gic = G_IC(short_data)
    kic = gic
    kic[:,0] = np.sqrt(gic[:,0] * ePrime)
    kic[:,1] = gic[:,1]
    #print("K_IC DATA")
    #print(kic)
    ft = np.mean(kic[15:,0])
    return kic

def plot_gic(short_data):
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)
    gicdat = G_IC(short_data)
    kicdat = fracture_toughness(short_data)
    ax1.plot(gicdat[:,0], gicdat[:,1])
    ax2.plot(kicdat[:,0], kicdat[:,1])
    plt.show()

# def fracture_toughness(data, t=0.008, E=614e06, v=0.3):
#     """
#     data[0] = displacement [mm]
#     data[1] = load
#     data[2] = crack length
#     t = thickness of the specimen [mm]
#     """
#     data = np.array(data)
#     print("DATA")
#     print(data)
#     G_IC = np.empty(data.shape[0]-1)
#     print("GIC")
#     print(G_IC)
#     for i in range(len(data[0])-1):
#         G_IC[i] = ((data[1][i+1]*data[0][i] - data[1][i]*data[0][i+1])/(2 * (t) * (data[2][i+1]-data[2][i])))


#     K_IC = np.average(np.sqrt((E * G_IC) / (1 - v**2)))
    
#     return K_IC

# if __name__ == "__main__":
#     dataa = np.array([[1,2,3,4,5,7,8,9,10],[4,5,6,7,8,9,10,11,12],[7,8,9,10,11,12,13,14,15]])
#     print(fracture_toughness(dataa))
    
