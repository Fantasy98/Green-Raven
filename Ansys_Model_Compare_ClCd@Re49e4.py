####Part 1 Package used 
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd

#####Part 2 Document and Data Naming 

# General 

Airfoil = ['MH61','MH104']
# Angle_of_Attack = [-4,-2,0,2,4,6,8,10,12]
Angle_of_Attack = [-2,0,2,4,6,8,10]
Reynolds_Number_MH61 = [342293,492902,958421,1341790]
Reynolds_Number_MH104 = [2081144,2327595]

Data_kind =['Cp','Cf']

Model_Name = ["Spalart-Allmaras","K-omega SST","K-kl-omega","Transition SST"]
Sheet_Name = ['MH61_Ansys',"MH61_Xfoil","MH104_Ansys","MH104_Xfoil"]
dict_type = {"Cl":np.float64,"Cd":np.float64,"Length(m)":np.float64}

io_fig_compare = "/Users/wangyuning/Desktop/LowRe/Compare_Result/{}"
excel_name = 'Cruise=20.xlsx'


### Load the excel data
df = pd.read_excel(excel_name,sheet_name=Sheet_Name[0],header=1,dtype=dict_type)
df_Xfoil = pd.read_excel(excel_name,sheet_name=Sheet_Name[1],header=1,dtype=dict_type)


df_Cl_036m= df['Cl'].loc[df['Length(m)']==0.36]
Xfoil_Cl_036m= df_Xfoil['Cl'].loc[df['Length(m)']==0.36].values


df_Cd_036m= df['Cd'].loc[df['Length(m)']==0.36]
Xfoil_Cd_036m= df_Xfoil['Cd'].loc[df['Length(m)']==0.36].values


### Store all the data from dataframe into a matrix
Cl = np.zeros((len(Model_Name),len(Angle_of_Attack)))
Cd = np.zeros((len(Model_Name),len(Angle_of_Attack)))

for name in np.arange(len(Model_Name)): 
    Cl[name,:] = df_Cl_036m.loc[df['Turbulence Model'] == Model_Name[name]].values
    Cd[name,:] = df_Cd_036m.loc[df['Turbulence Model'] == Model_Name[name]].values

Model_Name = ["Spalart-Allmaras","k-omega SST","k-kl-omega","Transition SST"]
######Figure 1 Cl vs alpha


n= 0 
plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_Cl_@Re49e4"
plt.xlabel('Angle of Attack (deg)')
plt.ylabel("Lift Coefficient")
plt.grid()
for name in np.arange(len(Model_Name)): 
    plt.plot(Angle_of_Attack,Cl[name,:],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Model_Name[name]))
plt.plot(Angle_of_Attack,Xfoil_Cl_036m,'-o',markersize = 3.5, lw = 1.5,label = "Xfoil")

plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n+=1

plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_Cd_@Re49e4"
plt.xlabel('Angle of Attack (deg)')
plt.ylabel("Drag Coefficient")
plt.grid()
for name in np.arange(len(Model_Name)): 
    plt.plot(Angle_of_Attack,Cd[name,:],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Model_Name[name]))
plt.plot(Angle_of_Attack,Xfoil_Cd_036m,'-o',markersize = 3.5, lw = 1.5,label = "Xfoil")


plt.legend()
plt.savefig(io_fig_compare.format(tlt))
n+=1


n +=1
plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_ClCd_@Re49e4"
plt.xlabel('Angle of Attack (deg)')
plt.ylabel("Cl/Cd")
plt.grid()
for name in np.arange(len(Model_Name)): 
    plt.plot(Angle_of_Attack,Cl[name,:]/Cd[name,:],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Model_Name[name]))

plt.plot(Angle_of_Attack,Xfoil_Cl_036m/Xfoil_Cd_036m,'-o',markersize = 3.5, lw = 1.5,label = "Xfoil")

plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n +=1

plt.figure(n)
tlt = "Ansys_MH61_ModelCompare_Cl_Cd_@Re49e4"
plt.xlabel('Drag Coefficient')
plt.ylabel("Lift Coefficient")
plt.grid()
for name in np.arange(len(Model_Name)): 
    plt.plot(Cd[name,:],Cl[name,:],'-o',markersize = 3.5, lw = 1.5,label = "{}".format(Model_Name[name]))
plt.plot(Xfoil_Cd_036m,Xfoil_Cl_036m,'-o',markersize = 3.5, lw = 1.5,label = "Xfoil")

plt.legend()
plt.savefig(io_fig_compare.format(tlt))

n +=1


Cl_std = np.std(Cl,axis=0)
Cd_std = np.std(Cd,axis=0)
print(Cl)
print(Cl_std)
print(Cd_std)
