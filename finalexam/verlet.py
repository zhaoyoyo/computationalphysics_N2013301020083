import math
import matplotlib.pyplot as plt 

g=9.8
def f(theta,l):
    return -g*math.sin(theta)/l
dt=0.02

def Verlet(omega0,theta0,l,T):
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    motion[1].append(theta0+omega0*dt)
    motion[2].append(dt)
    for i in range(1,int(T/dt)):
        motion[1].append(2*motion[1][i]-motion[1][i-1]+f(motion[1][i],l)*dt**2)
        motion[0].append((motion[1][i+1]-motion[1][i-1])/(2*dt))
        motion[2].append(motion[2][i]+dt)
    return motion

d=Verlet(0,2,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='Verlet')
plt.text(2,15,r'$\theta_0=2,l=1$'+'\ntime step dt=0.02 seconds')
plt.legend()
plt.grid(True,color='k')
plt.title('Fig.4 verlet')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()
