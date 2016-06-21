import math
import matplotlib.pyplot as plt      
g=9.8 
dt=0.04

def adjust(x):
    while x>math.pi:
        x=x-2*math.pi
    while x<-math.pi:
        x=x+2*math.pi
    return x

def EC(omega0,theta0,q,l,FD,omegaD,T):
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    while motion[2][-1]<=T:
        motion[0].append(motion[0][-1]+(-g*math.sin(motion[1][-1])/l-q*motion[0][-1]+FD*math.sin(omegaD*motion[2][-1]))*dt)
        motion[1].append(motion[1][-1]+motion[0][-1]*dt)
        motion[2].append(motion[2][-1]+dt)
    return motion



omega0,theta0,q,l,omegaD,T=0,0.2,0.5,9.8,0.66,60
d1=EC(omega0,theta0,q,l,0,omegaD,T)
d2=EC(omega0,theta0,q,l,0.5,omegaD,T)
d3=EC(omega0,theta0,q,l,1.2,omegaD,T)
plt.plot(d1[2],d1[1],linestyle='-',linewidth=1.0,label=r'$F_D=0$')
plt.plot(d2[2],d2[1],linestyle='-',linewidth=1.0,label=r'$F_D=0.5$')
plt.plot(d3[2],d3[1],linestyle='-',linewidth=1.0,label=r'$F_D=1.2$')
plt.xlim(0,T)
plt.grid(True,color='k')
plt.title(r'Fig7.1 $\theta$ versus time with different $F_D$')
plt.ylabel(r'$\theta$(radius)',fontsize=15)
plt.xlabel('time(seconds)',fontsize=15)
plt.legend()
plt.show()







omega0,theta0,q,l,omegaD,T=0,0.2,0.5,9.8,0.66,60
d1=EC(omega0,theta0,q,l,0,omegaD,T)
d2=EC(omega0,theta0,q,l,0.5,omegaD,T)
d3=EC(omega0,theta0,q,l,1.2,omegaD,T)
plt.plot(d3[2],d3[0],linestyle='-',linewidth=1.0,label=r'$F_D=1.2$')
plt.plot(d2[2],d2[0],linestyle='-',linewidth=1.0,label=r'$F_D=0.5$')
plt.plot(d1[2],d1[0],linestyle='-',linewidth=1.0,label=r'$F_D=0$')
plt.title(r'Fig.7.2 $\omega$ versus time with different $F_D$')
plt.xlim(0,T)
plt.grid(True,color='k')
plt.ylabel(r'$\omega$(radius/second)',fontsize=15)
plt.xlabel('time(seconds)',fontsize=15)
plt.legend()
plt.show()

