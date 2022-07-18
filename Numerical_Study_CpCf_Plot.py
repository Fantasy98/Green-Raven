from cProfile import label
import Load_Function as lf
from matplotlib import pyplot as plt

X_Cf,Xfoil_Cf = lf.Load_Cf_Xfoil(Airfoil="MH61",Alpha=6,Reynolds_number="11e5")
X_Cp,Xfoil_Cp = lf.Load_Cp_Xfoil(Airfoil="MH61",Alpha=6,Reynolds_number="11e5")

fontdic = {'size':16}

####################################################################################
#Part 1 Grid Convergence 
####################################################################################


grid_convergence = ['1e-1','25e-3','10e-3','5e-3']
case =['Case1','Case2','Case3','Case4']
domain_exam = ['375e-2','75e-1','15','30']
time_scale_factor = ['1','1e-1','1e-2','1e-3','1e-4']
Turbulence_Intensity = ['1','3','5']

io_fig_Numerical ="/Users/wangyuning/Desktop/LowRe/Numerical_Result/{}"

n= 0
plt.figure(n,dpi=80)
plt.grid()
plt.xlabel("Location (x/c)",fontdict=fontdic)
plt.ylabel("Skin Friction Coefficient",fontdict=fontdic)
plt.ylim([0,0.0075])
plt.xlim([0,1])
tlt = "Grid_Convergence_Cf_Upper"
case_no = 0
for grid in grid_convergence: 
    Upper,Lower = lf.Load_Cf_Grid(size=grid)
    plt.plot(Upper[0,:],Upper[1,:],'-',markersize = 1,lw= 1,label = '{}'.format(case[case_no]))
    case_no +=1
# plt.plot(X_Cf,Xfoil_Cf,'-x',lw = 0.6,markersize = 0.8,label="Xfoil Reference")

plt.legend()
plt.savefig(io_fig_Numerical.format(tlt))

n+=1


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)",fontdict=fontdic)
plt.ylabel("Skin Friction Coefficient",fontdict=fontdic)
plt.ylim([0,0.0075])
plt.xlim([0,1])
tlt = "Grid_Convergence_Cf_Lower"
case_no = 0
for grid in grid_convergence: 
    Upper,Lower = lf.Load_Cf_Grid(size=grid)
    plt.plot(Lower[0,:],Lower[1,:],'-',markersize = 1,lw= 1,label = '{}'.format(case[case_no]))
    case_no +=1
# plt.plot(X_Cf,Xfoil_Cf,'-x',lw = 0.6,markersize = 0.8,label="Xfoil Reference")
plt.legend()

plt.savefig(io_fig_Numerical.format(tlt))

n+=1


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Pressure Coefficient")
plt.xlim([0,1])
tlt = "Grid_Convergence_Cp"
for grid in grid_convergence: 
    Upper,Lower = lf.Load_Cp_Grid(size=grid)
    x,cp = lf.Merge_Cp(Upper=Upper,Lower=Lower)
    plt.plot(x,cp,'.',markersize = 1,label = "Grid Size ={}".format(grid))
plt.legend(loc ='lower right')

plt.savefig(io_fig_Numerical.format(tlt))

n+=1


####################################################################################
#Part 2 Domain_Examination
####################################################################################


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Skin Friction Coefficient")
plt.ylim([0,0.0075])
plt.xlim([0,1])
tlt = "Domain_Examination_Cf_Upper"
for domian in domain_exam: 
    Upper,Lower = lf.Load_Cf_Domain(size=domian)
    plt.plot(Upper[0,:],Upper[1,:],'-',markersize = 1,lw= 1,label = 'Domian Size R = {}'.format(domian))



plt.legend()
plt.savefig(io_fig_Numerical.format(tlt))

n+=1


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Skin Friction Coefficient")
plt.ylim([0,0.0075])
plt.xlim([0,1])
tlt = "Domain_Examination_Cf_Lower"
for domian in domain_exam:  
    Upper,Lower = lf.Load_Cf_Domain(size=domian)
    plt.plot(Lower[0,:],Lower[1,:],'-',markersize = 1,lw= 1,label = 'Domian Size R = {}'.format(domian))


plt.plot(X_Cf,Xfoil_Cf,'-x',lw = 0.6,markersize = 0.8,label="Xfoil Reference")
plt.legend()

plt.savefig(io_fig_Numerical.format(tlt))

n+=1


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Pressure Coefficient")
plt.xlim([0,1])
tlt = "Domain_Examination_Cp"
for domian in domain_exam: 
    Upper,Lower = lf.Load_Cp_Domian(size=domian)
    x,cp = lf.Merge_Cp(Upper=Upper,Lower=Lower)
    plt.plot(x,cp,'.',markersize = 1,label = "Domian Size R ={}".format(domian))


plt.legend(loc ='lower right')
plt.savefig(io_fig_Numerical.format(tlt))

n+=1



####################################################################################
#Part 3 Turbulence Intensity
####################################################################################


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Skin Friction Coefficient")
plt.ylim([0,0.0075])
plt.xlim([0,1])
tlt = "Turbulence_Intensity_Cf_Upper"
for intensity in Turbulence_Intensity: 
    Upper,Lower = lf.Load_Cf_Intensity(size=intensity)
    plt.plot(Upper[0,:],Upper[1,:],'-',markersize = 1,lw= 1,label = 'Turbulence Intensity = {}%'.format(intensity))
plt.legend()
plt.savefig(io_fig_Numerical.format(tlt))

n+=1


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Skin Friction Coefficient")
plt.ylim([0,0.0075])
plt.xlim([0,1])
tlt = "Turbulence_Intensity_Cf_Lower"
for intensity in Turbulence_Intensity: 
    Upper,Lower = lf.Load_Cf_Intensity(size=intensity)
    plt.plot(Lower[0,:],Lower[1,:],'-',markersize = 1,lw= 1,label = 'Turbulence Intensity = {}%'.format(intensity))
plt.legend()
plt.savefig(io_fig_Numerical.format(tlt))

n+=1


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Pressure Coefficient")
plt.xlim([0,1])
tlt = "Turbulence_Intensity_Cp"
for intensity in Turbulence_Intensity: 
    Upper,Lower = lf.Load_Cp_Intensity(size=intensity)
    x,cp = lf.Merge_Cp(Upper=Upper,Lower=Lower)
    plt.plot(x,cp,'.',markersize = 1,label = 'Turbulence Intensity = {}%'.format(intensity))
plt.legend(loc ='lower right')

plt.savefig(io_fig_Numerical.format(tlt))

n+=1


####################################################################################
#Part 4 Time Scale Factor
####################################################################################


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Skin Friction Coefficient")
plt.ylim([0,0.0075])
plt.xlim([0,1])
tlt = "Time_Scale_Factor_Cf_Upper"
for factor in time_scale_factor: 
    Upper,Lower = lf.Load_Cf_TimeScale(size=factor)
    plt.plot(Upper[0,:],Upper[1,:],'-',markersize = 1,lw= 1,label = 'Time Scale Factor = {}'.format(factor))
plt.legend(loc = "best")

plt.savefig(io_fig_Numerical.format(tlt))

n+=1


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Skin Friction Coefficient")
plt.ylim([0,0.0075])
plt.xlim([0,1])
tlt = "Time_Scale_Factor_Cf_Lower"
for factor in time_scale_factor: 
    Upper,Lower = lf.Load_Cf_TimeScale(size=factor)
    plt.plot(Lower[0,:],Lower[1,:],'-',markersize = 1,lw= 1,label = 'Time Scale Factor = {}'.format(factor))
plt.legend()

plt.savefig(io_fig_Numerical.format(tlt))

n+=1


plt.figure(n)
plt.grid()
plt.xlabel("Location (x/c)")
plt.ylabel("Pressure Coefficient")
plt.xlim([0,1])
tlt = "Time_Scale_Factor_Cp"
for factor in time_scale_factor: 
    Upper,Lower = lf.Load_Cp_TimeScale(size=factor)
    x,cp = lf.Merge_Cp(Upper=Upper,Lower=Lower)
    plt.plot(x,cp,'.',markersize = 1,label = 'Time Scale Factor = {}'.format(factor))
plt.legend(loc ='best')

plt.savefig(io_fig_Numerical.format(tlt))

n+=1