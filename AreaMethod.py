import numpy as np

def fracture_toughness(data, t=8):
    G_IC = np.empty(len(data[0])-1)
    for i in range(len(data[0])-1):
        G_IC[i] = ((data[1][i+1]*data[0][i] - data[1][i]*data[0][i+1])/(2 * (t / 1000) * (data[2][i+1]-data[2][i])))
    return G_IC

if __name__ == "__main__":
    print(fracture_toughness([[1,2,3],[4,5,6],[7,8,9]]))
    
