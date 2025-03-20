import numpy as np
from matplotlib import pyplot as plt
import readData

def G_IC(short_data, t=0.008, v = 0.3):
    disp = short_data[:,0]
    load = short_data[:,1]
    crack = short_data[:,2]
    frame = short_data[:,3]
    gic = np.zeros((frame.shape[0],2))

    for i in range(frame.shape[0]-1):
        gic[i,0] = (load[i]*disp[i+1] - load[i+1]*disp[i]) /( 2*t* (crack[i+1]-crack[i]))
        gic[i,1] = frame[i]
    return gic

def fracture_toughness(short_data, sampleNo):
    gic = G_IC(short_data)

    pass
def plot_gic(short_data):
    gicdat = G_IC(short_data)
    plt.plot(gicdat[:,0], gicdat[:,1])
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
    
