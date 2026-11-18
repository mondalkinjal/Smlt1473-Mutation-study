import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os

def load_hydrogen_bond_data(directory):
    try:
        h_bond_path = os.path.join(directory, "h_bondlist.npy")
        h_list_path = os.path.join(directory, "h_residues.npy")

        # Load h_bond.npy
        h_bond = np.load(h_bond_path)
        print(f"h_bond original shape for {directory}:", h_bond.shape)

        if h_bond.ndim != 2:
            print(f"Error: 'h_bond.npy' in '{directory}' is not a 2D array.")
            return None, None

        h_bond = h_bond.T
        h_bond_reduced = h_bond[1:, :]  # Exclude the first row (if it's not relevant)
        print(f"h_bond_reduced shape for {directory}:", h_bond_reduced.shape)

        # Load h_list.npy and process residue IDs
        h_list = np.load(h_list_path)
        h_list = h_list.tolist() if not isinstance(h_list, list) else h_list
        h_list_processed = [int(str(item)[3:]) + 21 for item in h_list]  # Adjust residue IDs

        return h_bond_reduced, h_list_processed

    except Exception as e:
        print(f"Error loading hydrogen bond data from '{directory}': {e}")
        return None, None

def plot_hydrogen_bonds(data_list, labels, output_image='hydrogen_bonds_comparison.png'):
    num_datasets = len(data_list)
    fig, axs = plt.subplots(3, 2, figsize=(16, 18), sharex=True)  # 3 rows, 2 columns
    axs = axs.flatten()

    bounds = [0, 0.5, 1.5]
    colors_list = ["blue", "black"]  # Blue: bond present, Black: no bond
    cmap = colors.ListedColormap(colors_list)
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Create custom legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='s', color='w', label='Hydrogen Bond Present', markerfacecolor='blue', markersize=10),
        Line2D([0], [0], marker='s', color='w', label='No Hydrogen Bond', markerfacecolor='black', markersize=10)
    ]

    alphabet_labels = ["A", "B", "C", "D", "E", "F"]  # Alphabetical subplot labels

    for idx, ((h_bond, h_list_processed), label) in enumerate(zip(data_list, labels)):
        ax = axs[idx]
        subplot_label = f"{label}"

        if h_bond is None or h_list_processed is None:
            ax.text(0.5, 0.5, 'No Data', horizontalalignment='center', verticalalignment='center', fontsize=14)
            ax.set_title(subplot_label, fontweight='bold')
            ax.set_xlabel("time (ns)", fontsize=12, fontweight='bold')
#            if idx % 2 == 0:
            ax.set_ylabel("residue", fontsize=12, fontweight='bold')
            continue

        num_frames, num_residues = h_bond.shape
        time = np.arange(num_frames) / 10.0  # Time scaling

        # Prepare data for scatter plot
        x = np.repeat(time, num_residues)
        y_indices = np.tile(np.arange(num_residues), num_frames)
        z = h_bond.flatten()

        residue_ids = [str(resid) for resid in h_list_processed]
        sc = ax.scatter(x, y_indices, c=z, cmap=cmap, norm=norm, s=5, alpha=0.7)

        # Set y-axis ticks and labels
        tick_step = max(1, num_residues // 20)
        y_ticks = np.arange(0, num_residues, tick_step)
        y_ticklabels = [residue_ids[i] for i in y_ticks]

        ax.set_yticks(y_ticks)
        ax.set_yticklabels(y_ticklabels)

        ax.set_xlabel("time (ns)", fontsize=12, fontweight='bold')
#        if idx % 2 == 0:
        ax.set_ylabel("residue", fontsize=12, fontweight='bold')
        ax.set_title(subplot_label, fontsize=14, fontweight='bold')

        ax.set_ylim(-0.5, num_residues - 0.5)
        ax.set_xlim(time[0], time[-1])

    # Remove unused subplots
    for idx in range(num_datasets, len(axs)):
        fig.delaxes(axs[idx])

    # Add legend
    fig.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 0.05),
               ncol=2, title="Hydrogen Bonds")

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Plot saved as '{output_image}'.")

def main():
    # Define the directories and labels
    current_working_directory = os.getcwd()

    base_directories = [
        os.path.join(current_working_directory, 'hexamana'),
        os.path.join(current_working_directory, 'H221F_hexamana'),
        os.path.join(current_working_directory, 'R312L_hexamana')
    ]
    subdirectories = ['H109', 'NOH109']
    labels = ["A", "B", "C", "D", "E", "F"]

    # Generate list of directories
    directories = [os.path.join(base_dir, sub, 'gromacs') for base_dir in base_directories for sub in subdirectories]

    # Initialize list to store data
    data_list = []

    # Load data for each directory
    for directory, label in zip(directories, labels):
        print(f"Processing directory: {directory}")
        h_bond, h_list_processed = load_hydrogen_bond_data(directory)
        if h_bond is not None and h_list_processed is not None:
            data_list.append((h_bond, h_list_processed))
        else:
            data_list.append((None, None))

    # Plot all datasets
    if data_list:
        plot_hydrogen_bonds(data_list, labels, output_image='hydrogen_bonds_comparison.png')
    else:
        print("No data to plot.")

if __name__ == "__main__":
    main()

