#libraries
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
#fracture toughness calculation methods
import AreaMethod as area
import ASTM_D5045 as d5045
import ASTM_E399 as e399
import ComplianceCalibrationMethod as ccm
import ModifiedCCM as modccm

#data arrays -- np arrays, 2D
loadDisplacement = []
crackLength = []

#specimen geometry
specimenWidth = 0.07 #[m]
specimenHeight = 0.06 #[m]
specimenThickness = 0.008 #[m]
initialCrackLength = 0.013 #[m]
loadOffset = 0.01 #[m] -- distance from notch tip to load application point
specimenGeometryArray = [specimenHeight,specimenWidth,specimenThickness,initialCrackLength,loadOffset]