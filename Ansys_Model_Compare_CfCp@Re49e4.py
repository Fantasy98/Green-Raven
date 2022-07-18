
from cProfile import label
from curses import A_ALTCHARSET
from re import A
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
import Load_Function as lf

# General 
Airfoil = ['MH61','MH104']
Angle_of_Attack = [-2,0,2,4,6,8,10]
Reynolds_Number_MH61 = ['27e4','39e4','76e4','11e5']
Data_kind =['Cp','Cf']


#For Ansys
Fluent_Model = ["1EQN","2EQN","3EQN","4EQN"]
Model_Name = ["Spalart-Allmaras","K-omega SST","K-kl-omega","Transition SST"]
Sides = ['up','low']

io_fig_compare = "/Users/wangyuning/Desktop/LowRe/Compare_Result/{}"
# Format : {Ansys/Xfoil}_{Airfoil}_{which coefficient}_{w.r.t what coefficient/ factor}@{under what situation}

n = 0 
plt.figure(n,dpi=120)
plt.xlabel("location (x/c)")
plt.ylabel("Pressure Coefficient")
plt.grid()
tlt = "Ansys_MH61_ModelCompare_Cp_@Re49e46deg"
for model in np.arange(len(Fluent_Model)):
    Upper,Lower = lf.Load_Cp_Ansys(Model=Fluent_Model[model],Airfoil="MH61",Reynolds_number="49e4",Alpha=6)
    X,Cp = lf.Merge_Cp(Upper,Lower)
    plt.plot(X,Cp,'.',markersize = 1 ,label="Model:{}".format( Model_Name[model]))
plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n += 1 

plt.figure(n,dpi=120)
plt.xlabel("location (x/c)")
plt.ylabel("Skin Friction Coefficient")
plt.grid()
plt.ylim([0,0.015])
tlt = "Ansys_MH61_ModelCompare_Cf_up_@Re49e46deg"
for model in np.arange(len(Fluent_Model)):
    Upper,Lower = lf.Load_Cf_Ansys(Model=Fluent_Model[model],Airfoil="MH61",Reynolds_number="49e4",Alpha=6)
    
    plt.plot(Upper[0,:],Upper[1,:],'-',markersize = 1 ,label="Model:{}".format( Model_Name[model]))
plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n += 1

plt.figure(n,dpi=120)
plt.xlabel("location (x/c)")
plt.ylabel("Skin Friction Coefficient")
plt.grid()
plt.ylim([0,0.015])
tlt = "Ansys_MH61_ModelCompare_Cf_low_@Re49e46deg"
for model in np.arange(len(Fluent_Model)):
    Upper,Lower = lf.Load_Cf_Ansys(Model=Fluent_Model[model],Airfoil="MH61",Reynolds_number="49e4",Alpha=6)
    
    plt.plot(Lower[0,:],Lower[1,:],'-',markersize = 1 ,label="Model:{}".format( Model_Name[model] ))
plt.legend()
plt.savefig(io_fig_compare.format(tlt))


######### Plot Cf distribution at each angle of attack  
 
for aoa in Angle_of_Attack :
    n+= 1
    plt.figure(n)
    plt.xlabel("location (x/c)")
    plt.ylabel("Skin Friction Coefficient")
    plt.grid()
    plt.ylim([0,0.015])
    plt.xlim([0,1])
    for model in np.arange(len(Fluent_Model)) : 
       
        Upper,Lower = lf.Load_Cf_Ansys(Model=Fluent_Model[model],Airfoil="MH61",Reynolds_number="49e4",Alpha=aoa)
        scale = Upper[0,-1]
        Upper_X = Upper[0,:]/Upper[0,-1]
        plt.plot(Upper_X,Upper[1,:],'-',markersize = 1 ,label="Model:{}".format( Model_Name[model]))
    X_Xfoil ,Cf_Xfoil = lf.Load_Cf_Xfoil(Airfoil='MH61',Reynolds_number="39e4",Alpha=aoa)
    plt.plot(X_Xfoil,Cf_Xfoil,'-',label="Xfoil")  
    tlt = "Ansys_MH61_ModelCompare_Cf_up_@Re49e4{}deg".format(aoa)
    plt.legend()
    plt.savefig(io_fig_compare.format(tlt))


########### Plot Cp at each angle of attack

for aoa in Angle_of_Attack :
    n+= 1
    plt.figure(n)
    plt.xlabel("location (x/c)")
    plt.ylabel("Pressure Coefficient")
    plt.grid()
  
    for model in np.arange(len(Fluent_Model))  : 
        Upper,Lower = lf.Load_Cp_Ansys(Model=Fluent_Model[model],Airfoil="MH61",Reynolds_number="49e4",Alpha=aoa)
        X,Cp = lf.Merge_Cp(Upper,Lower=Lower)
        plt.plot(X/np.max(X),Cp,'o',markersize = 0.8 ,label="Model:{}".format(Model_Name[model]))
    X_Xfoil,Cp_Xfoil = lf.Load_Cp_Xfoil(Airfoil='MH61',Reynolds_number="49e4",Alpha=aoa)
    print('Plotting alpha = {}'.format(aoa))
    plt.plot(X_Xfoil,Cp_Xfoil,'-',lw=1.2,label="Xfoil")
    tlt = "Ansys_MH61_ModelCompare_Cp_@Re49e4{}deg".format(aoa)
    plt.legend()
    plt.savefig(io_fig_compare.format(tlt))
