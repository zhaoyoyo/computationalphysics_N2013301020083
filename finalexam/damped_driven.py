import math
import matplotlib.pyplot as plt  
    
g=9.8 


def DampedDriven(omega0,theta0,q,FD,omegaD,l,T):
    dt=0.001
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<= T:
        omega = omega+(-g*theta/l-q*omega+FD* math.sin(omegaD*t))*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

d=DampedDriven(0,0.2,1,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'q=1,$F_D=0,\Omega_D=0$')
d=DampedDriven(0,0.2,3,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'q=3,$F_D=0,\Omega_D=0$')
d=DampedDriven(0,0.2,10,0,0,1,10)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'q=10,$F_D=0,\Omega_D=0$')
d=DampedDriven(0,0.2,1,0.8,2,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'q=1,$F_D=0.8,\Omega_D=2$')
d=DampedDriven(0,0.2,1,2,2.0,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'q=1,$F_D=2.0,\Omega_D=2$')
d=DampedDriven(0,0.2,1,0.4,1,1,20)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label=r'q=1,$F_D=0.4,\Omega_D=1$')
plt.text(13,-0.35,r'$\theta_0=0.2,q=1,l=1$')
plt.xlim(0,10)
plt.grid(True,color='k')
plt.title('Fig.5 Damped_Driven')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()
