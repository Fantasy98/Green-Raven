####Part 1 Package used 
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
import Load_Function as lf

#####Part 2 Document and Data Naming 

# General 
Airfoil = ['MH61','MH104']
# Angle_of_Attack = [-4,-2,0,2,4,6,8,10,12]
Angle_of_Attack = [-2,0,2,4,6,8,10]
# Reynolds_Number_MH61 = ['27e4','39e4','76e4','11e5']
Reynolds_Number_MH61 = ['34e4','49e4','95e4','13e5']
Reynolds_Number_MH61 = [342293,492902,958421,1341790]
# Reynolds_Number_MH104 = ['16e5','18e5']
Reynolds_Number_MH104 = ['21e5','23e5']
Reynolds_Number_MH104 = [2081144,2327595]
Data_kind =['Cp','Cf']


#For Ansys
Fluent_Model = ["1EQN","2EQN","3EQN","4EQN"]
Fluent_Model = ["Spalart-Allmaras","K-omega SST","K-kl-omega","Transition SST"]
Model_Name = ["Spalart-Allmaras","k-omega SST","k-kl-omega","Transition SST"]

Sides = ['up','low']

#For numerical study
Numerical= ['Grid_Convergence','Domain_Examination','Time_Scale_Factor','Turbulence_Intensity']
grid_convergence = ['1e-1','25e-3','10e-3','5e-3']
domain_exam = ['375e-2','75e-1','15','30']
time_scale_factor = ['1','1e-1','1e-2','1e-3','1e-4','1e-5']
Turbulence_Intensity = ['1','3','5']


##2.1 Load From the xfoil
io_xfoil  = "/Users/wangyuning/Desktop/LowRe/Xfoil/{}"
title_xfoil = 'Xfoil_{}_{}_Re{}{}deg.txt'  
#For example : Xfoil_MH61_Cp_Re11e52deg.txt
dict_xfoil = io_xfoil.format(title_xfoil)

##2.2 Load From Ansys Flunet  
io_ansys  = "/Users/wangyuning/Desktop/LowRe/Ansys/{}/{}"
title_ansys = '{}_{}_{}_{}Re{}{}deg.txt'
#For example : 4EQN_Cf_up_MH61Re12e56deg.txt
dict_ansys = io_ansys.format(Fluent_Model[-1] ,title_ansys)

## 2.3 Numercial Study 
io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/{}/{}"
title_grid = "{}_{}_size{}.txt"
#For example Cp_up_size25e-3.txt
dict_grid = io_numerical.format(Numerical[0],title_grid)

title_domain = "{}_{}_R{}.txt"
#For example Cp_up_R75e-1.txt
dict_domian = io_numerical.format(Numerical[1],title_domain)

title_timescale = "{}_{}_T={}.txt"
#for exampe Cp_low_T=1e-3.txt
dict_timescale = io_numerical.format(Numerical[2],title_timescale)

title_intensity = "{}_{}_I={}.txt"
#For example : Cp_up_I=1.txt
dict_intensity = io_numerical.format(Numerical[-1],title_intensity)

###Part 3 Loading the different type of document

##3.1 For Xfoil 

##3.1.1 Load Cf file
with open(dict_xfoil,'r') as f: 
    read = f.read()
    read = read.split()
    x = [float(i) for i in read[10:-7:8]]
    cf = [float(i) for i in read[15:-2:8]]
f.close()

##3.1.2 Load Cp file 
with open(dict_xfoil,'r') as f : 
    read = f.read()
    read = read.split()
    x = [float(i) for i in read[15:-2:3]]
    cp = [float(i) for i in read[17::3]]
f.close()

##3.2 For Ansys 
#### Also valid for Numerical part !
##3.2.1 Load Cf file , two cases for upper and lower 
with open(dict_ansys,'r') as f: 
    read_up = f.read()
    read_up = read_up.split()
f.close()
x_up = [float(j) for j in read_up[11:-2:2]]
cp_up = [float(j) for j in read_up[12:-1:2]]

with open(dict_ansys,'r') as f: 
    read_low = f.read()
    read_low = read_low.split()
f.close()
x_low = [float(j) for j in read_low[11:-2:2]]
cp_low = [float(j) for j in read_low[12:-1:2]]


#3.2.3 Load Cp file, two cases for upper and lower 
with open(dict_ansys,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
f.close()
x_up = [float(j) for j in read_up[9:-1:2]]
cp_up = [float(j) for j in read_up[10::2]]
    
with open(dict_ansys,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
f.close()
x_low = [float(j) for j in read_low[9:-1:2]]
cp_low = [float(j) for j in read_low[10::2]]



#######There is a way to plot both upper and lower sides. 
#######This method works for both Cp and Cf
m = len(x_up) +len(x_low)
n = len(cp_low) + len(cp_up)

x_plot = np.zeros((m+15,1))
cp_plot = np.zeros((n+15,1))

flag_up= 0
flag_low = 1
for i in np.arange(0,len(x_up)):
    x_plot[flag_up,:] = x_up[i]
    flag_up += 2
for i in np.arange(0,len(x_low)):
    x_plot[flag_low,:] = x_low[i]
    flag_low += 2
flag_up= 0
flag_low = 1    
for i in np.arange(0,len(cp_up)):    
    cp_plot[flag_up,:] = cp_up[i]
    flag_up += 2
for i in np.arange(0,len(cp_low)):
    cp_plot[flag_low,:] = cp_low[i]
    flag_low += 2






###### Part4 plot
## 4.1 Label and setting 
plt.xlabel('Location x/c')
plt.ylabel('Pressure Coefficient')
## 4.2 This figure size is for amplifying the Cf plot, which is used for observing separation point.
plt.figure(figsize=[50,10])

## 4.3 A way to have two ysticks with different label , which is used for Numerical Study
x = []
y = []
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax2.plot(x, y, 'o-r',markersize = 10,lw = 1.5)
ax1.plot(x, y, 'o-b',markersize = 10,lw = 1.5)


ax1.set_xlabel(r'$R_{CD}$')
ax2.set_ylabel('Cl', color='r',fontsize = 15)
ax1.set_ylabel('Cd', color='b',fontsize = 15) 

## 4.4 Location to save the plots and Naming 
### To be noticed : Do NOT add title in the figure !!!

# 4.4.1 Aerodynamic coefficient 
# Format : {Ansys/Xfoil}_{Airfoil}_{which coefficient}_{w.r.t what coefficient/ factor}@{under what situation}
#### If both ansys and xfoil contain ,then There is no first {}
### Compare with different model :
## GIVE some examples 
tlt_Cl = "{}_{}_Cl_model_@Re{}"
tlt_Cd = "{}_Cd_model_@Re{}"
tlt_Cm = "{}_Cm_model_@Re{}"
tlt_ClCd ="{}_ClCd_model_@Re{}"
### Compare under different Re number:
tlt_Cl_Re = "{}_{}_Cl_Re_@{}".format(Airfoil[0],Fluent_Model[1])

## 4.5 Save figures 
io_fig_xfoil = "/Users/wangyuning/Desktop/LowRe/Xfoil_Result/{}"
io_fig_ansys = "/Users/wangyuning/Desktop/LowRe/Ansys_Result/{}"
io_fig_ansys_Cf = "/Users/wangyuning/Desktop/LowRe/Ansys_Result_Cf/{}"

io_fig_Numerical ="/Users/wangyuning/Desktop/LowRe/Numerical_Result/{}"
io_fig_compare = "/Users/wangyuning/Desktop/LowRe/Compare_Result/{}"