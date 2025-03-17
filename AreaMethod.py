import numpy as np

def fracture_toughness(data, t=0.008, E=614e06, v=0.3):
    """
    data[0] = displacement [mm]
    data[1] = load
    data[2] = crack length
    t = thickness of the specimen [mm]
    """
    data = np.transpose(np.array(data))
    G_IC = np.empty(len(data[0])-1)
    for i in range(len(data[0])-1):
        G_IC[i] = ((data[1][i+1]*data[0][i] - data[1][i]*data[0][i+1])/(2 * (t) * (data[2][i+1]-data[2][i])))


    K_IC = np.sqrt((E * G_IC) / (1 - v**2))
    
    return K_IC

if __name__ == "__main__":
    dataa = np.array([[1,2,3,4,5,7,8,9,10],[4,5,6,7,8,9,10,11,12],[7,8,9,10,11,12,13,14,15]])
    print(fracture_toughness(dataa))
    
