
from typing import Sequence
import numpy as np 
import pandas  as pd

def Load_Numerical_Excel(keyword):
    df = pd.read_excel("Numerical Study at AOA =6deg_LowRE.xlsx",sheet_name=keyword,header=1,dtype={"Cl":np.float32,"Cd":np.float32,"Cm":np.float32,})
    return df


def Load_Cp_Xfoil(Airfoil:str,Reynolds_number:str,Alpha:int):
    io_xfoil  = "/Users/wangyuning/Desktop/LowRe/Xfoil/{}"
    title_xfoil = 'Xfoil_{}_Cp_Re{}{}deg.txt'.format(Airfoil,Reynolds_number,Alpha)  
    #For example : Xfoil_MH61_Cp_Re11e52deg.txt
    dict_xfoil = io_xfoil.format(title_xfoil)
    with open(dict_xfoil,'r') as f : 
        read = f.read()
        read = read.split()
    f.close()
    x = [float(i) for i in read[15:-2:3]]
    cp = [float(i) for i in read[17::3]]
    return x,cp


def Load_Cf_Xfoil(Airfoil:str,Reynolds_number:str,Alpha:int):
    io_xfoil  = "/Users/wangyuning/Desktop/LowRe/Xfoil/{}"
    title_xfoil = 'Xfoil_{}_Cf_Re{}{}deg.txt'.format(Airfoil,Reynolds_number,Alpha)  
    #For example : Xfoil_MH61_Cp_Re11e52deg.txt
    dict_xfoil = io_xfoil.format(title_xfoil)
    with open(dict_xfoil,'r') as f: 
        read = f.read()
        read = read.split()
    f.close()
    x = [float(i) for i in read[10:-7:8]]
    cf = [float(i) for i in read[15:-2:8]]
    return x,cf

def Load_Cp_Ansys(Model:str,Airfoil:str,Reynolds_number:str,Alpha:int):
    io_ansys  = "/Users/wangyuning/Desktop/LowRe/Ansys/{}/{}"
    title_ansys_up = '{}_Cp_up_{}Re{}{}deg.txt'.format(Model,Airfoil,Reynolds_number,Alpha)
    #For example : 4EQN_Cf_up_MH61Re12e56deg.txt
    dict_ansys_up = io_ansys.format(Model,title_ansys_up)
    with open(dict_ansys_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[9:-1:2]] )[np.newaxis]
    cp_up =np.array( [float(j) for j in read_up[10::2]] )[np.newaxis]
    
    title_ansys_low = '{}_Cp_low_{}Re{}{}deg.txt'.format(Model,Airfoil,Reynolds_number,Alpha)
    #For example : 4EQN_Cf_up_MH61Re12e56deg.txt
    dict_ansys_low = io_ansys.format(Model,title_ansys_low)
    with open(dict_ansys_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[9:-1:2]])[np.newaxis]
    cp_low = np.array([float(j) for j in read_low[10::2]])[np.newaxis]
    
    Upper = np.vstack((x_up,cp_up))
    Lower = np.vstack((x_low,cp_low))

    return Upper,Lower

def Merge_Cp(Upper:Sequence,Lower:Sequence):

    m = len(Upper[0,:])+len(Lower[0,:])
    n = len(Upper[1,:])+len(Lower[1,:])
    
    
    Upper = Upper[:,0:-15]
    Lower = Lower[:,0:-15]
    x_plot = np.hstack((Upper[0,:],Lower[0,:]))
    cp_plot = np.hstack((Upper[1,:],Lower[1,:]))

    # flag_up= 0
    # flag_low = 1
    # for i in np.arange(0,len(Upper[0,:])):
    #     x_plot[flag_up,:] = Upper[0,i]
    #     flag_up += 2
    # for i in np.arange(0,len(Lower[0,:])):
    #     x_plot[flag_low,:] = Lower[0,i]
    #     flag_low += 2
    # flag_up= 0
    # flag_low = 1    
    # for i in np.arange(0,len(Upper[1,:])):    
    #     cp_plot[flag_up,:] = Upper[1,i]
    #     flag_up += 2
    # for i in np.arange(0,len(Lower[1,:])):
    #     cp_plot[flag_low,:] = Lower[1,i]
    #     flag_low += 2
    return x_plot,cp_plot



def Load_Cf_Ansys(Model:str,Airfoil:str,Reynolds_number:str,Alpha:int):
    io_ansys  = "/Users/wangyuning/Desktop/LowRe/Ansys/{}/{}"
    title_ansys_up = '{}_Cf_up_{}Re{}{}deg.txt'.format(Model,Airfoil,Reynolds_number,Alpha)
    #For example : 4EQN_Cf_up_MH61Re12e56deg.txt
    dict_ansys_up = io_ansys.format(Model,title_ansys_up)
    with open(dict_ansys_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[11:-2:2]] )[np.newaxis]
    cf_up =np.array( [float(j) for j in read_up[12:-1:2]] )[np.newaxis]
    
    title_ansys_low = '{}_Cf_low_{}Re{}{}deg.txt'.format(Model,Airfoil,Reynolds_number,Alpha)
    #For example : 4EQN_Cf_up_MH61Re12e56deg.txt
    dict_ansys_low = io_ansys.format(Model,title_ansys_low)
    with open(dict_ansys_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[11:-2:2]])[np.newaxis]
    cf_low = np.array([float(j) for j in read_low[12:-1:2]])[np.newaxis]
    
    Cf_up= np.vstack((x_up,cf_up))
    Cf_low = np.vstack((x_low,cf_low))
    return Cf_up, Cf_low


def Load_Cp_Grid(size:str):
    io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/Grid_Convergence/{}"
    title_grid_up = "Cp_up_size{}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_up = io_numerical.format(title_grid_up)
    
    with open(dict_grid_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[9:-1:2]] )[np.newaxis]
    cp_up =np.array( [float(j) for j in read_up[10::2]] )[np.newaxis]
    
    title_grid_low = "Cp_low_size{}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_low = io_numerical.format(title_grid_low)
    with open(dict_grid_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[9:-1:2]])[np.newaxis]
    cp_low = np.array([float(j) for j in read_low[10::2]])[np.newaxis]
    
    Cp_up = np.vstack((x_up,cp_up))
    Cp_low = np.vstack((x_low,cp_low))

    return Cp_up,Cp_low

def Load_Cf_Grid(size:str):
    io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/Grid_Convergence/{}"
    title_grid_up = "Cf_up_size{}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_up = io_numerical.format(title_grid_up)
    
    with open(dict_grid_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[11:-2:2]] )[np.newaxis]
    cf_up =np.array( [float(j) for j in read_up[12:-1:2]] )[np.newaxis]
    
    title_grid_low = "Cf_low_size{}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_low = io_numerical.format(title_grid_low)
    with open(dict_grid_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[11:-2:2]])[np.newaxis]
    cf_low = np.array([float(j) for j in read_low[12:-1:2]])[np.newaxis]
    
    Cf_up = np.vstack((x_up,cf_up))
    Cf_low = np.vstack((x_low,cf_low))

    return Cf_up,Cf_low



def Load_Cp_Domian(size:str):
    io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/Domain_Examination/{}"
    title_grid_up = "Cp_up_R{}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_up = io_numerical.format(title_grid_up)
    
    with open(dict_grid_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[9:-1:2]] )[np.newaxis]
    cp_up =np.array( [float(j) for j in read_up[10::2]] )[np.newaxis]
    
    title_grid_low = "Cp_low_R{}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_low = io_numerical.format(title_grid_low)
    with open(dict_grid_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[9:-1:2]])[np.newaxis]
    cp_low = np.array([float(j) for j in read_low[10::2]])[np.newaxis]
    
    Cp_up = np.vstack((x_up,cp_up))
    Cp_low = np.vstack((x_low,cp_low))

    return Cp_up,Cp_low


def Load_Cf_Domain(size:str):
    io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/Domain_Examination/{}"
    title_grid_up = "Cf_up_R{}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_up = io_numerical.format(title_grid_up)
    
    with open(dict_grid_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[11:-2:2]] )[np.newaxis]
    cf_up =np.array( [float(j) for j in read_up[12:-1:2]] )[np.newaxis]
    
    title_grid_low = "Cf_low_R{}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_low = io_numerical.format(title_grid_low)
    with open(dict_grid_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[11:-2:2]])[np.newaxis]
    cf_low = np.array([float(j) for j in read_low[12:-1:2]])[np.newaxis]
    
    Cf_up = np.vstack((x_up,cf_up))
    Cf_low = np.vstack((x_low,cf_low))

    return Cf_up,Cf_low




def Load_Cp_TimeScale(size:str):
    io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/Time_Scale_Factor/{}"
    title_grid_up = "Cp_up_T={}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_up = io_numerical.format(title_grid_up)
    
    with open(dict_grid_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[9:-1:2]] )[np.newaxis]
    cp_up =np.array( [float(j) for j in read_up[10::2]] )[np.newaxis]
    
    title_grid_low = "Cp_low_T={}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_low = io_numerical.format(title_grid_low)
    with open(dict_grid_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[9:-1:2]])[np.newaxis]
    cp_low = np.array([float(j) for j in read_low[10::2]])[np.newaxis]
    
    Cp_up = np.vstack((x_up,cp_up))
    Cp_low = np.vstack((x_low,cp_low))

    return Cp_up,Cp_low


def Load_Cf_TimeScale(size:str):
    io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/Time_Scale_Factor/{}"
    title_grid_up = "Cf_up_T={}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_up = io_numerical.format(title_grid_up)
    
    with open(dict_grid_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[11:-2:2]] )[np.newaxis]
    cf_up =np.array( [float(j) for j in read_up[12:-1:2]] )[np.newaxis]
    
    title_grid_low = "Cf_low_T={}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_low = io_numerical.format(title_grid_low)
    with open(dict_grid_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[11:-2:2]])[np.newaxis]
    cf_low = np.array([float(j) for j in read_low[12:-1:2]])[np.newaxis]
    
    Cf_up = np.vstack((x_up,cf_up))
    Cf_low = np.vstack((x_low,cf_low))

    return Cf_up,Cf_low

def Load_Cp_Intensity(size:str):
    io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/Turbulence_Intensity/{}"
    title_grid_up = "Cp_up_I={}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_up = io_numerical.format(title_grid_up)
    
    with open(dict_grid_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[9:-1:2]] )[np.newaxis]
    cp_up =np.array( [float(j) for j in read_up[10::2]] )[np.newaxis]
    
    title_grid_low = "Cp_low_I={}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_low = io_numerical.format(title_grid_low)
    with open(dict_grid_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[9:-1:2]])[np.newaxis]
    cp_low = np.array([float(j) for j in read_low[10::2]])[np.newaxis]
    
    Cp_up = np.vstack((x_up,cp_up))
    Cp_low = np.vstack((x_low,cp_low))

    return Cp_up,Cp_low


def Load_Cf_Intensity(size:str):
    io_numerical= "/Users/wangyuning/Desktop/LowRe/Ansys/Turbulence_Intensity/{}"
    title_grid_up = "Cf_up_I={}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_up = io_numerical.format(title_grid_up)
    
    with open(dict_grid_up,'r') as f: 
        read_up = f.read()
        read_up = read_up.split()
    f.close()
    x_up = np.array( [float(j) for j in read_up[11:-2:2]] )[np.newaxis]
    cf_up =np.array( [float(j) for j in read_up[12:-1:2]] )[np.newaxis]
    
    title_grid_low = "Cf_low_I={}.txt".format(size)
    #For example Cp_up_size25e-3.txt
    dict_grid_low = io_numerical.format(title_grid_low)
    with open(dict_grid_low,'r') as f: 
        read_low = f.read()
        read_low = read_low.split()
    f.close()
    x_low = np.array([float(j) for j in read_low[11:-2:2]])[np.newaxis]
    cf_low = np.array([float(j) for j in read_low[12:-1:2]])[np.newaxis]
    
    Cf_up = np.vstack((x_up,cf_up))
    Cf_low = np.vstack((x_low,cf_low))

    return Cf_up,Cf_low