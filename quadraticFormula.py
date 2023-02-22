import math

#this program solves a quadratic equation using the quadratic formula

print("ax^2+bx+c is the reference equation");
a=int(input("enter the a coefficient: "));
b=int(input("enter the b coefficient: "));
c=int(input("enter the c coefficient: "));

negb=int((b*-1));#is the negative b

bsquared=b*b;#is b squared 

fourAC=4*a*c;#calculates 4*a*c without root

inroot=bsquared-fourAC;#is b squared - 4*a*c to prepare for root

underhalf=2*a;#is the 2*a under fraction bar

positive=int((negb+inroot)/underhalf); #solves for upper bound answer
negative=int((negb-inroot)/underhalf); #solves for lower bound answer

print("x is ",positive); #prints result
print("or x is ",negative); # print result



