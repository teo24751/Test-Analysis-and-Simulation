#libraries
import csv
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt

#utlities
import readData
import DeterminingCompliance as complianceDet

#fracture toughness calculation methods
import AreaMethod as area
import ASTM_D5045 as d5045
import ASTM_E399 as e399
import ComplianceCalibrationMethod as ccm

#data arrays -- np arrays, 2D
LD1 = readData.load_displacement_curve(1)
LD2 = readData.load_displacement_curve(2)
LD3 = readData.load_displacement_curve(3)

#print(LD3)

#specimen geometry
specimenWidth = 0.07 #[m]
specimenHeight = 0.06 #[m]
specimenThickness = 0.008 #[m]
initialCrackLength = 0.013 #[m]
youngsModulus = 614e6#[Pa]
loadOffset = 0.01 #[m] -- distance from notch tip to load application point
specimenGeometryArray = np.array([specimenHeight,specimenWidth,specimenThickness,initialCrackLength,loadOffset])

#Different plots for different samples
#In one figure, all the methods are plotted for comparison
for sample_number in range(1,4):
    frames=d5045.frames(sample_number)
    method_d5045=d5045.fracture_toughnesses(sample_number)
    method_e399=e399.fracture_toughnesses(sample_number)
    method_area=area.fracture_toughnesses(sample_number)
    method_ccm=ccm.fracture_toughnesses(sample_number)
    plt.subplot(310+sample_number)
    plt.plot(frames,method_d5045)
    plt.plot(frames,method_e399)
    plt.plot(frames,method_area)
    plt.plot(frames,method_ccm)
    plt.xlabel('Frame number')
    plt.ylabel('Fracture toughness')



