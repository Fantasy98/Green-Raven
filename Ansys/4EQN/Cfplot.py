from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd 

sides = ['up','low']
Re_numbers = ['34e4','49e4','95e4']
Angle_of_attack =[-2,0,2,4,6,8,10]

file_title  = "4EQN_Cf_{}_MH61Re{}{}deg.txt"

# Fig1 Re=3.4e5 at different angle of attack from -5 to 6 deg. 
plt.figure(0)
plt.xlabel('location x/c')
plt.ylabel('Skin Fraction Coefficient')

plt.grid()
plt.ylim([0,0.02])

w = []
for i in Angle_of_attack:
    w.append("AOA={}".format(i))
    load_title = file_title.format(sides[1],Re_numbers[1],i)

    with open(load_title,'r') as f: 
        read = f.read()
        read = read.split()
    f.close()

    x = [float(i) for i in read[11:-2:2]]
    scale = x[-1]
    x = [i/scale for i in x]
    Cf = [float(i) for i in read[12:-1:2]]
    print(len(x)==len(Cf))
    plt.plot(x,Cf,'-',lw = 1)
plt.legend(w,loc='upper right')
plt.savefig('MH61_lower_Re{}_AOA-2~10'.format(Re_numbers[1]))

#Fig 2 