import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml


def parse_yaml(file_path):
    """
    Parses a YAML file and returns its content as a Python dictionary.
    
    :param file_path: Path to the YAML file.
    :return: Parsed content as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def read_csv(file_path):
    """
    Reads a CSV file and returns a DataFrame.
    
    :param file_path: Path to the CSV file.
    :return: DataFrame containing the CSV data.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"No data found in the file: {file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the CSV file: {e}")
        return None

def plot_data(df):
    """
    Plots the data from the DataFrame.
    
    :param df: DataFrame containing the data to plot.
    """
    if df is not None:
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df, x='time', y='dif_x', hue='# particleId', marker='o')
        plt.title('Position in X-direction vs Time for Particles')
        plt.xlabel('Time (s)')
        plt.ylabel('Position in X-direction (m)')
        plt.grid(True)
        plt.show()
    else:
        print("No data to plot.")

if __name__ == "__main__":

    # Parse the file
    yaml_file_path = "config.yaml"
    config = parse_yaml(yaml_file_path)

    file = read_csv(config['file'])
    if file is not None:
        df = pd.DataFrame(file)
        plot_data(df)
    else:
        print("No data available to plot.")

    # plt.tight_layout()
    # plt.show()
