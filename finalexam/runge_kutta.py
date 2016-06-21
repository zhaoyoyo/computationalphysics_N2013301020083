import math
import matplotlib.pyplot as plt 

g=9.8

def f(theta,l):
    return -g*math.sin(theta)/l
dt=0.02

def RK(omega0,theta0,l,T):
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while motion[2][-1]<=T:
        omega1 = omega+f(theta,l)*dt/2
        theta1 = theta+omega*dt/2
        t1 = t+dt/2
        omega=omega+f(theta1,l)*dt
        theta=theta+omega1*dt
        t=t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

d=RK(0,2,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='Runge-Kutta')
plt.text(2,15,r'$\theta_0=2,l=1$'+'\ntime step dt=0.02 seconds')
plt.legend()
plt.grid(True,color='k')
plt.title('Fig.3 runge_kutta')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()
