
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
from pyrsistent import l
io_fig_ansys_Cf = "/Users/wangyuning/Desktop/LowRe/Ansys_Result_Cf/{}"

Airfoil = ['MH61','MH104']
Angle_of_Attack = [-2,0,2,4,6,8,10]
Reynolds_Number_MH61 = [342293,492902,958421,1341790]
Reynolds_Number_MH61 = np.array(Reynolds_Number_MH61)
Reynolds_Number_MH104 = [2081144,2327595]
Reynolds_Number_MH104 = np.array(Reynolds_Number_MH104)
font_dict = {'size':16}
dtyp_dict = {'Angle of Attack':np.int64,'Separation':np.float64,'Transition':np.float64,'Reattachment':np.float64}
df = pd.read_excel('LSB.xlsx',sheet_name='MH61',header=0,dtype=dtyp_dict)
df = df.dropna()

Sep = np.zeros((len(Reynolds_Number_MH61),len(Angle_of_Attack)))
Tran = np.zeros((len(Reynolds_Number_MH61),len(Angle_of_Attack)))
Reattch = np.zeros((len(Reynolds_Number_MH61),len(Angle_of_Attack)))

print(Sep.shape)
for re in np.arange(len(Reynolds_Number_MH61)):
    
    Sep[re,:] = df['Separation'].loc[df['Re']==Reynolds_Number_MH61[re]].values
    Tran[re,:] = df['Transition'].loc[df['Re']==Reynolds_Number_MH61[re]].values
    Reattch[re,:] = df['Reattachment'].loc[df['Re']==Reynolds_Number_MH61[re]].values
    print(Sep[re,:])

n = 0
fig = plt.figure(n)
ax = fig.add_subplot(projection = '3d')
plt.grid()
tlt = 'LSB_3D_Sep@MH61'
ax.set_xlabel('Angle of Attack')
ax.set_ylabel(r'Reynolds Number x $10^{6}$')

ax.set_zlabel('Separation')

for re in np.arange(len( Reynolds_Number_MH61)):
    ax.bar(Angle_of_Attack[:],Sep[re,:],zdir='y',zs = Reynolds_Number_MH61[re]/(10**6))
    
     
ax.set_yticks(Reynolds_Number_MH61/(10**6))

plt.savefig(io_fig_ansys_Cf.format(tlt))

n+=1

fig = plt.figure(n)
ax = fig.add_subplot(projection = '3d')
plt.grid()
tlt = 'LSB_3D_Tran@MH61'
ax.set_xlabel('Angle of Attack')
ax.set_ylabel(r'Reynolds Number x $10^{6}$')

ax.set_zlabel('Transition')

for re in np.arange(len( Reynolds_Number_MH61)):
    ax.bar(Angle_of_Attack[:],Tran[re,:],zdir='y',zs = Reynolds_Number_MH61[re]/(10**6))
    
     
ax.set_yticks(Reynolds_Number_MH61/(10**6))
plt.savefig(io_fig_ansys_Cf.format(tlt))

n+=1


fig = plt.figure(n)
ax = fig.add_subplot(projection = '3d')
plt.grid()
tlt = 'LSB_3D_Reattach@MH61'
ax.set_xlabel('Angle of Attack')
ax.set_ylabel(r'Reynolds Number x $10^{6}$')
ax.set_zlabel('Reattachment')

for re in np.arange(len( Reynolds_Number_MH61)):
    ax.bar(Angle_of_Attack[:],Reattch[re,:],zdir='y',zs = Reynolds_Number_MH61[re]/(10**6))
    
     
ax.set_yticks(Reynolds_Number_MH61/(10**6))
plt.savefig(io_fig_ansys_Cf.format(tlt))

n+=1

