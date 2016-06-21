import math
import matplotlib.pyplot as plt

g=9.8

def euler_cromer(omega0,theta0,l,T,dt):
    t=0
    omega,theta = omega0,theta0
    motion=[[]for i in range(3)]
    motion[0].append(omega)
    motion[1].append(theta)
    motion[2].append(t)
    while t<=T:
        omega = omega-(g/l)*theta*dt
        theta = theta+omega*dt
        t = t+dt
        motion[0].append(omega)
        motion[1].append(theta)
        motion[2].append(t)
    return motion

d=euler_cromer(0,0.2,1,10,0.04)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='dt=0.04')
d=euler_cromer(0,0.2,1,10,0.05)
plt.plot(d[2],d[1],linestyle='-',linewidth=1.0,label='dt=0.05')


plt.xlim(0,10)
plt.grid(True,color='k')
plt.title('Fig.2 euler_cromer')
plt.xlabel('Time(s)')
plt.ylabel(r'$\theta$(radius)')
plt.legend()
plt.show()


