import csv
import numpy as np
from matplotlib import pyplot as plt

#use the load_displacement_curve function to get a 2D numpy array
# argument is the sample number (1-3)

#LOAD DISPLACEMENT FUNCTIONS
def readLD(sampleNo,colNo):
    filename = f"data_CSV/S{str(sampleNo)}_load_displ_data.csv"
    datList = []
    with open(filename, newline='') as csvfile:
        rawDat = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(rawDat)
        for i in rawDat:
            x = float((i[-1]).split(",")[colNo])
            datList.append(x)
    return np.array(datList)

def load_displacement_curve(sampleNo):
    LD = np.stack((readLD(sampleNo,5),readLD(sampleNo,6),readLD(sampleNo,0)), axis=1)
    return LD

def plot_load_displacement_curve(sampleNoList):
    for i in sampleNoList:
        curve = load_displacement_curve(i)
        plt.plot(curve[:,1],curve[:,0], label="Sample "+str(i))
    plt.xlabel("Displacement [mm]") 
    plt.ylabel("Load [N]")
    plt.legend()
    plt.title("Load-Displacement Curve(s)")
    plt.show()


def readCrack(sampleNo, colNo):
    filename = f"data_CSV/S{str(sampleNo)}_crack_data.csv"
    datList = []
    with open(filename, newline='') as csvfile:
        rawDat = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(rawDat)
        for i in rawDat:
            x = float((i[-1]).split(",")[colNo])
            #print(x)
            datList.append(x)
    return np.array(datList)

def crack_curve(sampleNo):
    CC = np.stack((readCrack(sampleNo,2), readCrack(sampleNo,4), readCrack(sampleNo,1), readCrack(sampleNo,0)), axis = 1)
    #print(CC)
    return CC
print(len(crack_curve(1)))
print(len(crack_curve(2)))
print(len(crack_curve(3)))
def plot_crack_curve(sampleNoList, framePlot = True):
    for i in sampleNoList:
        curve = crack_curve(i)
        if framePlot:
            plt.plot(curve[:,3],curve[:,0], label="Sample "+str(i))
        else:
            plt.plot(curve[:,2],curve[:,0], label="Sample "+str(i))
    #plt.xlabel("Y-displacement [mm]") 
    plt.xlabel("Y-Displacement [mm]") 
    if framePlot:
        plt.xlabel("Frame [-]")
    plt.ylabel("Crack length [mm]")
    plt.legend()
    plt.title("Crack Length Propagation")
    plt.show()

def data_short(sampleNo):#trim load data
    lDat = load_displacement_curve(sampleNo)
    cDat = crack_curve(sampleNo)
    frameNo = cDat.shape[0]
    frames = cDat[:,-1].astype(np.int64)    
    short_lDat = lDat[frames]
    shortDat = np.zeros((frameNo,4))
    shortDat[:,-1] = cDat[:,-1]#frame number
    shortDat[:,2] = cDat[:,0]#crack length
    shortDat[:,0] = short_lDat[:,1]#displacement
    shortDat[:,1] = short_lDat[:,0]#load
    return shortDat

def data_long():#interpolates crack length data
    pass

def plot_all_data():
    ax1 = plt.subplot(311)
    ax2 = plt.subplot(312)
    ax3 = plt.subplot(313)
    for i in range(1,4):
        frm1 = load_displacement_curve(i)[:,-1]
        frm2 = crack_curve(i)[:,-1]
        ax1.plot(frm1, load_displacement_curve(i)[:,0], label="Sample "+str(i))
        ax1.set_ylabel("Load [N]")

        # share x only
        ax2.plot(frm2, crack_curve(i)[:,0], label="Sample "+str(i))
        ax2.set_ylabel("Crack Length [mm]")

        # share x and y
        ax3.plot(frm1, load_displacement_curve(i)[:,1], label="Sample "+str(i))
        ax3.set_ylabel("Displacement [mm]")
        ax3.set_xlabel("Frame")
    plt.legend()
    plt.show()

#for testing
if __name__ == "__main__":
    #plot_load_displacement_curve([2])
    #plot_crack_curve([1,2,3], framePlot=False)
    #crack_curve(3)
    #print(data_short(1))
    pass