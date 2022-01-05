import matplotlib.pyplot as plt
import numpy as np
 
 
def get_rotation_matrix(rad):
    """
    指定したradの回転行列を返す
    """
    rot = np.array([[np.cos(rad), -np.sin(rad)],
                    [np.sin(rad), np.cos(rad)]])
    return rot
 
 
# 始点
base_point = np.array([1, 0])
x_points = []
y_points = []
 
for i in range(0, 12):
    deg = i * 30
    rad = deg * np.pi / 180
    rot = get_rotation_matrix(rad)
    rotated = np.dot(rot, base_point)
    x_points.append(rotated[0])
    y_points.append(rotated[1])
 
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_points, y_points)
ax.grid(True)
 
plt.gca().set_aspect('equal', adjustable='box')
plt.show()