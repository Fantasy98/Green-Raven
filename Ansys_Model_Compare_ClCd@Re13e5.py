####Part 1 Package used 
from cProfile import label
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd


Angle_of_Attack = [-4,-2,0,2,4,6,8,10,12]
Fluent_Model = ["Spalart-Allmaras","K-omega SST","K-kl-omega","Transition SST",'Xfoil']
Model_Name = ["Spalart-Allmaras","K-omega SST","K-kl-omega","Transition SST"]

io_fig_compare = "/Users/wangyuning/Desktop/LowRe/Compare_Result/{}"

Sheet_Name = ["Spalart-Allmaras Model","K-Omega SST Model","k-kl-SST Model","Transition SST Model","Xfoil"]
dytype_dict ={'Cl':np.float64,"Cd":np.float64,"Cm":np.float64}

### Create a matrix for saving Cl Cd Cm size = (5*9) 
# The last row is for xfoil !!! 
Cl = np.zeros((len(Fluent_Model),len(Angle_of_Attack)))

Cd = np.zeros((len(Fluent_Model),len(Angle_of_Attack))) 
Cm = np.zeros((len(Fluent_Model),len(Angle_of_Attack)))

for name in np.arange( len(Sheet_Name)): 
    
    df = pd.read_excel("MH61_14-18.xlsx",sheet_name=Sheet_Name[name],header=1,dtype=dytype_dict)
    
    Cl[name,:] = df['Cl'].loc[df["Re"] == 1095584].values
    
    Cd[name,:] = df['Cd'].loc[df["Re"] == 1095584].values
    Cm[name,:] = df['Cm'].loc[df["Re"] == 1095584].values



n= 0 
plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_Cl_@Re11e5"
plt.xlabel('Angle of Attack (deg)')
plt.ylabel("Lift Coefficient")
plt.grid()
for name in np.arange(len(Sheet_Name)): 
    plt.plot(Angle_of_Attack[1:-1],0.8*Cl[name,1:-1],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Fluent_Model[name]))
plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n+=1

plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_Cd_@Re11e5"
plt.xlabel('Angle of Attack (deg)')
plt.ylabel("Drag Coefficient")
plt.grid()
for name in np.arange(len(Sheet_Name)): 
    plt.plot(Angle_of_Attack[1:-1],0.8*Cd[name,1:-1],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Fluent_Model[name]))
plt.legend()
plt.savefig(io_fig_compare.format(tlt))
n+=1

plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_Cm_@Re11e5"
plt.xlabel('Angle of Attack (deg)')
plt.ylabel("Momentum Coefficient")
plt.grid()
for name in np.arange(len(Sheet_Name)): 
    plt.plot(Angle_of_Attack[1:-1],0.8*Cm[name,1:-1],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Fluent_Model[name]))
plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n +=1

plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_ClCd_@Re11e5"
plt.xlabel('Angle of Attack (deg)')
plt.ylabel("Cl/Cd")
plt.grid()
for name in np.arange(len(Sheet_Name)): 
    plt.plot(Angle_of_Attack[1:-1],Cl[name,1:-1]/Cd[name,1:-1],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Fluent_Model[name]))
plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n +=1

plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_Cl_Cd_@Re11e5"
plt.xlabel('Drag Coefficient')
plt.ylabel("Lift Coefficient")
plt.grid()
for name in np.arange(len(Sheet_Name)): 
    plt.plot(0.8*Cd[name,1:-1],0.8*Cl[name,1:-1],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Fluent_Model[name]))
plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n +=1

Cl_std = np.std(Cl,axis=0)
Cd_std = np.std(Cd,axis=0)
print(Cl_std)
print(Cd_std)