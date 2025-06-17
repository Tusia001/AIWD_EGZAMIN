import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
sizes = [20, 30, 17,40, 10, 45, 20]
explode = (0.1, 0, 0.2, 0, 0.1, 0, 0)
colors=['green', 'orange', 'yellow', 'pink', 'purple', 'blue', 'grey']

plt.pie(sizes, explode=explode, labels=labels, colors=colors, startangle=35)
circle = plt.Circle((0, 0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.axis('equal')

plt.text(0, 0, "ABCDE", ha='center', va='center', fontsize=12)


plt.tight_layout()
plt.savefig("zad1.svg", format="svg")

plt.show()