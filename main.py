#Algorithmus, der Sinus mit Hilfe der Taylorreihe berechnet 

def power(a,x): #calculates a^x
    if x==0:
        return 1
    ret = a
    while x > 1:
        ret = ret * a
        x = x-1 
    return ret

def fak(x): #calculates x! 
    ret = x 
    while x > 1:
        x=x-1
        ret=ret*x
    return ret 

x = float(input("Sinus welcher Zahl soll berechnet werden?"))
m = float(15) #Acuracy of the Taylor expansion

a=float(0)
b=float(0)
c=float(0)

n=float(0)
sin = float(0)
while n<=m:      #Formular: a/b * c
    a = power(-1,n) #a=(-1)^n
    b = fak(2*n+1)  #(2n+1)!
    c= power(x,((2*n)+1)) #x^(2n+1)
    sin = sin + ((a/b)*c)
    n=n+1

print(sin)

    
    
