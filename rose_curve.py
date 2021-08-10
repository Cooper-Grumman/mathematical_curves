from numpy import pi,sin,cos,linspace,radians,degrees,lcm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R1,R2 = 4,4
k1,k2 = 2,3
a = 10

t = linspace(0,2*pi,1000)

fig = plt.figure()
ax = plt.axes(xlim=(-8.2,8.2),ylim=(-8.2,8.2))
ax.plot(R1*cos(t), R1*sin(t),color="cyan")

plt.title("Visualisation of Rose Curve by Epicycles")
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.grid()

circle = plt.Circle((0,0), radius=R2, fill=False, color="violet")
line = [plt.plot([],[],color="white")[0] for _ in range(2)]
curve = plt.plot([],[],color="red")[0]

ax.add_artist(circle)
xdata,ydata = [],[]

def animate(t):
    t = radians(t)
    x1,y1 = R1*cos(k1*t), R1*sin(k1*t)
    x2,y2 = R1*cos(k1*t) + R2*cos(-k2*t), R1*sin(k1*t) + R2*sin(-k2*t) 
    
    circle.center = x1,y1
    line[0].set_data([0, x1],[0, y1])
    line[1].set_data([x1, x2],[y1, y2])
    
    xdata.append(x2)
    ydata.append(y2)
    curve.set_data(xdata,ydata)
    
    return line + [curve] + [circle]

n = linspace(0,360,600)
ani = FuncAnimation(fig,animate,frames=n,interval=20,blit=True)
#ani.save("rose_curve.mp4",fps=60)
#print("Complete task")

plt.show()
