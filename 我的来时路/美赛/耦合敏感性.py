import numpy as np
import matplotlib.pyplot as plt

# 全局配置（O奖级，学术精致、跨平台兼容）
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['lines.linewidth'] = 1.8
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.facecolor'] = '#F8F9FA'  # 浅灰背景，提升高级感
plt.rcParams['grid.color'] = '#E9ECEF'

# 核心数据（与前文闭环，所有耦合影响率<1%）
# param_pairs = ['($\lambda$, $\\alpha$(T))', '($\lambda$, $k$(cycle))', '($\lambda$, $\\beta$)',
#                '($\\alpha$(T), $k$(cycle))', '($\\alpha$(T), $\\beta$)', '($k$(cycle), $\\beta$)']
# game_coupling_rate = [0.90, 0.85, 0.78, 0.62, 0.55, 0.48]
# video_coupling_rate = [0.82, 0.76, 0.70, 0.58, 0.50, 0.42]
# standby_coupling_rate = [0.60, 0.55, 0.49, 0.40, 0.35, 0.30]

param_pairs = ['($\lambda$, $\\alpha$(T))', '($\lambda$, $k$(cycle))',
               '($\\alpha$(T), $k$(cycle))']
game_coupling_rate = [0.90, 0.85,  0.62,]
video_coupling_rate = [0.82, 0.76,  0.58 ]
standby_coupling_rate = [0.60, 0.55,  0.40 ]

# O奖级配色（低饱和度、和谐统一，避免撞色）
colors = ['#2E86AB', '#A23B72', '#F18F01']  # 蓝/紫/橙，学术期刊常用
alpha_val = 0.8  # 透明度，提升层次感

# 绘图：分组柱状图（O奖级细节）
x = np.arange(len(param_pairs))
width = 0.25

fig, ax = plt.subplots()
# 绘制柱状图，增加细腻边框和透明度
bars1 = ax.bar(x - width, game_coupling_rate, width, label='Game Scenario',
               color=colors[0], alpha=alpha_val, edgecolor='#1A5F7A', linewidth=0.7)
bars2 = ax.bar(x, video_coupling_rate, width, label='Video Scenario',
               color=colors[1], alpha=alpha_val, edgecolor='#712A55', linewidth=0.7)
bars3 = ax.bar(x + width, standby_coupling_rate, width, label='Standby Scenario',
               color=colors[2], alpha=alpha_val, edgecolor='#C06C00', linewidth=0.7)

# 标注数值（O奖级对齐，字体精致，无重叠）
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.015,
                f'{height:.2f}%', ha='center', va='bottom', fontsize=8,
                color='#212529', fontweight='light')

# 绘制1%临界线（O奖级视觉强化，加文字标注）
ax.axhline(y=1.0, color='#212529', linestyle='--', linewidth=1.5, label='1% Critical Threshold')
ax.text(len(param_pairs)-0.5, 1.02, 'Critical Threshold (1%)', ha='center',
        va='bottom', fontsize=9, color='#212529', style='italic')

# 坐标轴与标题（O奖级层级，标题加粗，提升辨识度）
ax.set_xlabel('Core Parameter Pairs', fontsize=12, fontweight='bold', color='#212529')
ax.set_ylabel('Coupling Influence Rate (%)', fontsize=12, fontweight='bold', color='#212529')
ax.set_title('Coupling Influence Rate of Parameter Pairs Across Three Typical Usage Scenarios',
             fontsize=14, fontweight='bold', pad=20, color='#212529')
ax.set_xticks(x)
ax.set_xticklabels(param_pairs, rotation=15, ha='right')  # 旋转对齐，避免重叠
ax.set_ylim(0, 1.15)  # 预留空间，提升美观度
ax.grid(axis='y', linestyle='-', alpha=0.7)  # 仅纵向网格，更干净

# 图例（O奖级，带阴影，位置优化）
ax.legend(loc='upper right', fontsize=10, frameon=True, shadow=True, facecolor='white', framealpha=0.9)

# 去除顶部和右侧边框（O奖级简约风格）
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#DEE2E6')
ax.spines['bottom'].set_color('#DEE2E6')

# 仅显示图表（符合受限环境要求）
plt.tight_layout()
plt.show()