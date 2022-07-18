####Part 1 Package used 
from cProfile import label
from matplotlib import pyplot as plt
import numpy as np 
import pandas as pd

#####Part 2 Document and Data Naming 

# General 
Airfoil = ['MH61','MH104']
Angle_of_Attack = [-4,-2,0,2,4,6,8,10,12]
Reynolds_Number = ['96e4','11e5','12e5']
Data_kind =['Cp','Cf']

##2.1 Load From the xfoil
io_xfoil  = "/Users/wangyuning/Desktop/LowRe/Xfoil/{}"
title_xfoil = 'Xfoil_{}_{}_Re{}{}deg.txt'  
#For example : Xfoil_MH61_Cp_Re11e52deg.txt
# dict_xfoil = io_xfoil.format(title_xfoil)

##3.1.1 Load Cf file
# with open(dict_xfoil,'r') as f: 
#     read = f.read()
#     read = read.split()
#     x = [float(i) for i in read[10:-7:8]]
#     cf = [float(i) for i in read[15:-2:8]]
# f.close()

# ##3.1.2 Load Cp file 
# with open(dict_xfoil,'r') as f : 
#     read = f.read()
#     read = read.split()
#     x = [float(i) for i in read[15:-2:3]]
#     cp = [float(i) for i in read[17::3]]
# f.close()


# Format : {Ansys/Xfoil}_{Airfoil}_{which coefficient}_{w.r.t what coefficient/ factor}@{under what situation}

io_fig_xfoil = "/Users/wangyuning/Desktop/LowRe/Xfoil_Result/{}"

# For MH61
### Plot Cp at Each Angle of Attack under 3 Re numbers 
n = 0 
fig_title = "{}_{}_{}_{}@{}"
for aoa in Angle_of_Attack : 
    in_title = fig_title.format("Xfoil",Airfoil[0],Data_kind[0],aoa,"all_Re")
    plt.figure(n)
    plt.xlabel('location (x/c)')
    plt.ylabel("Pressure Coefficient")
    plt.grid()
    for re in Reynolds_Number:
        doc_xfoil = title_xfoil.format(Airfoil[0],Data_kind[0],re,aoa)
        dict_xfoil = io_xfoil.format(doc_xfoil)
        with open(dict_xfoil,'r') as f : 
            read = f.read()
            read = read.split()
        f.close()
        x = [float(i) for i in read[15:-2:3]]
        cp = [float(i) for i in read[17::3]]
        print('Plotting {} Cp at aoa = {} re = {}'.format(Airfoil[0],aoa,re))
        plt.plot(x,cp,'-',lw = 2,label="Re={}".format(re))

    plt.legend()
    plt.savefig(io_fig_xfoil.format(in_title))
    n+=1


for aoa in Angle_of_Attack : 
    in_title = fig_title.format("Xfoil",Airfoil[0],Data_kind[1],aoa,"all_Re")
    
    plt.figure(n)
    plt.xlabel('location (x/c)')
    plt.ylabel("Skin Friction  Coefficient")
    plt.grid()
    plt.xlim([0,1])
    plt.ylim([-0.001,0.02])
    for re in Reynolds_Number:
        doc_xfoil = title_xfoil.format(Airfoil[0],Data_kind[1],re,aoa)
        dict_xfoil = io_xfoil.format(doc_xfoil)
        with open(dict_xfoil,'r') as f : 
            read = f.read()
            read = read.split()
        f.close()
        x = [float(i) for i in read[10:-7:8]]
        cf = [float(i) for i in read[15:-2:8]]
        print('Plotting {} Cp at aoa = {} re = {}'.format(Airfoil[0],aoa,re))
        plt.plot(x,cf,'-',lw=0.7,markersize = 1,label="Re={}".format(re))
    plt.legend()
    plt.savefig(io_fig_xfoil.format(in_title))
    n+=1



# For MH104
### Plot Cp at Each Angle of Attack under 3 Re numbers 

fig_title = "{}_{}_{}_{}@{}"
for aoa in Angle_of_Attack : 
    in_title = fig_title.format("Xfoil",Airfoil[1],Data_kind[0],aoa,"all_Re")
    
    plt.figure(n)
    plt.xlabel('location (x/c)')
    plt.ylabel("Pressure Coefficient")
    plt.grid()
    for re in Reynolds_Number:
        doc_xfoil = title_xfoil.format(Airfoil[1],Data_kind[0],re,aoa)
        dict_xfoil = io_xfoil.format(doc_xfoil)
        with open(dict_xfoil,'r') as f : 
            read = f.read()
            read = read.split()
        f.close()
        x = [float(i) for i in read[15:-2:3]]
        cp = [float(i) for i in read[17::3]]
        print('Plotting {} Cp at aoa = {} re = {}'.format(Airfoil[1],aoa,re))
        plt.plot(x,cp,'-',lw = 2,label="Re={}".format(re))

    plt.legend()
    plt.savefig(io_fig_xfoil.format(in_title))
    n+=1


for aoa in Angle_of_Attack : 
    in_title = fig_title.format("Xfoil",Airfoil[1],Data_kind[1],aoa,"all_Re")
    
    plt.figure(n)
    plt.xlabel('location (x/c)')
    plt.ylabel("Skin Friction  Coefficient")
    plt.grid()
    plt.xlim([0,1])
    plt.ylim([-0.001,0.02])
    for re in Reynolds_Number:
        doc_xfoil = title_xfoil.format(Airfoil[0],Data_kind[1],re,aoa)
        dict_xfoil = io_xfoil.format(doc_xfoil)
        with open(dict_xfoil,'r') as f : 
            read = f.read()
            read = read.split()
        f.close()
        x = [float(i) for i in read[10:-7:8]]
        cf = [float(i) for i in read[15:-2:8]]
        print('Plotting {} Cf at aoa = {} re = {}'.format(Airfoil[1],aoa,re))
        plt.plot(x,cf,'-',lw=0.7,markersize = 1,label="Re={}".format(re))
    plt.legend()
    plt.savefig(io_fig_xfoil.format(in_title))
    n+=1