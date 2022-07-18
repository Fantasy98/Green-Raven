from cProfile import label
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
import Load_Function as lf

io_fig_ansys_Cf = "/Users/wangyuning/Desktop/LowRe/Ansys_Result_Cf/{}"

Upper,Lower = lf.Load_Cf_Ansys(Model='3EQN', Airfoil='MH61',Reynolds_number='49e4',Alpha=2)
Upper[0,:] = Upper[0,:]/np.max(Upper[0,:])
Lower[0,:] = Lower[0,:]/np.max(Lower[0,:])


font_dict = {'size':15}
n = 0
plt.figure(n)
plt.grid()
plt.ylabel('Skin Friction Coefficient',fontdict=font_dict)
plt.xlabel('x/c',fontdict=font_dict)
plt.ylim([0,0.01])
plt.xlim([0,1])
tlt = 'Cf_example'
plt.plot(Upper[0,:],Upper[1,:],'r',lw=3.5,label='Suction Side')
plt.plot(Lower[0,:],Lower[1,:],'b',lw=3.5,label='Pressure Side')
plt.legend()
plt.savefig(io_fig_ansys_Cf.format(tlt),bbox_inches='tight')