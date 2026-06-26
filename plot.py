import matplotlib.pyplot as plt
import numpy as np
import yaml

dirs = ['CellSize_L1_H1', 'CellSize_L1_H2', 'CellSize_L2_H1', 'CellSize_L2_H2']

for dir in dirs:
    with open(f"{dir}/energy.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    fig, ax = plt.subplots()
    for i in range(0, len(data)):
        ax.scatter(data[i]["stress"], data[i]["energy"], c='black')


plt.ylabel("Total Energy")
plt.xlabel("Stress")
plt.title("Peierls stress TaC Edge Dislocation")


plt.savefig("data-plot.png", dpi=300)
plt.show()
