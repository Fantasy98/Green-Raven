from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
#######################################################################
####Part 1  Prepare
#######################################################################
# Basic data
Airfoil = 'MH61'
Angle_of_Attack = [-2,0,2,4,6,8,10]
Reynolds_Number_MH61 = [342293,492902,958421,1341790]
Length_range = [0.25,0.36,0.7,0.98]


# Set for loading excel 
Model_Name = ["Spalart-Allmaras","K-omega SST","K-kl-omega","Transition SST"]

Sheet_Name = ['MH61_Ansys',"MH61_Xfoil"]

dict_type = {"Cl":np.float64,"Cd":np.float64,"Length(m)":np.float64}

excel_name = 'Cruise=20.xlsx'

# Where to savefig()
io_fig_ansys = "/Users/wangyuning/Desktop/LowRe/Ansys_Result/{}"



#######################################################################
####Part 2 Load and store Data
#######################################################################

### Load the excel data of ANSYS and Xfoil results , 3EQN only
df = pd.read_excel(excel_name,sheet_name=Sheet_Name[0],header=1,dtype=dict_type)
df = df.dropna()
Cl_Ansys = np.zeros((len(Length_range),len(Angle_of_Attack)))
Cd_Ansys = np.zeros((len(Length_range),len(Angle_of_Attack)))


df_3EQN = df.loc[df['Turbulence Model'] == Model_Name[2]]

for le in np.arange(len(Length_range)):

    print('Xfoil Collecting Length = {} Re = {}'.format(Length_range[le],Reynolds_Number_MH61[le]))
    df_len=df_3EQN.loc[ df_3EQN['Length(m)'] == Length_range[le] ]
    Cl_Ansys[le,:] = df_len['Cl'].values
    Cd_Ansys[le,:] = df_len['Cd'].values




df_Xfoil = pd.read_excel(excel_name,sheet_name=Sheet_Name[1],header=1,dtype=dict_type)

Cl_Xfoil = np.zeros((len(Length_range),len(Angle_of_Attack)))
Cd_Xfoil = np.zeros((len(Length_range),len(Angle_of_Attack)))

for le in np.arange(len(Length_range)):
    print('Xfoil Collecting Length = {} Re = {}'.format(Length_range[le],Reynolds_Number_MH61[le]))
    Cl_Xfoil[le,:] = df_Xfoil['Cl'].loc[df_Xfoil['Length(m)'] == Length_range[le]]
    Cd_Xfoil[le,:] = df_Xfoil['Cd'].loc[df_Xfoil['Length(m)'] == Length_range[le]]

std_Cl = np.std(Cl_Ansys,axis=0)
std_Cd = np.std(Cd_Ansys,axis=0)
print("MH61 Std of Cl ANSYS {}".format(std_Cl))
print("MH61 Std of Cd ANSYS {}".format(std_Cd))


#######################################################################
####Part 3 Plot and save figures of Cl Cd ANSYS
#######################################################################

font_dict = {'size':16}
marker = ["o-",'s-','D-','v-']
n= 0 
labels = ['$0.34x10^6$',"$0.49x10^6$",'$0.96x10^6$','$1.34x10^6$']



plt.figure(n)
plt.grid()
plt.xlabel('Angle of Attack (deg)',font_dict)
plt.ylabel('Lift Coefficient',font_dict)
tlt = "Ansys_MH61_Cl@Re34e4-13e5"
for re in np.arange(len(Reynolds_Number_MH61)):
    plt.plot(Angle_of_Attack, Cl_Ansys[re,:],marker[re],lw=0.75,markersize = 8.5,label="Re={}".format(labels[re]))
plt.legend()
print('Saving fig {}'.format(tlt))
plt.savefig(io_fig_ansys.format(tlt))
n+=1



plt.figure(n)
plt.grid()
plt.xlabel('Angle of Attack (deg)',font_dict)
plt.ylabel('Drag Coefficient',font_dict)
tlt = "Ansys_MH61_Cd@Re34e4-13e5"
for re in np.arange(len(Reynolds_Number_MH61)):
    plt.plot(Angle_of_Attack, Cd_Ansys[re,:],marker[re],lw=0.75,markersize = 8.5,label="Re={}".format(labels[re]))
plt.legend()
print('Saving fig {}'.format(tlt))
plt.savefig(io_fig_ansys.format(tlt))
n+=1





plt.figure(n)
plt.grid()
plt.xlabel('Drag Coefficient',font_dict)
plt.ylabel('Lift Coefficient',font_dict)
tlt = "Ansys_MH61_Cl_Cd@Re34e4-13e5"
for re in np.arange(len(Reynolds_Number_MH61)):
    plt.plot(Cd_Ansys[re,:], Cl_Ansys[re,:],marker[re],lw=0.75,markersize = 8.5,label="Re={}".format(labels[re]))
plt.legend()
print('Saving fig {}'.format(tlt))
plt.savefig(io_fig_ansys.format(tlt))
n+=1



plt.figure(n)
plt.grid()
plt.xlabel('Angle of Attack (deg)',font_dict)
plt.ylabel('Lift-to-Drag Coefficient',font_dict)
tlt = "Ansys_MH61_ClCd@Re34e4-13e5"
for re in np.arange(len(Reynolds_Number_MH61)):
    plt.plot(Angle_of_Attack, Cl_Ansys[re,:]/Cd_Ansys[re,:],marker[re],lw=0.75,markersize = 8.5,label="Re={}".format(labels[re]))
plt.legend()
print('Saving fig {}'.format(tlt))
plt.savefig(io_fig_ansys.format(tlt))
n+=1

#######################################################################
####Part 34 Plot and save figures of Cl Cd difference between ANSYS & XFOIL
#######################################################################
print("Check Cl matrix shape : {}".format(Cl_Ansys.shape == Cl_Xfoil.shape))
print("Check Cd matrix shape : {}".format(Cd_Ansys.shape == Cd_Xfoil.shape))

Cl_diff = np.abs((Cl_Ansys - Cl_Xfoil)/Cl_Ansys)
Cd_diff = np.abs((Cd_Ansys - Cd_Xfoil)/Cd_Ansys)


plt.figure(n)
plt.xlabel('Angle of Attack (deg)',fontdict=font_dict)
plt.ylabel('Difference of Cl',fontdict=font_dict)
plt.grid()
tlt = "Ansys_MH61_Diff_Cl_Xfoil_Ansys"
for re in np.arange(len(Reynolds_Number_MH61)):
    plt.plot(Angle_of_Attack,Cl_diff[re,:],marker[re],lw=0.75,markersize = 8.5,label = "Re={}".format(labels[re]))
plt.legend()
print('Saving fig {}'.format(tlt))
plt.savefig(io_fig_ansys.format(tlt))
n+=1 


plt.figure(n)
plt.xlabel('Angle of Attack (deg)',fontdict=font_dict)
plt.ylabel('Difference of Cd',fontdict=font_dict)
plt.grid()
tlt = "Ansys_MH61_Diff_Cd_Xfoil_Ansys"
for re in np.arange(len(Reynolds_Number_MH61)):
    plt.plot(Angle_of_Attack,Cd_diff[re,:],marker[re],lw=0.75,markersize = 8.5,label = "Re={}".format(labels[re]))
plt.legend()
print('Saving fig {}'.format(tlt))
plt.savefig(io_fig_ansys.format(tlt))
n+=1 
