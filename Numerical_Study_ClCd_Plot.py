import numpy as np
import Load_Function as lf
from matplotlib import pyplot as plt
io_fig_Numerical ="/Users/wangyuning/Desktop/LowRe/Numerical_Result/{}"

keywords = ["Grid Convergence","Domain Examination","Time Scale Factor","Turbulence Intensity"]

fontdic = {'size':16}
Cl_Xfoil = 0.7531
Cd_Xfoil = 0.00838
####################################################################################
#Part 1 Grid Convergence 
####################################################################################

df = lf.Load_Numerical_Excel(keyword=keywords[0])

n = 0
tlt = "Grid_Convergence_Cl_Cd"
# plt.figure(n,figsize=[20,20])
Cl = df["Cl"].values
Cd = df['Cd'].values
grid = df["Number of Elements"].values
grid = grid/(10**5)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax2.plot(grid, Cl, 'o-r',markersize = 10,lw = 1.5)
# ax2.hlines(Cl_Xfoil,xmin=grid[0],xmax=grid[-1],colors='r',linestyles='dashdot',label='Xfoil')
# ax1.hlines(Cd_Xfoil,xmin=grid[0],xmax=grid[-1],colors='b',linestyles='dashdot',label='Xfoil')
ax1.plot(grid, Cd, 'o-b',markersize = 10,lw = 1.5)


ax1.set_xlabel('Number of Elements (x10^5)',fontdict=fontdic)
ax2.set_ylabel('Cl', color='r',fontsize = 15)
ax1.set_ylabel('Cd', color='b',fontsize = 15) 
plt.legend()
plt.savefig(io_fig_Numerical.format(tlt),bbox_inches='tight')

n+=1

dCl = np.diff(Cl)
deCl = dCl/Cl[0:-1] * 100
print("{} delta Cl is {}%".format(tlt,deCl))
dCd = np.diff(Cd)
deCd = dCd/Cd[0:-1] * 100
print("{} delta Cd is {}%".format(tlt,deCd))

####################################################################################
#Part 2 Domain_Examination
####################################################################################

df = lf.Load_Numerical_Excel(keyword=keywords[1])


tlt = "Domain_Examination_Cl_Cd"
# plt.figure(n,figsize=[20,20])
Cl = df["Cl"].values
Cd = df['Cd'].values
grid = df["R"].values

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax2.plot(grid, Cl, 'o-r',markersize = 10,lw = 1.5)
ax1.plot(grid, Cd, 'o-b',markersize = 10,lw = 1.5)

ax1.set_xlabel('Radius of Domain (m)',fontdict=fontdic)
ax2.set_ylabel('Cl', color='r',fontsize = 15)
ax1.set_ylabel('Cd', color='b',fontsize = 15) 
plt.savefig(io_fig_Numerical.format(tlt),bbox_inches='tight')

dCl = np.diff(Cl)
deCl = dCl/Cl[0:-1] * 100
print("{} delta Cl is {}%".format(tlt,deCl))
dCd = np.diff(Cd)
deCd = dCd/Cd[0:-1] * 100
print("{} delta Cd is {}%".format(tlt,deCd))

####################################################################################
#Part 3 Time Scale Factor
####################################################################################

df = lf.Load_Numerical_Excel(keyword=keywords[2])


tlt = "Time_Scale_Factor_Cl_Cd"
# plt.figure(n,figsize=[20,20])
Cl = df["Cl"].values
Cd = df['Cd'].values
grid = df["Time Scale Factor "].values

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.xscale('log')
ax2.plot(grid, Cl, 'o-r',markersize = 10,lw = 1.5)
ax1.plot(grid, Cd, 'o-b',markersize = 10,lw = 1.5)

ax1.set_xlabel('Time Scale Factor',fontdict=fontdic)
ax2.set_ylabel('Cl', color='r',fontsize = 15)
ax1.set_ylabel('Cd', color='b',fontsize = 15) 
plt.savefig(io_fig_Numerical.format(tlt),bbox_inches='tight')

dCl = np.diff(Cl)
deCl = dCl/Cl[0:-1] * 100
print("{} delta Cl is {}%".format(tlt,deCl))
dCd = np.diff(Cd)
deCd = dCd/Cd[0:-1] * 100
print("{} delta Cd is {}%".format(tlt,deCd))

####################################################################################
#Part 4 Turbulence Intensity
####################################################################################

df = lf.Load_Numerical_Excel(keyword=keywords[-1])


tlt = "Turbulence_Intensity_Cl_Cd"
# plt.figure(n,figsize=[30,30])
Cl = df["Cl"].values
Cd = df['Cd'].values
grid = df["Turbulence Intensity(%)"].values

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax2.plot(grid, Cl, 'o-r',markersize = 10,lw = 1.5)
ax1.plot(grid, Cd, 'o-b',markersize = 10,lw = 1.5)

ax1.set_xlabel('Turbulence Intensity(%)',fontdict=fontdic)
ax2.set_ylabel('Cl', color='r',fontsize = 15)
ax1.set_ylabel('Cd', color='b',fontsize = 15) 
plt.savefig(io_fig_Numerical.format(tlt),bbox_inches='tight')

dCl = np.diff(Cl)
deCl = dCl/Cl[0:-1] * 100
print("{} delta Cl is {}%".format(tlt,deCl))
dCd = np.diff(Cd)
deCd = dCd/Cd[0:-1] * 100
print("{} delta Cd is {}%".format(tlt,deCd))