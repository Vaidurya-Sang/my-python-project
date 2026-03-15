import numpy as np
import matplotlib.pyplot as plt

# 全局配置（全英文、跨平台兼容、无冗余）
plt.rcParams['figure.figsize'] = (6, 4)
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'DejaVu Sans'  # matplotlib内置字体，全环境支持
plt.rcParams['axes.unicode_minus'] = False

# 核心数据（场景、敏感性指数，与原数据一致）
scenarios = ['Game', 'Video', 'Standby']
sensitivity_index = [2.100, 1.228, 1.041]
bar_colors = ['#E74C3C', '#3498DB', '#2ECC71']  # 保持配色一致性

# 绘制柱状图
fig, ax = plt.subplots()
bars = ax.bar(scenarios, sensitivity_index, color=bar_colors, edgecolor='black', linewidth=0.8)

# 标注敏感性数值（英文格式，无中文）
for bar, idx in zip(bars, sensitivity_index):
    bar_height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., bar_height + 0.05,
            f'{idx:.3f}', ha='center', va='bottom', fontsize=9)

# 坐标轴与标题（全英文，专业术语准确）
ax.set_ylabel('Sensitivity Index of Power Consumption Coefficient $\lambda$', fontsize=11)
ax.set_title('Sensitivity Index of $\lambda$ Across Three Usage Scenarios', fontsize=12, pad=15)
ax.set_ylim(0, 2.3)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 仅显示图表（无文件读写，符合受限环境要求）
plt.tight_layout()
plt.show()