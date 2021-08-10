import numpy as np
from numpy import exp,pi,sin,cos,lcm
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from math import gcd

r = 6
R = 12
d = -r
a = 20
t = np.linspace(0,2*pi,1000)

theta = int(np.degrees(2*pi * (lcm(R,r)/R)))

fig = plt.figure()
ax = plt.axes(xlim=(-a,a),ylim=(-a,a))

plt.title("Visualisation of Hypotrochoid by Epicycles")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.grid()

ax.plot(R*cos(t),R*sin(t))

circle = plt.Circle((0,0),radius=r,fill=False,color="cyan")
line = plt.plot([],[],color="white")[0]
curve = plt.plot([],[],color="red")[0]

ax.add_artist(circle)
xdata,ydata = [],[]

def animate(t):
    t = np.radians(t) 
    circle.center = (R-r)*cos(t), (R-r)*sin(t)
    
    x1,y1 = (R-r)*cos(t), (R-r)*sin(t)
    x2,y2 = (R-r)*cos(t) + d*cos(((R-r)/r)*t) ,(R-r)*sin(t) - d*sin(((R-r)/r)*t)
    line.set_data([x1,x2],[y1,y2])
    
    xdata.append(x2)
    ydata.append(y2)
    curve.set_data(xdata,ydata)
    return [line] + [curve] + [circle] 



ani = FuncAnimation(fig,animate,frames=theta,interval=10,blit=True)
#ani.save("hypotrochoid.mp4")
#print("Complete task")
plt.show()