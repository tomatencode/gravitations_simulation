import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import json

def get_sim_data():
    # JSON file
    f = open ('/Users/simonthomas/src/gravitations_simulation/sim_data.json', "r")
    
    # Reading from file
    sim_data = json.loads(f.read())
    return sim_data


def gen_lines(sim_data):
    num_planets = len(sim_data[0])
    dims = len(sim_data[0][0][0])
    frames = len(sim_data)
    lines = []
    for i in range(0,num_planets):
        line = np.empty((dims, frames))
        for j in range(0,frames):
            line[0][j] = sim_data[j][i][0][0]
            line[1][j] = sim_data[j][i][0][1]
            line[2][j] = sim_data[j][i][0][2]
        lines.append(line.copy())

    return lines

def update_lines(num, dataLines, lines) :
    for line, data in zip(lines, dataLines) :
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2,:num])
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines
sim_data = get_sim_data()
data = gen_lines(sim_data)

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

# Setting the axes properties
ax.set_xlim3d([0.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 1.0])
ax.set_zlabel('Z')

ax.set_title('3D Sim')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 3000, fargs=(data, lines),interval=1, blit=False)

plt.show()