import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
from matplotlib.lines import Line2D

def load_salt_bridge_data(directory):
    """
    Load salt bridge data from the specified directory.

    Parameters:
    - directory (str): Path to the directory containing 'salt_bridge.npy' and 'salt_list.npy'.

    Returns:
    - tuple: (salt_bridge_array, processed_salt_list) or (None, None) if an error occurs.
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

        # Transpose if necessary (as per your modification)
        salt_bridge = salt_bridge.T
        print(f"salt_bridge transposed shape: {salt_bridge.shape}")

        # Load salt_list.npy and process residue IDs
        salt_list = np.load(salt_list_path)
        print(f"salt_list shape in {directory}: {salt_list.shape}")
        salt_list = salt_list.tolist()

        # Adjust residue IDs (e.g., adding 21)
        salt_list_processed = [int(item) + 21 for item in salt_list]
        print(f"Processed salt_list: {salt_list_processed}")

        return salt_bridge, salt_list_processed

    except Exception as e:
        print(f"Error loading salt bridge data from '{directory}': {e}")
        return None, None

def plot_salt_bridges(data_list, labels, output_image='salt_bridges.png'):
    """
    Plot salt bridges for multiple datasets without individual subplot legends.
    A single legend is added for the entire figure.

    Parameters:
    - data_list (list): List of tuples containing (salt_bridge_array, processed_salt_list) for each dataset.
    - labels (list): List of labels corresponding to each dataset.
    - output_image (str): Filename for the saved plot image.
    """
    num_datasets = len(data_list)
    fig_rows = (num_datasets + 1) // 2  # Calculate the number of rows needed for subplots
    fig, axs = plt.subplots(fig_rows, 2, figsize=(16, fig_rows * 6))
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
        ax_salt = axs[idx]
        label = labels[idx]
        subplot_label_salt = f"{label}"

        if salt_bridge is not None and salt_list_processed is not None:
            num_frames_salt, num_residues_salt = salt_bridge.shape
            time_salt = np.arange(num_frames_salt) / 10.0  # Adjust time scaling if needed
            x_salt = np.repeat(time_salt, num_residues_salt)
            y_indices_salt = np.tile(np.arange(num_residues_salt), num_frames_salt)
            z_salt = salt_bridge.flatten()

            # Create scatter plot
            sc_salt = ax_salt.scatter(x_salt, y_indices_salt, c=z_salt, cmap=salt_cmap,
                                      norm=salt_norm, s=5, alpha=0.7)

            # Set y-axis ticks and labels without rotation
            tick_step_salt = max(1, num_residues_salt // 20)
            y_ticks_salt = np.arange(0, num_residues_salt, tick_step_salt)
            y_ticklabels_salt = [str(salt_list_processed[i]) for i in y_ticks_salt]
            ax_salt.set_yticks(y_ticks_salt)
            ax_salt.set_yticklabels(y_ticklabels_salt)  # Removed rotation and horizontal alignment

            # Set labels and title
            ax_salt.set_xlabel("time (ns)", fontsize=12, fontweight='bold')
            ax_salt.set_ylabel("residue", fontsize=12, fontweight='bold')
            ax_salt.set_title(subplot_label_salt, fontsize=14, fontweight='bold')

        else:
            # If data is missing, display a message
            ax_salt.text(0.5, 0.5, 'No Salt Bridge Data', horizontalalignment='center',
                         verticalalignment='center', fontsize=14)
            ax_salt.set_title(subplot_label_salt, fontweight='bold')
            ax_salt.set_xlabel("Time (ns)", fontsize=12, fontweight='bold')
            ax_salt.set_ylabel("Residue", fontsize=12, fontweight='bold')

    # Remove any unused subplots
    for idx in range(len(data_list), len(axs)):
        fig.delaxes(axs[idx])

    # Add a single legend for the entire figure at the bottom
    fig.legend(handles=salt_legend_elements, loc='lower center', ncol=2, title='Salt Bridge', fontsize=12)

    # Adjust layout to make space for the legend at the bottom
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # Leave space at the bottom

    plt.savefig(output_image, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Plot saved as '{output_image}'.")

def main():
    """
    Main function to load salt bridge data from multiple directories and plot them.
    """
    # Define the directories and labels
    current_working_directory = os.getcwd()
    directories = [
        os.path.join(current_working_directory, 'tetraha', 'H123', 'gromacs'),
        os.path.join(current_working_directory, 'tetraha', 'NOH123', 'gromacs'),
        os.path.join(current_working_directory, 'H221F_tetraha', 'H123', 'gromacs'),
        os.path.join(current_working_directory, 'H221F_tetraha', 'NOH123', 'gromacs')
    ]
    labels = ['A', 'B', 'C', 'D']  # Labels for each dataset

    # Initialize list to store data
    data_list = []

    # Loop over directories to load data
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

