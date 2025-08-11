from sympy import *
from math import *
#some basic commands of matricces
A=Matrix([[2,-1,1],[-1,2,-1],[1,-1,2]])
B=Matrix([[6,6,2],[1,1,3],[6,1,5]])
print(A+B)
print(A*B)
print(2*A+3*B)
print(A*A)

#problems using Cramer's Rule
#problem 1
A=Matrix([[5,2,1],[1,7,-6],[0,3,6]])
B=Matrix([[-1,2,1],[-18,7,-6],[9,3,6]])
C=Matrix([[5,-1,1],[1,-18,-6],[0,9,6]])
D=Matrix([[5,2,-1],[1,7,-18],[0,3,9]])
x=B.det()/A.det()
y=C.det()/A.det()
z=D.det()/A.det()
print("The value of x,y and z are=",x,y,z,"respectively")

#problem 2
A=Matrix([[1,2,-4],[3,-1,2],[5,-3,2]])
B=Matrix([[1,2,-4],[4,-1,2],[-3,-3,2]])
C=Matrix([[1,1,-4],[3,4,2],[5,-3,2]])
D=Matrix([[1,2,1],[3,-1,4],[5,-3,-3]])
x=B.det()/A.det()
y=C.det()/A.det()
z=D.det()/A.det()
print("The value of x,y and z are=",x,y,z,"respectively")

#problem 3
A=Matrix([[6,1,2,3],[1,5,2,1],[1,1,2,1]])
print(A.rref())

#problem 4
B=Matrix([[1,1,3,7],[6,1,2,7],[2,2,6,14],[1,3,4,7]])
print(B.rref())

#problem 5
T=Matrix([[1,1,3],[2,1,3],[6,1,2]])
T_inv=T.inv()
print(T_inv)

#problem 6
A=Matrix([[1,3,-1],[2,-3,1],[1,1,-2]])
B=Matrix([[6],[-3],[1]])
X=A.inv()*B
print("The solution of the system of eqns is:",X)

#problem 7
A=Matrix([[1,-2,3],[2,2,-3],[1,2,3]])
B=Matrix([[-1],[5],[9]])
x=A.inv()*B
print("The solution of the system of eqns is:",x)

#problem 8
A=Matrix([[3,-1,2],[1,-2,3],[2,4,-1]])
B=Matrix([[4],[2],[5]])
x=A.inv()*B
print("The solution of the system of eqns is:",x)

#computation of derivatives
#problem 1
x=Symbol('x')
y=Symbol('y')
F=7*x**5
#1st and 2nd erivative
F_dash=diff(F,x)
F_2=diff(F,x,2)
print(F_dash)
print(F_2)