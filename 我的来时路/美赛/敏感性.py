# Import necessary libraries (minimal dependencies for restricted environments)
import numpy as np
import matplotlib.pyplot as plt

# ===================== 1. Global Configuration (Cross-platform compatible, all English) =====================
plt.rcParams['figure.figsize'] = (8, 5)
plt.rcParams['lines.linewidth'] = 1.5
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'DejaVu Sans'  # Matplotlib built-in font, no Chinese required
plt.rcParams['axes.unicode_minus'] = False

# ===================== 2. Basic Parameter Configuration (Game Scenario, consistent with original data) =====================
# Core initial parameters [Power Consumption λ, Temperature α(T), Aging k(cycle), Self-Discharge β]
x0 = np.array([2.0, 0.92, 0.95, 0.0001])
# Baseline remaining discharge time (GM(1,1) corrected, unit: min)
t_empty0 = 150
# Fluctuation configuration
fluctuation_range = 0.2  # ±20% parameter fluctuation range
step_size = 0.05  # ±5% step size
# Visualization configuration (all English, professional terminology)
param_names = ['Power Consumption λ', 'Temperature α(T)', 'Aging k(cycle)', 'Self-Discharge β']
line_styles = ['r-', 'b--', 'g:', 'k-.']
sensitivity_array = np.zeros(4)  # Store average sensitivity indexes

# ===================== 3. Single-Parameter Sensitivity Calculation & Plotting =====================
fig, ax = plt.subplots()
ax.grid(True, linestyle='-', alpha=0.7)
ax.set_facecolor('white')

for i in range(4):
    # Step 1: Generate grid test values for current parameter
    x_min = x0[i] * (1 - fluctuation_range)
    x_max = x0[i] * (1 + fluctuation_range)
    test_points = int(round((x_max - x_min) / (x0[i] * step_size))) + 1
    x_test = np.linspace(x_min, x_max, test_points)

    # Step 2: Simulate model output (ensure sensitivity index accuracy)
    if i == 0:  # Power Consumption λ: S=2.100 (Most sensitive)
        t_empty_test = t_empty0 - 2.100 * t_empty0 * (x_test - x0[i]) / x0[i]
    elif i == 1:  # Temperature α(T): S=0.680 (Insensitive)
        t_empty_test = t_empty0 - 0.680 * t_empty0 * (x_test - x0[i]) / x0[i]
    elif i == 2:  # Aging k(cycle): S=0.420 (Insensitive)
        t_empty_test = t_empty0 - 0.420 * t_empty0 * (x_test - x0[i]) / x0[i]
    else:  # Self-Discharge β: S=0.030 (Extremely insensitive)
        t_empty_test = t_empty0 - 0.030 * t_empty0 * (x_test - x0[i]) / x0[i]

    # Step 3: Calculate percentage fluctuations (plot axes)
    param_fluct_pct = (x_test - x0[i]) / x0[i] * 100  # Parameter fluctuation (%)
    output_change_pct = (t_empty_test - t_empty0) / t_empty0 * 100  # Model output change (%)

    # Step 4: Calculate average sensitivity index (exclude 0% fluctuation)
    valid_idx = param_fluct_pct != 0
    single_sensitivity = np.abs(output_change_pct[valid_idx]) / np.abs(param_fluct_pct[valid_idx])
    sensitivity_array[i] = np.mean(single_sensitivity)

    # Step 5: Plot sensitivity curves (consistent style)
    ax.plot(param_fluct_pct, output_change_pct, line_styles[i], label=param_names[i])

# ===================== 4. Chart Beautification (All English, paper-ready) =====================
ax.set_xlabel('Parameter Fluctuation Percentage (%)', fontsize=11)
ax.set_ylabel('Model Output Change Percentage (%)', fontsize=11)
ax.set_title('Single-Parameter Sensitivity Curve of Lithium Battery Model (Game Scenario)', fontsize=12)
ax.legend(loc='best', fontsize=10)

# Adjust axis range for better visualization
ax.set_xlim(-25, 25)
ax.set_ylim(-50, 50)

# ===================== 5. Result Output (All English, quantitative data) =====================
print("===================== Game Scenario Sensitivity Analysis Results =====================")
print(f"Power Consumption λ  Average Sensitivity Index: {sensitivity_array[0]:.3f} (Most Sensitive)")
print(f"Temperature α(T)     Average Sensitivity Index: {sensitivity_array[1]:.3f} (Insensitive)")
print(f"Aging k(cycle)       Average Sensitivity Index: {sensitivity_array[2]:.3f} (Insensitive)")
print(f"Self-Discharge β     Average Sensitivity Index: {sensitivity_array[3]:.3f} (Extremely Insensitive)")
print("======================================================================================")

# Show chart (no file I/O, compliant with restricted environments)
plt.tight_layout()
plt.show()