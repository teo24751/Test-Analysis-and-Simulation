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

def plot_including_area_method():
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))  # One figure with 3 vertical subplots
    for sample_number in range(1,4):
        frames=d5045.crack_tip_length(sample_number)
        method_d5045=d5045.fracture_toughnesses(sample_number)
        #method_e399=e399.fracture_toughnesses(sample_number)
        method_area=area.fracture_toughnesses(sample_number)[:,0]
        method_ccm=ccm.fracture_toughnesses(sample_number)[0]

        ax = axs[sample_number - 1]  # Index starts from 0
    
        ax.plot(frames, method_d5045, 'o', color='blue', markersize=3, label='D5045')
        ax.plot(frames, method_d5045, '-', color='black', linewidth=0.5)

        #ax.plot(frames, np.array(method_e399) * 1e-6, 'o', color='red', markersize=3, label='E399')
        #ax.plot(frames, np.array(method_e399) * 1e-6, '-', color='black', linewidth=0.5)

        ax.plot(frames, np.array(method_area) * 1e-6, 'o', color='orange', markersize=3, label='Area')
        ax.plot(frames, np.array(method_area) * 1e-6, '-', color='black', linewidth=0.5)

        ax.plot(frames, method_ccm, 'o', color='green', markersize=3, label='CCM')
        ax.plot(frames, method_ccm, '-', color='black', linewidth=0.5)

        
        #ax.set_xlim(0, 450)
        #ax.set_ylim(0, 100)

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
    plt.savefig("fracture_toughness_plot_including_area_method.png", dpi=300)
    #plt.show()

def reduced_plot_including_area_method():
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))  # One figure with 3 vertical subplots
    for sample_number in range(1,4):
        frames=d5045.crack_tip_length(sample_number)
        method_d5045=d5045.fracture_toughnesses(sample_number)
        #method_e399=e399.fracture_toughnesses(sample_number)
        method_area=area.fracture_toughnesses(sample_number)[:,0]
        #print('Area methods: ',method_area)
        method_ccm=ccm.fracture_toughnesses(sample_number)[0]

        #G_IC_method_cmm = ccm.fracture_toughnesses(sample_number)[1]

        ax = axs[sample_number - 1]  # Index starts from 0
    
        ax.plot(np.array(frames)*1000, method_d5045, 'o', color='blue', markersize=3, label='D5045 & E399')
        ax.plot(np.array(frames)*1000, method_d5045, '-', color='black', linewidth=0.5)

        #ax.plot(frames, np.array(method_e399) * 1e-6, 'o', color='red', markersize=3, label='E399')
        #ax.plot(frames, np.array(method_e399) * 1e-6, '-', color='black', linewidth=0.5)

        ax.plot(np.array(frames)*1000, np.array(method_area) * 1e-6, 'o', color='orange', markersize=3, label='Area')
        ax.plot(np.array(frames)*1000, np.array(method_area) * 1e-6, '-', color='black', linewidth=0.5)

        ax.plot(np.array(frames)*1000, method_ccm, 'o', color='green', markersize=3, label='CCM')
        ax.plot(np.array(frames)*1000, method_ccm, '-', color='black', linewidth=0.5)

        

        #ax.set_xlim(0, 450)
        ax.set_ylim(0, 12)

        ax.set_xlabel('Crack length [mm]')
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
    plt.savefig("reduced_fracture_toughness_plot_including_area_method.png", dpi=300)
    #plt.show()

def plot_excluding_area_method():
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))  # One figure with 3 vertical subplots
    for sample_number in range(1,4):
        frames=d5045.crack_tip_length(sample_number)
        method_d5045=d5045.fracture_toughnesses(sample_number)
        #method_e399=e399.fracture_toughnesses(sample_number)
        method_area=area.fracture_toughnesses(sample_number)[:,0]
        method_ccm=ccm.fracture_toughnesses(sample_number)[0]

        ax = axs[sample_number - 1]  # Index starts from 0
    
        ax.plot(frames, method_d5045, 'o', color='blue', markersize=3, label='D5045')
        ax.plot(frames, method_d5045, '-', color='black', linewidth=0.5)

        #ax.plot(frames, np.array(method_e399) * 1e-6, 'o', color='red', markersize=3, label='E399')
        #ax.plot(frames, np.array(method_e399) * 1e-6, '-', color='black', linewidth=0.5)

        #ax.plot(frames, np.array(method_area) * 1e-6, 'o', color='orange', markersize=3, label='Area')
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
    plt.savefig("fracture_toughness_plot_excluding_area_method.png", dpi=300)
    #plt.show()




def averages():
    fig, axs = plt.subplots(3, 1, figsize=(8, 8))  # One figure with 3 vertical subplots
    ax1=axs[0]
    ax2=axs[1]
    ax3=axs[2]

    frames=d5045.crack_tip_length(1)
    average_method_d5045=(np.array(d5045.fracture_toughnesses(1))+np.array(d5045.fracture_toughnesses(2))+np.array(d5045.fracture_toughnesses(3)))/3
    #average_method_e399=(np.array(e399.fracture_toughnesses(1))+np.array(e399.fracture_toughnesses(2))+np.array(e399.fracture_toughnesses(3)))/3*1e-6
    average_method_area=(np.array(area.fracture_toughnesses(1)[:,0])+np.array(area.fracture_toughnesses(2)[:,0])+np.array(area.fracture_toughnesses(3)[:,0]))/3*1e-6
    average_method_ccm=(np.array(ccm.fracture_toughnesses(1)[0])+np.array(ccm.fracture_toughnesses(2)[0])+np.array(ccm.fracture_toughnesses(3)[0]))/3
    
    
    standard_deviation_d5045=np.sqrt(((average_method_d5045-np.array(d5045.fracture_toughnesses(1)))**2+
                                      (average_method_d5045-np.array(d5045.fracture_toughnesses(2)))**2+
                                      (average_method_d5045-np.array(d5045.fracture_toughnesses(3)))**2)/2)
    #standard_deviation_e399=np.sqrt(((average_method_e399-np.array(e399.fracture_toughnesses(1))*1e-6)**2+(average_method_e399-np.array(e399.fracture_toughnesses(2))*1e-6)**2)/3)
    standard_deviation_ccm=np.sqrt(((average_method_ccm-np.array(ccm.fracture_toughnesses(1)[0]))**2+
                                    (average_method_ccm-np.array(ccm.fracture_toughnesses(2)[0]))**2+
                                    (average_method_ccm-np.array(ccm.fracture_toughnesses(3)[0]))**2)/2)
    standard_deviation_area=np.sqrt(((average_method_area-np.array(area.fracture_toughnesses(1)[:,0])*1e-6)**2+
                                     (average_method_area-np.array(area.fracture_toughnesses(2)[:,0])*1e-6)**2+
                                     (average_method_area-np.array(area.fracture_toughnesses(3)[:,0])*1e-6)**2)/2)

    ax1.plot(np.array(frames)*1000, average_method_d5045, 'o', color='blue', markersize=3, label='D5045 & E399')
    ax1.plot(np.array(frames)*1000, average_method_d5045, '-', color='black', linewidth=0.5)

    #ax1.plot(frames, average_method_e399, 'o', color='red', markersize=3, label='E399')
    #ax1.plot(frames, average_method_e399, '-', color='black', linewidth=0.5)

    ax1.plot(np.array(frames)*1000, average_method_area, 'o', color='orange', markersize=3, label='AM')
    ax1.plot(np.array(frames)*1000, average_method_area, '-', color='black', linewidth=0.5)

    ax1.plot(np.array(frames)*1000, average_method_ccm, 'o', color='green', markersize=3, label='CCM')
    ax1.plot(np.array(frames)*1000, average_method_ccm, '-', color='black', linewidth=0.5)

    ax1.set_ylim(0, 13)

    ax1.set_xlabel('Crack length [mm]')
    ax1.set_ylabel(r'Fracture toughness [MPa$\sqrt{\mathrm{m}}$]')
    ax1.set_title(f'Average values')

    ax1.minorticks_on()
    ax1.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax1.xaxis.set_major_locator(MaxNLocator(nbins=10))
    ax1.yaxis.set_major_locator(MaxNLocator(nbins=10))
    ax1.grid(True, which='both', linewidth=0.5, alpha=0.7)
    ax1.legend()
    
    ax2.plot(np.array(frames)*1000, standard_deviation_d5045, 'o', color='blue', markersize=3, label='D5045 & E399')
    ax2.plot(np.array(frames)*1000, standard_deviation_d5045, '-', color='black', linewidth=0.5)

    #ax2.plot(frames, standard_deviation_e399, 'o', color='red', markersize=3, label='E399')
    #ax2.plot(frames, standard_deviation_e399, '-', color='black', linewidth=0.5)

    ax2.plot(np.array(frames)*1000, standard_deviation_area, 'o', color='orange', markersize=3, label='AM')
    ax2.plot(np.array(frames)*1000, standard_deviation_area, '-', color='black', linewidth=0.5)

    ax2.plot(np.array(frames)*1000, standard_deviation_ccm, 'o', color='green', markersize=3, label='CCM')
    ax2.plot(np.array(frames)*1000, standard_deviation_ccm, '-', color='black', linewidth=0.5)

    ax2.set_ylim(0, 7)
    ax2.set_xlabel('Crack length [mm]')
    ax2.set_title('Standard deviation')
    ax2.set_ylabel(r'Standard deviation [MPa$\sqrt{\mathrm{m}}$]')

    ax2.minorticks_on()
    ax2.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax2.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax2.xaxis.set_major_locator(MaxNLocator(nbins=10))
    ax2.yaxis.set_major_locator(MaxNLocator(nbins=10))
    ax2.grid(True, which='both', linewidth=0.5, alpha=0.7)
    ax2.legend()

    ax3.plot(np.array(frames)*1000, standard_deviation_d5045, 'o', color='blue', markersize=3, label='D5045 & E399')
    ax3.plot(np.array(frames)*1000, standard_deviation_d5045, '-', color='black', linewidth=0.5)

    ax3.plot(np.array(frames)*1000, standard_deviation_ccm, 'o', color='green', markersize=3, label='CCM')
    ax3.plot(np.array(frames)*1000, standard_deviation_ccm, '-', color='black', linewidth=0.5)

    #ax3.set_ylim(0, 10)
    ax3.set_xlabel('Crack length [mm]')
    ax3.set_title('Standard deviation excluding the area method')
    ax3.set_ylabel(r'Standard deviation [MPa$\sqrt{\mathrm{m}}$]')

    ax3.minorticks_on()
    ax3.xaxis.set_minor_locator(AutoMinorLocator(4))
    ax3.yaxis.set_minor_locator(AutoMinorLocator(4))
    ax3.xaxis.set_major_locator(MaxNLocator(nbins=10))
    ax3.yaxis.set_major_locator(MaxNLocator(nbins=10))
    ax3.grid(True, which='both', linewidth=0.5, alpha=0.7)
    ax3.legend()
    
    plt.tight_layout()
    plt.savefig("averages_and_deviations.png", dpi=300)
    #plt.show()

def absolute_differences():
    fig, axs = plt.subplots(1, 1, figsize=(8, 8))  # One figure with 3 vertical subplots
    
    frames=d5045.crack_tip_length(1)
    average_method_d5045=(np.array(d5045.fracture_toughnesses(1))+np.array(d5045.fracture_toughnesses(2))+np.array(d5045.fracture_toughnesses(3)))/3
    #average_method_e399=1e-6*(np.array(e399.fracture_toughnesses(1))+np.array(e399.fracture_toughnesses(2))+np.array(e399.fracture_toughnesses(3)))/3
    #average_method_area=(np.array(area.fracture_toughnesses(1)[:,0])+np.array(area.fracture_toughnesses(2)[:,0])+np.array(area.fracture_toughnesses(3)[:,0]))/3
    average_method_ccm=(np.array(ccm.fracture_toughnesses(1)[0])+np.array(ccm.fracture_toughnesses(2)[0])+np.array(ccm.fracture_toughnesses(3)[0]))/3
    
    #differences_1=abs(average_method_d5045-average_method_e399)
    differences_2=abs(average_method_d5045-average_method_ccm)
    #differences_3=abs(average_method_e399-average_method_ccm)


    #axs.plot(frames, differences_1, 'o', color='blue', markersize=3, label='D5045 vs. E399')
    #axs.plot(frames, differences_1, '-', color='black', linewidth=0.5)

    axs.plot(frames, differences_2, 'o', color='red', markersize=3, label='D5045 vs. CCM')
    axs.plot(frames, differences_2, '-', color='black', linewidth=0.5)

    #axs.plot(frames, differences_3, 'o', color='green', markersize=3, label='E399 vs. CCM')
    #axs.plot(frames, differences_3, '-', color='black', linewidth=0.5)

    axs.set_xlabel('Frame number')
    axs.set_ylabel(r'Fracture toughness [MPa$\sqrt{\mathrm{m}}$]')
    axs.set_title(f'Differences')

    axs.minorticks_on()
    axs.xaxis.set_minor_locator(AutoMinorLocator(4))
    axs.yaxis.set_minor_locator(AutoMinorLocator(4))
    axs.xaxis.set_major_locator(MaxNLocator(nbins=10))
    axs.yaxis.set_major_locator(MaxNLocator(nbins=10))
    axs.grid(True, which='both', linewidth=0.5, alpha=0.7)
    axs.legend()

    plt.tight_layout()
    plt.savefig("differences.png", dpi=300)
    #plt.show()

def percentage():
    fig, axs = plt.subplots(1, 1, figsize=(8, 8))  # One figure with 3 vertical subplots
    
    frames=d5045.crack_tip_length(1)
    average_method_d5045=(np.array(d5045.fracture_toughnesses(1))+np.array(d5045.fracture_toughnesses(2))+np.array(d5045.fracture_toughnesses(3)))/3
    #average_method_e399=1e-6*(np.array(e399.fracture_toughnesses(1))+np.array(e399.fracture_toughnesses(2))+np.array(e399.fracture_toughnesses(3)))/3
    # average_method_area=(np.array(area.fracture_toughnesses(1)[:,0])+np.array(area.fracture_toughnesses(2)[:,0])+np.array(area.fracture_toughnesses(3)[:,0]))/3
    average_method_ccm=(np.array(ccm.fracture_toughnesses(1)[0])+np.array(ccm.fracture_toughnesses(2)[0])+np.array(ccm.fracture_toughnesses(3)[0]))/3
    
    #perentage_1=abs(100*(average_method_d5045-average_method_e399)/average_method_e399)
    #percentage_2=abs(100*(average_method_d5045-average_method_e399)/average_method_e399)
    # differences_3=abs(average_method_e399-average_method_ccm)


    #axs.plot(frames, perentage_1, 'o', color='blue', markersize=3, label='D5045 of E399')
    #axs.plot(frames, perentage_1, '-', color='black', linewidth=0.5)

    # axs.plot(frames, percentage_2, 'o', color='red', markersize=3, label='D5045 vs. CCM')
    # axs.plot(frames, percentage_2, '-', color='black', linewidth=0.5)

    # axs.plot(frames, differences_3, 'o', color='green', markersize=3, label='E399 vs. CCM')
    # axs.plot(frames, differences_3, '-', color='black', linewidth=0.5)

    axs.set_xlabel('Frame number')
    axs.set_ylabel('Percentage [%]')
    axs.set_title(f'D5045 percentage of E399')

    axs.minorticks_on()
    axs.xaxis.set_minor_locator(AutoMinorLocator(4))
    axs.yaxis.set_minor_locator(AutoMinorLocator(4))
    axs.xaxis.set_major_locator(MaxNLocator(nbins=10))
    axs.yaxis.set_major_locator(MaxNLocator(nbins=10))
    axs.grid(True, which='both', linewidth=0.5, alpha=0.7)
    axs.legend()

    plt.tight_layout()
    plt.savefig("percentage.png", dpi=300)

    # frame_index = 150
    # if frame_index in frames:
    #     index = list(frames).index(frame_index)
    #     print(f"E399 at frame {frame_index}: {average_method_e399[index]}")
    #     print(f"D5045 at frame {frame_index}: {average_method_d5045[index]}")
    # else:
    #     print(f"Frame {frame_index} is not in the list of frames.")


#plot_excluding_area_method()
#plot_including_area_method()
reduced_plot_including_area_method()
#average_excluding_area_method()
#absolute_differences()
#percentage()
averages()





