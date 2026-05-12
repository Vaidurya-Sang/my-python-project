import numpy as np
import matplotlib.pyplot as plt

g = 9.8
H = 8000.0
k = 0.0005
v0 = 200.0
theta = 45.0
theta_rad = np.radians(theta)


x0, y0 = 0.0, 0.0
vx0 = v0 * np.cos(theta_rad)
vy0 = v0 * np.sin(theta_rad)
u0 = np.array([x0, y0, vx0, vy0], dtype=float)

dt = 0.01
t_max = 50.0



def f(t, u):
    x, y, vx, vy = u
    v = np.hypot(vx, vy)
    rho_ratio = np.exp(-y / H)
    ax = -k * rho_ratio * vx * v
    ay = -g - k * rho_ratio * vy * v
    return np.array([vx, vy, ax, ay])



t_vals = [0.0]
u_vals = [u0.copy()]
while t_vals[-1] < t_max and u_vals[-1][1] >= 0.0:
    t = t_vals[-1]
    u = u_vals[-1]

    k1 = dt * f(t, u)
    k2 = dt * f(t + dt / 2, u + k1 / 2)
    k3 = dt * f(t + dt / 2, u + k2 / 2)
    k4 = dt * f(t + dt, u + k3)

    u_next = u + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    t_next = t + dt

    t_vals.append(t_next)
    u_vals.append(u_next)


u_vals = np.array(u_vals)
x_vals = u_vals[:, 0]
y_vals = u_vals[:, 1]


plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, 'b-', linewidth=1.5, label='Trajectory')
plt.scatter(x_vals[0], y_vals[0], color='green', s=50, label='Start')
plt.scatter(x_vals[-1], y_vals[-1], color='red', s=50, label='Impact')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.tight_layout()
plt.show()