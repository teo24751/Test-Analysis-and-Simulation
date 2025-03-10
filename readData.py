import csv
import numpy as np

def readLD(sampleNo,colNo):
    filename = "S"+str(sampleNo)+"_load_displ_data.csv"
    datList = []
    with open(filename, newline='') as csvfile:
        rawDat = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for i in rawDat:
            x = (i[-1]).split(",")[colNo]
            datList.append(x)
    return np.array(datList)

def load_displacement_curve():
    LD = np.stack((readLD(3,5),readLD(3,6)), axis=1)
    return LD