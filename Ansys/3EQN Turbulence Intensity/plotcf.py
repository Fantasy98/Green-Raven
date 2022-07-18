from cProfile import label
import pandas as pd
from matplotlib import pyplot as plt




intensity = [1,3,5]

io = "Cf_up_I={}.txt"

plt.figure(0)

plt.grid()
plt.ylim([0,0.0010])
# plt.xlim([0.2,0.4])
plt.xlabel('Loaction (x/c)')
plt.ylabel('Skin Friction Coefficient')
for i in intensity:
    dict = io.format(i)
    with open(dict,'r') as f:
        read = f.read()
        read = read.split()
    f.close()
    x =[float(i) for i in read[11:-2:2]]
    cf=[float(i) for i in read[12:-1:2]]
    plt.plot(x,cf,label="Turbulence Intensity = {} %".format(i))
plt.legend()
plt.savefig('Intensity')