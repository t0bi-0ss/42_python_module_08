import sys

import importlib.metadata


INSTALL_GUIDE = r"""
┌───────────────────────────────────────────────────────────┐
│                   INSTALLATION GUIDE                      │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  Option 1: Using pip                                      │
│    $ pip install -r requirements.txt                      │
│    $ python3 loading.py                                   │
│                                                           │
│  Option 2: Using Poetry                                   │
│    $ poetry install                                       │
│    $ poetry run python loading.py                         │
│                                                           │
│  pip:    Installs packages globally or in active venv     │
│          Uses requirements.txt for flat listing           │
│                                                           │
│  Poetry: Creates isolated environment automatically       │
│          Uses pyproject.toml with metadata & versions     │
│          Handles dependency resolution and virtualenvs    │
└───────────────────────────────────────────────────────────┘
"""


def check_enviroment() -> None:
    """Checks wether module is run inside a virtual enviroment or not"""

    if sys.prefix != sys.base_prefix:
        if "pypoetry" in str(sys.path):
            name = "Poetry"
        elif "venv" in str(sys.path):
            name = "Venv"
        else:
            name = "Unknown"
        print(f"\t\t>>> Virtual enviroment detected --- Name: {name} <<<")
    else:
        print("\t\t>>> No Virtual enviroment was detected <<<")


def check_dependencies(
        required_dependencies: dict[str, str]) -> bool:
    """Checks if dependencies are effectively installed with
    their respective correct version"""

    distributions = importlib.metadata.distributions()
    installed_packages = {}
    for dist in distributions:
        if dist.metadata['Name'] in required_dependencies.keys():
            installed_packages[dist.metadata['Name']] = dist.version

    print("\n Checking dependencies:\n")
    missing = False
    for key, value in required_dependencies.items():
        if key not in installed_packages:
            print(
                f"  [MISSING] {key} ({value}) - "
                "No installation for required dependency was found"
            )
            missing = True
        elif installed_packages[key] == value:
            print(
                f"  [OK] {key} ({value}) - Ready"
            )
        else:
            print(
                f"  [MISMATCH] {key} ({value}) - "
                "WARNING: installed version differs from required."
                " This could result in a different"
                " behavior than expected"
            )
    if missing:
        print(INSTALL_GUIDE)
        return False
    return True


def data_analysis() -> None:
    # Import needed modules
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # Step 1: Generate a random number of data points (between 50 and 200)
    num_points = np.random.randint(100, 1000)

    print("\nAnalyzing Matrix data...")
    print(f"Processing {num_points} data points...")

    # Step 2: Generate random data values
    time_steps = np.arange(num_points)
    values_1 = np.random.randn(num_points)
    values_2 = np.random.randn(num_points)
    values_3 = np.random.randn(num_points)


    print("Generating visualization...")
    # Step 3: Organize data into a pandas DataFrame
    data_frame = pd.DataFrame({
        'Time': time_steps,
        'Signal_1': values_1,
        'Signal_2': values_2,
        'Signal_3': values_3
    })

    # Step 4: Create the plot using matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(data_frame['Time'], data_frame['Signal_1'], color='cyan', linestyle='-', linewidth=2)
    plt.plot(data_frame['Time'], data_frame['Signal_2'], color='red', linestyle=':', linewidth=2)
    plt.plot(data_frame['Time'], data_frame['Signal_3'], color='green', linestyle='dotted', linewidth=2)


    # Step 5: Customize the visual styling
    plt.title(f'Simulated Matrix Signal ({num_points} Data Points)')
    plt.xlabel('Time Step')
    plt.ylabel('Signal Value')
    plt.grid(True, linestyle='--', alpha=0.6)

    print("\nAnalysis complete!")
    # Step 6: Save the plot to a file and clean up resources
    plt.savefig('matrix_analysis.png')
    print("Results saved to: matrix_analysis.png")
    plt.close()

if __name__ == "__main__":

    check_enviroment()

    print("\nLOADING STATUS: Loading programs...")

    required_dependencies = {
            "numpy": "2.2.6",
            "matplotlib": "3.10.9",
            "pandas": "2.3.3"
        }
    if not check_dependencies(required_dependencies):
        sys.exit()
    data_analysis()    
