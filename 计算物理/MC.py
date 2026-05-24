import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

beta_mg = 1.0
H = 5.0
N = 5000
steps = 500000
delta_z = 2.0

z = np.random.uniform(0, H, N)

def potential(z):
    return z

U_total = np.sum(potential(z))

step_record = [0]
U_record = [U_total]

beta = 1.0

for step in range(1, steps+1):
    i = np.random.randint(N)
    z_new = z[i] + np.random.uniform(-delta_z, delta_z)
    if 0 <= z_new <= H:
        delta_U = potential(z_new) - potential(z[i])
        if delta_U < 0 or np.random.rand() < np.exp(-beta * delta_U):
            z[i] = z_new
            U_total += delta_U
    if step % 10 == 0:
        step_record.append(step)
        U_record.append(U_total)

plt.figure(figsize=(10,6))
plt.plot(step_record, U_record, 'r-', lw=0.8, alpha=0.7)
start_bal = int(0.8*len(step_record))
U_avg = np.mean(U_record[start_bal:])
plt.axhline(y=U_avg, color='g', ls='--', label=f'平衡平均势能 = {U_avg:.2f}')
plt.xlabel('蒙特卡洛步数')
plt.ylabel('系统总势能')
plt.title('系统总势能随蒙特卡洛步数的演化（无量纲）')
plt.legend()
plt.grid(alpha=0.3)
plt.show()