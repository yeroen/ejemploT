from modulo import *
n=input("ingrese su nommbre")
d=1
while(d<10**7 or d>=10**8):
    d=int(input("ingrese su DNI:"))
    if d<10**7 or d>=10**8:
        print("error de DNI")
m=-1
while(m<0):
    m=float(input("ingrese su monto de fondo:"))
    if m<0:
        print("error de monto")

t=input("ingrese tipo de fondo:")
menu(n,d,m,t)
