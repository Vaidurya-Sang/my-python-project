import numpy as np
import matplotlib.pyplot as plt

# 全局配置（全英文、无冗余）
plt.rcParams['figure.figsize'] = (6, 4)
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 核心数据（最优优化范围、最大提升率，全英文命名）
scenarios = ['Game', 'Video', 'Standby']
optimal_optimization_range = [10, 8, 0]
max_reasonable_improvement = [21.00, 9.82, 0.00]
colors_optim = ['#E74C3C', '#3498DB', '#2ECC71']
colors_improv = ['#C0392B', '#2980B9', '#27AE60']

# 绘制双柱状图
x = np.arange(len(scenarios))
bar_width = 0.35

fig, ax = plt.subplots()
bars1 = ax.bar(x - bar_width/2, optimal_optimization_range, bar_width,
               label='Optimal Optimization Range (%)', color=colors_optim,
               edgecolor='black', linewidth=0.8)
bars2 = ax.bar(x + bar_width/2, max_reasonable_improvement, bar_width,
               label='Max Reasonable Improvement Rate (%)', color=colors_improv,
               edgecolor='black', linewidth=0.8)

# 标注数值（全英文百分比格式）
for bar, val in zip(bars1, optimal_optimization_range):
    bar_height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., bar_height + 0.3,
            f'{val}%', ha='center', va='bottom', fontsize=8)
for bar, val in zip(bars2, max_reasonable_improvement):
    bar_height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., bar_height + 0.3,
            f'{val:.2f}%', ha='center', va='bottom', fontsize=8)

# 坐标轴与标题（全英文，贴合论文论证）
ax.set_xticks(x)
ax.set_xticklabels(scenarios)
ax.set_ylabel('Percentage (%)', fontsize=11)
ax.set_title('Optimal Optimization Range & Max Battery Life Improvement by Scenario', fontsize=12, pad=15)
ax.set_ylim(0, 23)
ax.legend(loc='upper left', frameon=True, shadow=True)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 仅显示图表（无文件读写）
plt.tight_layout()
plt.show()