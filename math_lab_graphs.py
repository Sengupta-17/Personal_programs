import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,30,1000)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Sine Curve")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,2,1000)
y=2*x+1
plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Straight Line")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
plt.axes()
Circle=plt.Circle((0,0), radius=2, fc='y')
plt.gca().add_patch(Circle)
plt.axis("Scaled")
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
u=np.linspace(0,2*np.pi,100)
v=np.linspace(0,np.pi,100)
x=10*np.outer(np.cos(u),np.sin(v))
y=10*np.outer(np.sin(u),np.sin(v))
z=10*np.outer(np.ones(np.size(u)),np.cos(v))
ax.plot_surface(x,y,z, rstride=4, cstride=4, color='r')
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from math import sin,cos,pi
z=np.arange(0,1,0.02)
theta=np.arange(0,2*pi+pi/50,pi/50)
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
for zval in z:
    x=zval*np.array([cos(q) for q in theta])
    y=zval*np.array([sin(q) for q in theta])
    ax.plot(x,y, -zval, 'c-')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,1000)
a=5
y1=(a**(2/3)-(x**2)**(1/3))**(3/2)
y2=-(a**(2/3)-(x**2)**(1/3))**(3/2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Astroid Curve")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-2,2,1000)
a=2
y1=(x**2-(x**4/a**2))**(1/2)
y2=-(x**2-(x**4/a**2))**(1/2)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Lemniscate")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(-2*np.pi,2*np.pi,1000)
a=2
y=a*(np.cosh(theta/a))
plt.plot(theta,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Catenary")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
theta=np.linspace(-2*np.pi,2*np.pi,1000)
a=4
x=a*(theta-np.sin(theta))
y=a*(1-np.cos(theta))
plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Cycloid")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
ax=plt.subplot(111, projection='polar')
theta=np.linspace(0,2*np.pi,100)
a=2
r=a*(1+np.cos(theta))
ax.plot(theta,r)
plt.title("Cardoid")
plt.show()

import matplotlib.pyplot as plt
import numpy as np
ax=plt.subplot(111, projection='polar')
theta=np.linspace(0,2*np.pi,100)
a=2
r=a*np.sin(3*theta)
ax.plot(theta,r)
plt.title("Three Leaved Rose")
plt.show()