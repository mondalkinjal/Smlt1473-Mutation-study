import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
from matplotlib.lines import Line2D

def load_salt_bridge_data(directory):
    """
    Load salt bridge data from the specified directory.
    """
    try:
        salt_bridge_path = os.path.join(directory, "salt_bridge.npy")
        salt_list_path = os.path.join(directory, "salt_list.npy")

        # Load salt_bridge.npy
        salt_bridge = np.load(salt_bridge_path)
        print(f"salt_bridge shape in {directory}: {salt_bridge.shape}")

        if salt_bridge.ndim != 2:
            print(f"Error: 'salt_bridge.npy' in '{directory}' is not a 2D array.")
            return None, None

        # Transpose the salt_bridge array
        salt_bridge = salt_bridge.T
        print(f"salt_bridge transposed shape: {salt_bridge.shape}")

        # Load salt_list.npy and process residue IDs
        salt_list = np.load(salt_list_path)
        print(f"salt_list shape in {directory}: {salt_list.shape}")
        salt_list = salt_list.tolist()

        # Adjust residue IDs (e.g., adding 21)
        salt_list_processed = [int(item) + 21 for item in salt_list]

        return salt_bridge, salt_list_processed

    except Exception as e:
        print(f"Error loading salt bridge data from '{directory}': {e}")
        return None, None

def plot_salt_bridges(data_list, labels, output_image='salt_bridges.png'):
    """
    Plot salt bridges for multiple datasets.
    """
    num_datasets = len(data_list)
    fig, axs = plt.subplots(3, 2, figsize=(16, 18))  # 3 rows, 2 columns
    axs = axs.flatten()

    # Define colormap for salt bridges
    salt_bounds = [0, 0.5, 1.5]
    salt_colors = ["blue", "black"]
    salt_cmap = colors.ListedColormap(salt_colors)
    salt_norm = colors.BoundaryNorm(salt_bounds, salt_cmap.N)

    # Create custom legend handles
    salt_legend_elements = [
        Line2D([0], [0], marker='s', color='w', label='Salt Bridge Present',
               markerfacecolor='blue', markersize=10),
        Line2D([0], [0], marker='s', color='w', label='No Salt Bridge',
               markerfacecolor='black', markersize=10)
    ]

    for idx, (salt_bridge, salt_list_processed) in enumerate(data_list):
        ax = axs[idx]
        label = labels[idx]

        if salt_bridge is not None and salt_list_processed is not None:
            num_frames, num_residues = salt_bridge.shape
            time = np.arange(num_frames) / 10.0  # Adjust time scaling
            x = np.repeat(time, num_residues)
            y_indices = np.tile(np.arange(num_residues), num_frames)
            z = salt_bridge.flatten()

            # Create scatter plot
            sc = ax.scatter(x, y_indices, c=z, cmap=salt_cmap, norm=salt_norm, s=5, alpha=0.7)

            # Set y-axis ticks and labels
            tick_step = max(1, num_residues // 20)
            y_ticks = np.arange(0, num_residues, tick_step)
            y_ticklabels = [str(salt_list_processed[i]) for i in y_ticks]
            ax.set_yticks(y_ticks)
            ax.set_yticklabels(y_ticklabels)

            # Set labels and title
            ax.set_xlabel("Time (ns)", fontsize=12, fontweight='bold')
            ax.set_ylabel("Residue", fontsize=12, fontweight='bold')
            ax.set_title(f"{label}", fontsize=14, fontweight='bold')

        else:
            # If data is missing
            ax.text(0.5, 0.5, 'No Data', horizontalalignment='center',
                    verticalalignment='center', fontsize=14)
            ax.set_title(f"{label}", fontsize=14, fontweight='bold')
            ax.set_xlabel("Time (ns)", fontsize=12, fontweight='bold')
            ax.set_ylabel("Residue", fontsize=12, fontweight='bold')

    # Remove unused subplots
    for idx in range(len(data_list), len(axs)):
        fig.delaxes(axs[idx])

    # Add a single legend
    fig.legend(handles=salt_legend_elements, loc='lower center', ncol=2, title='Salt Bridge', fontsize=12)

    # Adjust layout to make space for the legend
    plt.tight_layout(rect=[0, 0.05, 1, 1])

    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Plot saved as '{output_image}'.")

def main():
    """
    Main function to load salt bridge data from six directories and plot them.
    """
    # Define the directories and labels
    current_working_directory = os.getcwd()
    base_directories = [
        os.path.join(current_working_directory, 'hexamana'),
        os.path.join(current_working_directory, 'H221F_hexamana'),
        os.path.join(current_working_directory, 'R312L_hexamana')
    ]
    subdirectories = ['H109', 'NOH109']
    labels = ['A', 'B', 'C', 'D', 'E', 'F']  # Simplified labels

    # Generate list of directories
    directories = [os.path.join(base_dir, sub, 'gromacs') for base_dir in base_directories for sub in subdirectories]

    # Initialize list to store data
    data_list = []

    # Load data for each directory
    for directory in directories:
        print(f"Processing directory: {directory}")
        salt_bridge, salt_list_processed = load_salt_bridge_data(directory)
        data_list.append((salt_bridge, salt_list_processed))

    # Plot all datasets
    if data_list:
        plot_salt_bridges(data_list, labels)
    else:
        print("No data to plot.")

if __name__ == "__main__":
    main()

