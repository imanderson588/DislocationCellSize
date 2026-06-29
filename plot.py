import matplotlib.pyplot as plt
import numpy as np
import yaml

dirs = ['CellSize_L1_H1', 'CellSize_L1_H2', 'CellSize_L2_H1', 'CellSize_L2_H2']

for dir in dirs:
    with open(f"{dir}/energy.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    fig, ax = plt.subplots()
    stresses = [d["stress"] for d in data if "stress" in d]
    energies = [d["energy"] for d in data if "energy" in d]
    for s, e in zip(stresses, energies):
        ax.scatter(s, e, c='black')


plt.ylabel("Total Energy")
plt.xlabel("Stress")
plt.title("Peierls stress TaC Edge Dislocation")


plt.savefig("data-plot.png", dpi=300)
plt.show()
