from sympy import *
#problem 1
x=Symbol('x')
y=Symbol('y')
f=(x**2*y**3+x**4*y)
f_x=diff(f,x,1)
f_y=diff(f,y,1)
print(f_x)
print(f_y)

LHS=x*f_x+y*f_y
RHS=5*f
print("LHS=",LHS)
print("RHS=",RHS)

sfx=simplify(LHS)
sfy=simplify(RHS)
print("Simplified LHS=",sfx)
print("Simplified RHS",sfy)
if sfx==sfy:
    print("Same")
else:
    print("Not same")

#problem 2
x=Symbol('x')
y=Symbol('y')
h=x**3*y+x*y**3
h_x=diff(h,x,1)
h_y=diff(h,y,1)
print('\n',h_x)
print(h_y)

LHS=x*h_x+y*h_y
RHS=4*h
print("LHS=",LHS)
print("RHS=",RHS)

h_l=simplify(LHS)
h_r=simplify(RHS)
print("Simplified LHS=",h_l)
print("Simplified RHS=",h_r)

if h_l==h_r:
    print("Same")
else:
    print("Not same")

#problem 3
h=x**2*y**2+x*y**4
h_x=diff(h,x,1)
h_y=diff(h,y,1)
print(h_x)
print(h_y)

LHS=x*h_x+y*h_y
RHS=4*h
print("LHS=",LHS)
print("RHS=",RHS)

h_l=simplify(LHS)
h_r=simplify(RHS)
print("Simplified LHS=",h_l)
print("Simplified RHS=",h_r)

if h_l==h_r:
    print("Same")
else:
    print("Not same")

