####Part 1 Package used 
import io
from re import U
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
import Load_Function as lf

#####Part 2 Document and Data Naming 

#######################################################################
####Part 1  Prepare
#######################################################################

# General 
Airfoil = 'MH104'
# Angle_of_Attack = [-4,-2,0,2,4,6,8,10,12]
Angle_of_Attack = [-2,0,2,4,6,8,10]
# Reynolds_Number_MH61 = ['27e4','39e4','76e4','11e5']
Reynolds_Number_MH104 = ['21e5','23e5']

font_dict = {'size':16}
labels = ['$2.08x10^6$','$2.33x10^6$']
turbulent_model = "3EQN"
io_fig_ansys = "/Users/wangyuning/Desktop/LowRe/Ansys_Result/{}"

#######################################################################
####Part 2  Plot Cp at all angle of attack for each Reynolds number
#######################################################################
n = 0
for Re in Reynolds_Number_MH104:
    
    plt.figure(n)
    plt.xlabel('x/c',fontdict=font_dict)
    plt.ylabel('Pressure Coefficient',fontdict=font_dict)
    # plt.ylim([-4,1])
    plt.xlim([0,1])
    plt.grid()
    tlt = "Ansys_MH104_Cp@Re{}".format(Re)
    for aoa in Angle_of_Attack[1:-2]:
        Upper, Lower = lf.Load_Cp_Ansys(Model=turbulent_model,Airfoil=Airfoil,Reynolds_number=Re,Alpha=aoa)
        X, Cp = lf.Merge_Cp(Upper=Upper,Lower=Lower)
        X = X/np.max(X)
        plt.plot(X,Cp,'o',markersize = 1.5,label = r"$\alpha$={}".format(aoa))
    plt.legend()
    plt.savefig(io_fig_ansys.format(tlt))
    n+= 1 


#######################################################################
####Part 2  Plot Cp at all Reynolds number for each angle of attack
#######################################################################

for aoa in Angle_of_Attack:
    
    plt.figure(n)
    plt.xlabel('x/c',fontdict=font_dict)
    plt.ylabel('Pressure Coefficient',fontdict=font_dict)
    plt.xlim([0,1])
    plt.grid()
    tlt = "Ansys_MH104_Cp@AOA={}".format(aoa)
    for Re in np.arange(len(Reynolds_Number_MH104)):
        
        Upper, Lower = lf.Load_Cp_Ansys(Model=turbulent_model,Airfoil=Airfoil,Reynolds_number= Reynolds_Number_MH104[Re],Alpha=aoa)
        
        X, Cp = lf.Merge_Cp(Upper=Upper,Lower=Lower)  
        X = X/np.max(X)          
        plt.plot(X,Cp,'o',markersize = 1.5,label = "Re={}".format(labels[Re]))
    plt.legend()
    plt.savefig(io_fig_ansys.format(tlt))
    n+= 1 
