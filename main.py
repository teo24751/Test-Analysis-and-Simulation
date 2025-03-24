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
#import ASTM_D5045 as d5045
#import ASTM_E399 as e399
#import ComplianceCalibrationMethod as ccm

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

#get fracture toughness from methods
#AREAMETHOD = area.fracture_toughness(readData.data_short(1), t = specimenThickness)

#output fracture toughness
print("Fracture toughnesses:")
#print(f"Area Method: {AREAMETHOD}")
print(f"ASTM D5045: {5}")
print(f"ASTM E399: {5}")
print(f"Compliance: {5}")
print(f"Modified Compliance: {5}")

#graph crack length
area.plot_gic(readData.data_short(2))

#graph load-displacement
readData.plot_all_data()