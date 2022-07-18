#################################################
##Part 1 Preparation
#################################################
from cProfile import label
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
import Load_Function as lf

Airfoil = 'MH61'
Turbulence_Model = '3EQN'
Reynolds_Number_MH61 = ['34e4','49e4','95e4','13e5']
Angle_of_Attack = [-2,0,2,4,6,8,10]

io_fig_ansys_Cf_up = "/Users/wangyuning/Desktop/LowRe/Ansys_Result_Cf/Up/{}"
io_fig_ansys_Cf_low = "/Users/wangyuning/Desktop/LowRe/Ansys_Result_Cf/Low/{}"



#################################################
##Part 3 Plot all the pressure sides
#################################################
m = 0 
plt.figure(m,figsize=[50,10])
plt.ylim([0,0.005])
plt.xticks(np.arange(0,1,0.01))
plt.grid()
tlt = "Cf_low@Re={}".format(Reynolds_Number_MH61[m])
for aoa in Angle_of_Attack :
    Upper,Lower = lf.Load_Cf_Ansys(Model=Turbulence_Model,Airfoil=Airfoil,Reynolds_number=Reynolds_Number_MH61[m],Alpha=aoa)
    Lower[0,:] = Lower[0,:]/np.max(Lower[0,:])
    plt.plot(Lower[0,:],Lower[1,:],label = r'$\alpha$ = {}'.format(aoa))
plt.legend()
plt.savefig(io_fig_ansys_Cf_low.format(tlt))

m +=1

plt.figure(m,figsize=[50,10])
plt.ylim([0,0.005])
plt.xticks(np.arange(0,1,0.01))
plt.grid()
tlt = "Cf_low@Re={}".format(Reynolds_Number_MH61[m])
for aoa in Angle_of_Attack :
    Upper,Lower = lf.Load_Cf_Ansys(Model=Turbulence_Model,Airfoil=Airfoil,Reynolds_number=Reynolds_Number_MH61[m],Alpha=aoa)
    Lower[0,:] = Lower[0,:]/np.max(Lower[0,:])
    plt.plot(Lower[0,:],Lower[1,:],label = r'$\alpha$ = {}'.format(aoa))
plt.legend()
plt.savefig(io_fig_ansys_Cf_low.format(tlt))

m +=1
plt.figure(m,figsize=[50,10])
plt.ylim([0,0.005])
plt.xticks(np.arange(0,1,0.01))
plt.grid()
tlt = "Cf_low@Re={}".format(Reynolds_Number_MH61[m])
for aoa in Angle_of_Attack :
    Upper,Lower = lf.Load_Cf_Ansys(Model=Turbulence_Model,Airfoil=Airfoil,Reynolds_number=Reynolds_Number_MH61[m],Alpha=aoa)
    Lower[0,:] = Lower[0,:]/np.max(Lower[0,:])
    plt.plot(Lower[0,:],Lower[1,:],label = r'$\alpha$ = {}'.format(aoa))
plt.legend()
plt.savefig(io_fig_ansys_Cf_low.format(tlt))

m +=1
plt.figure(m,figsize=[50,10])
plt.ylim([0,0.005])
plt.xticks(np.arange(0,1,0.01))
plt.grid()
tlt = "Cf_low@Re={}".format(Reynolds_Number_MH61[m])
for aoa in Angle_of_Attack :
    Upper,Lower = lf.Load_Cf_Ansys(Model=Turbulence_Model,Airfoil=Airfoil,Reynolds_number=Reynolds_Number_MH61[m],Alpha=aoa)
    Lower[0,:] = Lower[0,:]/np.max(Lower[0,:])
    plt.plot(Lower[0,:],Lower[1,:],label = r'$\alpha$ = {}'.format(aoa))
plt.legend()
plt.savefig(io_fig_ansys_Cf_low.format(tlt))




