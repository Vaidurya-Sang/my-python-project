import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# 全局配置（全英文、跨平台兼容）
plt.rcParams['figure.figsize'] = (7, 4)
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 核心数据（参数名、敏感性指数、校准级别均为英文/专业符号）
core_parameters = ['$\lambda$ (Power Consumption)', '$\\alpha$(T) (Temperature)', '$k$(cycle) (Aging)', '$\\beta$ (Self-Discharge)']
sensitivity_index = [2.100, 0.564, 0.368, 0.025]
calibration_levels = ['Precise', 'Simplified', 'Simplified', 'Ignored']
bar_colors = ['#E74C3C', '#F39C12', '#F39C12', '#95A5A6']

# 绘制柱状图
fig, ax = plt.subplots()
bars = ax.bar(core_parameters, sensitivity_index, color=bar_colors, edgecolor='black', linewidth=0.8)

# 标注数值与校准级别（全英文，无中文）
for bar, idx, level in zip(bars, sensitivity_index, calibration_levels):
    bar_height = bar.get_height()
    # 标注敏感性指数
    ax.text(bar.get_x() + bar.get_width()/2., bar_height + 0.05,
            f'{idx:.3f}', ha='center', va='bottom', fontsize=9)
    # 标注校准级别
    ax.text(bar.get_x() + bar.get_width()/2., bar_height/2,
            level, ha='center', va='center', fontsize=8, color='white', fontweight='bold')

# 坐标轴与标题（全英文，专业准确）
ax.set_ylabel('Sensitivity Index', fontsize=11)
ax.set_title('Hierarchical Calibration Strategy for Lithium Battery Core Parameters', fontsize=12, pad=15)
ax.set_ylim(0, 2.3)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 图例（全英文，解释校准级别）
legend_elements = [Patch(facecolor='#E74C3C', label='Precise Calibration'),
                   Patch(facecolor='#F39C12', label='Simplified Calibration'),
                   Patch(facecolor='#95A5A6', label='Ignored Calibration')]
ax.legend(handles=legend_elements, loc='upper right', frameon=True, shadow=True)

# 仅显示图表（无文件读写）
plt.tight_layout()
plt.show()