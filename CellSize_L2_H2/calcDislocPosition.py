from ovito.io import import_file, export_file
from ovito.modifiers import SelectTypeModifier, CommonNeighborAnalysisModifier, DeleteSelectedModifier, ExpressionSelectionModifier


"""
This file uses the Ovito python API to locate and output the position of an edge dislocation within the simulation cell.
This is accomplished by first deleting all carbon atoms, then delecting all atoms in the FCC structure, then selecting atoms
in the center of the simulation cell and calculating the average y-position of the remaining atoms.
"""


def calculate_average_position(input_file):
    pipeline = import_file(input_file)

    pipeline.modifiers.append(SelectTypeModifier(
        operate_on="particles", property="Particle Type", types={"Type 2"}))

    pipeline.modifiers.append(DeleteSelectedModifier())

    data = pipeline.compute()

    pipeline.modifiers.append(CommonNeighborAnalysisModifier())

    pipeline.modifiers.append(SelectTypeModifier(
        operate_on='particles', property='Structure Type', types={"FCC"}))

    pipeline.modifiers.append(DeleteSelectedModifier())

    data = pipeline.compute()

    z_coordinates = data.particles['Position'][:, 2]

    z_min = min(z_coordinates)
    z_max = max(z_coordinates)

    surface_cutoff = 5

    expression = f"Position.Z < {z_min + surface_cutoff} || Position.Z > {z_max - surface_cutoff}"
    pipeline.modifiers.append(
        ExpressionSelectionModifier(expression=expression))

    pipeline.modifiers.append(DeleteSelectedModifier())

    final_data = pipeline.compute()

    y_coordinartes = data.particles['Position'][:, 1]

    average_y_position = sum(y_coordinartes)/len(y_coordinartes)

    return average_y_position


if __name__ == '__main__':
    import glob
    import os
    import matplotlib.pyplot as plt

    dump_files = sorted(
        glob.glob('dump/dump/dump_*.0'),
        key=lambda f: int(os.path.basename(f).split('_')[1].split('.')[0])
    )

    stresses = []
    positions = []

    for f in dump_files:
        stress = int(os.path.basename(f).split('_')[1].split('.')[0])
        positions.append(calculate_average_position(f))
        stresses.append(stress)

    plt.plot(stresses, positions, marker='o', color='black')
    plt.xlabel('Applied Stress (MPa)')
    plt.ylabel('Dislocation Y Position (Å)')
    plt.title('Dislocation Position vs. Applied Stress')
    plt.tight_layout()
    plt.savefig('disloc-position-plot.png', dpi=300)
    plt.show()
