from numpy import pi,sin,cos,linspace,radians,degrees,lcm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

r = 10
R = 2*r
d = r
a = 21

t = linspace(0,2*pi,1000)

theta = int(degrees(2*pi * (lcm(R,r)/R)))

angle = linspace(0,2*pi,10,endpoint=True)

def liner(R,r,phi,t):
    x = (R-r)*cos(t + phi) + d*cos(((R-r)/r)*(t)) 
    y = (R-r)*sin(t + phi) - d*sin(((R-r)/r)*(t))
    return x,y

fig = plt.figure()
ax = plt.axes(xlim=(-a,a),ylim=(-a,a))

plt.title("CIRCLE ILLUSION")
ax.set_facecolor("black")
ax.set_aspect("equal")

ax.plot(R*cos(t),R*sin(t),color="White")

for i in range(len(angle)):
    x = angle[i]
    plt.plot([R*cos(x),R*cos(x+pi)],[R*sin(x),R*sin(x+pi)],color="white",lw=0.5)

dot = [plt.plot([],[],"o",color="red")[0] for _ in range(len(angle))]
def animate(t):
    t = radians(t) 
    
    for i in range(len(angle)):
        x,y = liner(R,r,angle[i],t)
        dot[i].set_data([x],[y])
    return dot

ani = FuncAnimation(fig,animate,frames=2*theta,interval=20,blit=True)
ani.save("circle_illusion.mp4")
print("Complete task")
#plt.show()