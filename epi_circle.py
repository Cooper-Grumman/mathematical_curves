"""
epi-cycle
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

theta_array = np.linspace(0, 2 * np.pi, 1000)


def circle(x0, y0, r):
    return (r * np.cos(theta_array) + x0,
            r * np.sin(theta_array) + y0)

fig = plt.figure()
fig.set_size_inches(12, 12, True)
ax = plt.axes(xlim=(-3, 6), ylim=(-3, 3))
ax.set_aspect('equal', 'datalim')
Lines = [ax.plot([], [])[0] for _ in range(10)]
Lines.append(ax.plot([], [], color='black')[0])  # trace line
TraceLineData = [[], []]

def update(frame_count=0):
    x_0 = 0
    y_0 = 0
    radius = 1
    radius_factor = 0.75
    for i in range(0, 10):
        circle_xy = circle(x_0, y_0, radius)
        Lines[i].set_data(*circle_xy)
        #plt.plot(*np.copy(circle_xy))
        next_frame = int(frame_count * 2 * i % 1000)
        x_0, y_0 = circle_xy[0][next_frame], circle_xy[1][next_frame]
        if i == 9:
            TraceLineData[0].append(x_0)
            TraceLineData[1].append(y_0)
            Lines[i + 1].set_data(*TraceLineData)
        radius *= radius_factor
    return Lines


anim = animation.FuncAnimation(fig, update, init_func=update,
                               frames=999, interval=20, blit=True)
#anim.save('basic_animation.mp4', fps=60, dpi=100)
plt.show()
