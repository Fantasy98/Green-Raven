from cProfile import label
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd
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

for re in np.arange(len(Reynolds_Number_MH61)):
    
    Sep = df['Separation'].loc[df['Re']==Reynolds_Number_MH61[re]].values
    Tran = df['Transition'].loc[df['Re']==Reynolds_Number_MH61[re]].values
    Reattch = df['Reattachment'].loc[df['Re']==Reynolds_Number_MH61[re]].values
    l_sep  = len(Sep)
    plt.figure(re)
    plt.grid()
    tlt = 'LSB@Re{}'.format(Reynolds_Number_MH61[re])
    plt.xlabel('x/c',fontdict=font_dict)
    plt.ylabel("Angle of Attack (deg)",fontdict=font_dict)
    plt.plot(Sep,Angle_of_Attack[0:l_sep],'-o',markersize = 9.5,label='Separation')
    plt.plot(Tran,Angle_of_Attack[0:l_sep],'-v',markersize = 9.5,label='Transition')
    plt.plot(Reattch,Angle_of_Attack[0:l_sep],'-s',markersize = 9.5,label='Reattachment')
    plt.legend()
    plt.savefig(io_fig_ansys_Cf.format(tlt))




df = pd.read_excel('LSB.xlsx',sheet_name='MH104',header=0,dtype=dtyp_dict)
df = df.dropna()

for re in np.arange(len(Reynolds_Number_MH104)):
    
    Sep = df['Separation'].loc[df['Re']==Reynolds_Number_MH104[re]].values
    Tran = df['Transition'].loc[df['Re']==Reynolds_Number_MH104[re]].values
    Reattch = df['Reattachment'].loc[df['Re']==Reynolds_Number_MH104[re]].values
    l_sep  = len(Sep)
    plt.figure(re+5)
    plt.grid()
    tlt = 'LSB@Re{}'.format(Reynolds_Number_MH104[re])
    plt.xlabel('x/c',fontdict=font_dict)
    plt.ylabel("Angle of Attack (deg)",fontdict=font_dict)
    plt.plot(Sep,Angle_of_Attack[0:l_sep],'-o',markersize = 9.5,label='Separation')
    plt.plot(Tran,Angle_of_Attack[0:l_sep],'-v',markersize = 9.5,label='Transition')
    plt.plot(Reattch,Angle_of_Attack[0:l_sep],'-s',markersize = 9.5,label='Reattachment')
    plt.legend()
    plt.savefig(io_fig_ansys_Cf.format(tlt))

df = pd.read_excel('LSB.xlsx',sheet_name='MH61',header=0,dtype=dtyp_dict)
df = df.dropna()

for aoa in Angle_of_Attack[-2:]:
    Sep = df['Separation'].loc[df['Angle of Attack ']==aoa].values
    Tran = df['Transition'].loc[df['Angle of Attack ']==aoa].values
    Reattch = df['Reattachment'].loc[df['Angle of Attack ']==aoa].values
    plt.figure(aoa+10)
    plt.grid()
    tlt = 'MH61_LSB@aoa{}'.format(aoa)
    plt.ylabel('x/c',fontdict=font_dict)
    plt.xlabel(r"Reynolds Number x$10^{6}$",fontdict=font_dict)
    
    plt.plot(Reynolds_Number_MH61/(10**6),Sep,'-o',markersize = 9.5,label='Separation')
    plt.plot(Reynolds_Number_MH61/(10**6),Tran,'-v',markersize = 9.5,label='Transition')
    plt.plot(Reynolds_Number_MH61/(10**6),Reattch,'-s',markersize = 9.5,label='Reattachment')
    plt.legend()
    plt.savefig(io_fig_ansys_Cf.format(tlt))

    
df = pd.read_excel('LSB.xlsx',sheet_name='MH104',header=0,dtype=dtyp_dict)
df = df.dropna()

for aoa in Angle_of_Attack[-2:]:
    Sep = df['Separation'].loc[df['Angle of Attack ']==aoa].values
    Tran = df['Transition'].loc[df['Angle of Attack ']==aoa].values
    Reattch = df['Reattachment'].loc[df['Angle of Attack ']==aoa].values
    plt.figure(aoa+20)
    plt.grid()
    tlt = 'MH104_LSB@aoa{}'.format(aoa)
    plt.ylabel('x/c',fontdict=font_dict)
    plt.xlabel(r"Reynolds Number x$10^{6}$",fontdict=font_dict)
    
    plt.plot(Reynolds_Number_MH104/(10**6),Sep,'-o',markersize = 9.5,label='Separation')
    plt.plot(Reynolds_Number_MH104/(10**6),Tran,'-v',markersize = 9.5,label='Transition')
    plt.plot(Reynolds_Number_MH104/(10**6),Reattch,'-s',markersize = 9.5,label='Reattachment')
    plt.legend()
    plt.savefig(io_fig_ansys_Cf.format(tlt))
