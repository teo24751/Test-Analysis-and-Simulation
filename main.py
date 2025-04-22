#libraries
import csv
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator,MaxNLocator

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
fig, axs = plt.subplots(3, 1, figsize=(8, 8))  # One figure with 3 vertical subplots
for sample_number in range(1,4):
    frames=d5045.frames(sample_number)
    method_d5045=d5045.fracture_toughnesses(sample_number)
    method_e399=e399.fracture_toughnesses(sample_number)
    method_area=area.fracture_toughnesses(sample_number)
    method_ccm=ccm.fracture_toughnesses(sample_number)

    ax = axs[sample_number - 1]  # Index starts from 0
   
    ax.plot(frames, method_d5045, 'o', color='blue', markersize=3, label='D5045')
    ax.plot(frames, method_d5045, '-', color='black', linewidth=0.5)

    ax.plot(frames, np.array(method_e399) * 1e-6, 'o', color='red', markersize=3, label='E399')
    ax.plot(frames, np.array(method_e399) * 1e-6, '-', color='black', linewidth=0.5)

    #ax.plot(frames, np.array(method_area) * 1e-6, 'o', color='yellow', markersize=3, label='Area')
    #ax.plot(frames, np.array(method_area) * 1e-6, '-', color='black', linewidth=0.5)

    ax.plot(frames, method_ccm, 'o', color='green', markersize=3, label='CCM')
    ax.plot(frames, method_ccm, '-', color='black', linewidth=0.5)

    

    ax.set_xlabel('Frame number')
    ax.set_ylabel(r'Fracture toughness [MPa$\sqrt{\mathrm{m}}$]')
    ax.set_title(f'Sample {sample_number}')

    ax.minorticks_on()
    ax.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=10))
    ax.grid(True, which='both', linewidth=0.5, alpha=0.7)
    ax.legend()

plt.tight_layout()
plt.savefig("fracture_toughness_plot.png", dpi=300)
plt.show()


