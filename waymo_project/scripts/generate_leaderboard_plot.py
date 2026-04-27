import matplotlib.pyplot as plt
import numpy as np

# Data
cities = ['Phoenix', 'San Francisco', 'Austin', 'Los Angeles', 'Miami', 'Atlanta', 'Orlando']
areas = [302, 278, 133, 122, 90, 61, 58]

operators = ['Waymo', 'Zoox']
op_areas = [1044, 15]

# Set up the figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [1, 2]})
fig.patch.set_facecolor('#f8f9fa')

# Colors
waymo_blue = '#1a73e8'
zoox_color = '#34a853'
bar_colors = [waymo_blue] * len(cities)

# Subplot 1: Competitors
ax1.set_facecolor('#f8f9fa')
bars1 = ax1.bar(['Waymo', 'Zoox'], op_areas, color=[waymo_blue, zoox_color])
ax1.set_title('Public Level 4 Robotaxi Service Area', fontsize=14, fontweight='bold', pad=20)
ax1.set_ylabel('Square Miles (mi²)', fontsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 15, f'{int(yval):,} mi²', ha='center', va='bottom', fontweight='bold', fontsize=12)

# Subplot 2: Waymo Cities
ax2.set_facecolor('#f8f9fa')
y_pos = np.arange(len(cities))
bars2 = ax2.barh(y_pos, areas, color=waymo_blue)
ax2.set_yticks(y_pos)
ax2.set_yticklabels(cities, fontsize=12)
ax2.invert_yaxis()  # labels read top-to-bottom
ax2.set_title('Waymo 2026 Fleet Scale by City', fontsize=14, fontweight='bold', pad=20)
ax2.set_xlabel('Square Miles (mi²)', fontsize=12)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(axis='x', linestyle='--', alpha=0.7)

for bar in bars2:
    width = bar.get_width()
    ax2.text(width + 5, bar.get_y() + bar.get_height()/2, f'{int(width)} mi²', ha='left', va='center', fontweight='bold', fontsize=12)

plt.tight_layout(pad=3.0)
plt.savefig('figures/leaderboard_plot.png', dpi=300, bbox_inches='tight', facecolor='#f8f9fa')
print("Plot saved to figures/leaderboard_plot.png")
