import numpy as np
import matplotlib.pyplot as plt

# 全局配置（全英文、轻量化）
plt.rcParams['figure.figsize'] = (7, 4)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 核心数据（全英文命名，量化关系不变）
optimization_range = [0, 5, 8, 10]  # 优化幅度（%）
game_battery_improve = [0, 5*2.100, 8*2.100, 10*2.100]
video_battery_improve = [0, 5*1.228, 8*1.228, 10*1.228]
standby_battery_improve = [0, 5*1.041, 8*1.041, 10*1.041]

# 绘制折线图
fig, ax = plt.subplots()
ax.plot(optimization_range, game_battery_improve, 'o-', color='#E74C3C', label='Game ($S_\lambda$=2.100)')
ax.plot(optimization_range, video_battery_improve, 's-', color='#3498DB', label='Video ($S_\lambda$=1.228)')
ax.plot(optimization_range, standby_battery_improve, '^-', color='#2ECC71', label='Standby ($S_\lambda$=1.041)')

# 标注续航提升率（全英文百分比格式）
for x, y in zip(optimization_range, game_battery_improve):
    ax.text(x, y+0.3, f'{y:.2f}%', ha='center', fontsize=8, color='#E74C3C')
for x, y in zip(optimization_range, video_battery_improve):
    ax.text(x, y+0.3, f'{y:.2f}%', ha='center', fontsize=8, color='#3498DB')
for x, y in zip(optimization_range, standby_battery_improve):
    ax.text(x, y+0.3, f'{y:.2f}%', ha='center', fontsize=8, color='#2ECC71')

# 坐标轴与标题（全英文，逻辑清晰）
ax.set_xlabel('Optimization Range of Power Consumption Coefficient $\lambda$ (%)', fontsize=11)
ax.set_ylabel('Battery Life Improvement Rate (%)', fontsize=11)
ax.set_title('Relationship Between $\lambda$ Optimization and Battery Life Improvement', fontsize=12, pad=15)
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(0, 22)
ax.legend(loc='upper left', frameon=True, shadow=True)
ax.grid(linestyle='--', alpha=0.7)

# 仅显示图表（无文件读写）
plt.tight_layout()
plt.show()