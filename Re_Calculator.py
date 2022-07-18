import numpy as np 

rho = 1.225 
visc = 1.789*10**(-5)

MH61_Length = np.array([0.25,0.36,0.7,0.98])
MH104_Length = np.array([1.52,1.7])

velocity = 20 

Re_MH61 =  rho*MH61_Length*velocity/visc
Re_MH104 = rho*MH104_Length*velocity/visc

Velocity_MH61 = Re_MH61*visc/rho
Velocity_MH104 = Re_MH104*visc/rho

with open('ReynoldsNumber_calculate.txt','w+') as f :
    f.write("When set free stream velocity is {}m/s: \n".format(velocity))
    f.write("Corresponding Reynolds number for MH61 at {}m/s is{} {} {} {} \n".format(velocity,Re_MH61[0],Re_MH61[1],Re_MH61[2],Re_MH61[3]))
    f.write("Corresponding Reynolds number for MH104 at {}m/s is {} {} \n".format(velocity,Re_MH104[0],Re_MH104[1]))
    f.write("Corresponding Velocity for MH61 1m Profile is {}m/s {}m/s {}m/s {}m/s \n".format(Velocity_MH61[0],Velocity_MH61[1],Velocity_MH61[2],Velocity_MH61[3]))
    f.write("Corresponding Velocity for MH104 1m Profile is {}m/s {}m/s  \n".format(Velocity_MH104[0],Velocity_MH104[1]))
f.close()