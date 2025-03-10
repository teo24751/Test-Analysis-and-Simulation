#libraries
import csv
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
#utlities
import readData
#fracture toughness calculation methods
import AreaMethod as area
import ASTM_D5045 as d5045
import ASTM_E399 as e399
import ComplianceCalibrationMethod as ccm
import DeterminingCompliance as complianceDet

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
loadOffset = 0.01 #[m] -- distance from notch tip to load application point
specimenGeometryArray = np.array([specimenHeight,specimenWidth,specimenThickness,initialCrackLength,loadOffset])