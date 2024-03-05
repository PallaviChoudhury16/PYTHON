##rite a program to enter the coefficients of a quadratic equation and findout the roots of the equivalent


a=int(input("enter a value for a: "))
b=int(input("enter a value for b: "))
c=int(input("enter a value for c: "))
D=(b**2)-(4*a*c)
print("The value of discriminant is:",D)
var1=(-b+D**0.5/2*a)
var2=(-b-D**0.5/2*a)
print("The root of this equation are",var1,"and",var2)
