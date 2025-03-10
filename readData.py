import csv
import numpy as np
from matplotlib import pyplot as plt

#use the load_displacement_curve function to get a 2D numpy array
# argument is the sample number (1-3)

#LOAD DISPLACEMENT FUNCTIONS
def readLD(sampleNo,colNo):
    filename = "data_CSV/S"+str(sampleNo)+"_load_displ_data.csv"
    datList = []
    with open(filename, newline='') as csvfile:
        rawDat = csv.reader(csvfile, delimiter=' ', quotechar='|')
        next(rawDat)
        for i in rawDat:
            x = float((i[-1]).split(",")[colNo])
            datList.append(x)
    return np.array(datList)

def load_displacement_curve(sampleNo):
    LD = np.stack((readLD(sampleNo,5),readLD(sampleNo,6)), axis=1)
    return LD

def plot_load_displacement_curve(sampleNo):
    curve = load_displacement_curve(sampleNo)
    plt.plot(curve[:,1],curve[:,0])
    plt.title("Load-displacement curve, sample "+str(sampleNo))
    plt.xlabel("Displacement [mm]") 
    plt.ylabel("Load [N]")
    plt.show()

#for testing
if __name__ == "__main__":
    plot_load_displacement_curve(3)