import numpy as np
import matplotlib.pyplot as plt

# 全局配置（O奖级，精致简约，无冗余）
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.facecolor'] = '#F8F9FA'

# 核心数据（与前文闭环，场景×参数二维矩阵，无冗余）
scenarios = ['Game', 'Video', 'Standby']
# 修正：规范mathtext语法，简化\text{}内部格式，消除解析歧义
params = [
     r'$\lambda \text{ (Power Consumption)}$',
    r'$\alpha \text{ (T) (Temperature)}$',
    r'$k \text{ (cycle) (Aging)}$'
    # r'$\beta \text{ (Self-Discharge)}$'
]
# 敏感性指数矩阵：[场景][参数]，与前文完全一致
# sensitivity_matrix = np.array([
#     [2.100, 0.680, 0.420, 0.030],  # Game场景
#     [1.228, 0.564, 0.368, 0.025],  # Video场景
#     [1.041, 0.410, 0.300, 0.100]   # Standby场景
# ])
sensitivity_matrix = np.array([
     [2.100, 0.680, 0.420],  # Game场景
     [1.228, 0.564, 0.368],  # Video场景
     [1.041, 0.410, 0.300]   # Standby场景
 ])

# O奖级配色（渐变配色，直观反映数值大小，学术期刊常用）
cmap = 'YlOrRd'  # 黄-橙-红渐变，数值越高颜色越深
alpha_val = 0.9

# 绘图：热力图（非柱/非线，O奖级核心风格）
fig, ax = plt.subplots()

# 绘制热力图核心区域
im = ax.imshow(sensitivity_matrix, cmap=cmap, alpha=alpha_val, aspect='auto')

# 标注每个单元格的具体数值（O奖级，精准对齐，字体精致，无重叠）
for i in range(len(scenarios)):
    for j in range(len(params)):
        text = ax.text(j, i, f'{sensitivity_matrix[i, j]:.3f}',
                       ha="center", va="center", color="#212529", fontsize=9, fontweight='light')

# 坐标轴与标题（O奖级，层级分明，加粗醒目，避免文字重叠）
ax.set_xticks(np.arange(len(params)))
ax.set_yticks(np.arange(len(scenarios)))
ax.set_xticklabels(params, rotation=15, ha='right', fontsize=10)
ax.set_yticklabels(scenarios, fontsize=10)
ax.set_xlabel('Core Model Parameters', fontsize=12, fontweight='bold', color='#212529', labelpad=10)
ax.set_ylabel('Usage Scenarios', fontsize=12, fontweight='bold', color='#212529', labelpad=10)
ax.set_title('Sensitivity Index Heatmap of Parameters Across Three Usage Scenarios',
             fontsize=14, fontweight='bold', pad=20, color='#212529')

# 添加颜色条（O奖级，解释颜色含义，提升信息完整性）
cbar = fig.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Sensitivity Index', fontsize=10, fontweight='bold', color='#212529', labelpad=10)

# 去除顶部和右侧边框（O奖级简约风格，提升高级感）
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#DEE2E6')
ax.spines['bottom'].set_color('#DEE2E6')

# 仅显示图表（符合受限环境要求，无文件读写，直接运行弹出）
plt.tight_layout()
plt.show()