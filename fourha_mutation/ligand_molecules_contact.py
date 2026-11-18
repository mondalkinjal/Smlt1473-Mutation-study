import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os

def compute_contacts(u, distance_threshold=3.0):
    sugar_residues = u.select_atoms('resname BGLCN BGLCA').residues
    sugar_residue_ids = [residue.resid for residue in sugar_residues]
    protein_heavy_atoms = u.select_atoms('protein and not name H*')

    num_frames = len(u.trajectory)
    num_sugar_residues = len(sugar_residues)

    contacts_array = np.zeros((num_frames, num_sugar_residues), dtype=int)

    for frame_idx, ts in enumerate(u.trajectory):
        protein_positions = protein_heavy_atoms.positions
        for res_idx, residue in enumerate(sugar_residues):
            sugar_positions = residue.atoms.positions
            distances = mda.lib.distances.distance_array(sugar_positions, protein_positions, box=ts.dimensions)
            contacts = distances < distance_threshold
            num_contacts = np.count_nonzero(contacts)
            contacts_array[frame_idx, res_idx] = num_contacts

    time = np.arange(num_frames) / 10.0  # Adjust time scaling if needed
    return contacts_array, time, sugar_residue_ids

def plot_contacts(data_list, time_list, residue_ids_list, labels, output_image='sugar_protein_contacts_all.png'):
    num_datasets = len(data_list)
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))
    axs = axs.flatten()

    # Adjust bounds and colors based on your data range
    bounds = [0, 3, 6, 9, 12, 15, 30]  # Adjusted bounds for data up to 30
    colors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple']  # Corresponding colors
    cmap = mcolors.ListedColormap(colors)
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    for idx, (data, time, residue_ids, label) in enumerate(zip(data_list, time_list, residue_ids_list, labels)):
        ax = axs[idx]

        num_frames, num_residues = data.shape

        # Create arrays for scatter plot
        x = []
        y = []
        z = []
        for i in range(num_frames):
            for j in range(num_residues):
                x.append(time[i])
                y.append(residue_ids[j])
                z.append(data[i, j])

        # Create scatter plot with custom colormap and normalization
        sc = ax.scatter(x, y, c=z, cmap=cmap, norm=norm, s=5)

        ax.set_title(f"{label}", fontsize=14, fontweight='bold')

        # Set x and y labels
        ax.set_xlabel('time (ns)', fontsize=12, fontweight='bold')
        ax.set_ylabel('unit', fontsize=12, fontweight='bold')

        # Set y-axis ticks and labels
        tick_step = max(1, len(residue_ids) // 10)
        y_ticks = residue_ids[::tick_step]
        y_ticklabels = ['1','2','3','4','5','6','7','8']
        ax.set_yticks(y_ticks)
        ax.set_yticklabels(y_ticklabels)

    # Remove any unused subplots
    for idx in range(len(data_list), len(axs)):
        fig.delaxes(axs[idx])

    # Adjust layout to accommodate labels
    plt.subplots_adjust(wspace=0.3, hspace=0.4, right=0.85)

    # Add a single colorbar for all plots
    cbar_ax = fig.add_axes([0.87, 0.15, 0.03, 0.7])  # Adjust position as needed
    cbar = fig.colorbar(sc, cax=cbar_ax, boundaries=bounds, ticks=bounds)
    cbar.set_label('Number of Contacts', fontsize=12, fontweight='bold')


#    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Plot saved as '{output_image}'.")

# Main script
if __name__ == '__main__':
    # Define the directories and labels
    current_working_directory = os.getcwd()
    directories = [
        os.path.join(current_working_directory, 'fourha', 'H123', 'gromacs'),
        os.path.join(current_working_directory, 'fourha', 'NOH123', 'gromacs'),
        os.path.join(current_working_directory, 'H221F_fourha', 'H123', 'gromacs'),
        os.path.join(current_working_directory, 'H221F_fourha', 'NOH123', 'gromacs')
    ]
    labels = ['A', 'B', 'C', 'D']  # Labels for each dataset

    # Initialize lists to store data
    data_list = []
    time_list = []
    residue_ids_list = []

    # Loop over directories
    for directory, label in zip(directories, labels):
        print(f"Processing directory: {directory}")
        # Change to the directory
        original_cwd = os.getcwd()
        os.chdir(directory)

        # Define the paths to your files
        gro_file = 'protein_ligand.gro'
        xtc_file = 'final_production.xtc'

        # Load the universe
        u = mda.Universe(gro_file, xtc_file)

        # Compute contacts
        contacts_array, time, sugar_residue_ids = compute_contacts(u)

        data_list.append(contacts_array)
        time_list.append(time)
        residue_ids_list.append(sugar_residue_ids)

        # Return to the original directory
        os.chdir(original_cwd)

    # Plot all datasets
    if data_list:
        plot_contacts(data_list, time_list, residue_ids_list, labels)

