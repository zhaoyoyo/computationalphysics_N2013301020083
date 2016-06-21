import math
import matplotlib.pyplot as plt  
      
g=9.8 

def f(theta,l):
    return -g*math.sin(theta)/l
dt=0.02

def EC(omega0,theta0,l,T):
    omega,theta,t = omega0,theta0,0
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    while motion[2][-1]<=T:
        omega = omega+f(theta,l)*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

d=EC(0,0.2,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$\theta_0=0.2$')
d=EC(0,5,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$\theta_0=5$')
d=EC(0,10,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'$\theta_0=10$')


plt.legend()
plt.grid(True,color='k')
plt.title('Fig.6 Nonlinear')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()
