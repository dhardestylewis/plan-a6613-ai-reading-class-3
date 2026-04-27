import matplotlib.pyplot as plt
import networkx as nx
import os

os.makedirs('waymo_project/figures', exist_ok=True)

plt.figure(figsize=(6, 4))
categories = ['Pedestrian Injuries', 'Intersection Crashes']
reductions = [92, 96]
bars = plt.bar(categories, reductions, color=['#1f77b4', '#ff7f0e'])
plt.ylabel('Reduction % vs. Human Baseline')
plt.title('Waymo Safety Impact (2026)')
plt.ylim(0, 100)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval - 15, f"{yval}%", ha='center', va='bottom', color='white', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig('waymo_project/figures/safety_plot.png', dpi=300)
plt.close()

plt.figure(figsize=(8, 4))
G = nx.DiGraph()
G.add_edges_from([
    ('Sensors\n(LiDAR/Radar)', 'Perception'),
    ('Perception', 'Prediction'),
    ('Prediction', 'Planning'),
    ('Planning', 'Actuation')
])
pos = {'Sensors\n(LiDAR/Radar)': (0, 0), 'Perception': (1, 0), 'Prediction': (2, 0), 'Planning': (3, 0), 'Actuation': (4, 0)}
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=9, font_weight='bold', edge_color='gray', arrows=True, arrowstyle='-|>', arrowsize=20)
plt.title('Waymo Level 4 Autonomy Stack')
plt.tight_layout()
plt.savefig('waymo_project/figures/tech_dag.png', dpi=300)
plt.close()
