A=input('initial population of partical A=')
B=input('initial population of partical B=')
tau_A=input('decay time constant for A partical tau_A=')
tau_B=input('decay time constant for B partical tau_B=')
dt=input('dt=')
end_time=input('end_time=')
t=0
time=[]
NA=[]
NB=[]
time.append(t)
NA.append(A)
NB.append(B)
for i in range(int(end_time/dt)+1):
    t=t+dt
    B=B+(A/tau_A-B/tau_B)*dt
    A=A-(A/tau_A)*dt
    time.append(t)
    NA.append(A)
    NB.append(B)
print time
print NA
print NB

