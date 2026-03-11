from importlib import util, metadata
import sys
import os   # noqa: F401


def check_env() -> bool:
    try:
        return sys.base_prefix != sys.prefix
    except Exception as e:
        print(f"error: {e}")
    return False


def verify_module(module: str, description: str) -> dict[str, object] | bool:
    try:
        lib = util.find_spec(module)  # looking for the modules
        version = metadata.version(module)
        return {
            'module': lib,
            'version': version
            }
    except Exception:
        return False


def creation_of_data() -> None:
    try:
        import pandas  # type: ignore # noqa: F401
        import numpy  # type: ignore # noqa: F401
        import matplotlib.pyplot as plt  # type: ignore # noqa: F401
        import requests  # type: ignore # noqa: F401
    except (ImportError, ModuleNotFoundError) as e:
        print(f"Import Error: {e} - Please check your installation.")
        print("Install dependicies:")
        print("Using pip: pip install -r requirements.txt")
        print("Using poetry: ")
        return

    try:
        # geting dunmmy data from an free API
        responce = requests.get("https://jsonplaceholder.typicode.com/users")
        # checking dunmmy data
        responce.raise_for_status()
        # useres data as an dict {json format}
        users_data = responce.json()
        users_names = [user.get("name", "Ubnknown") for user in users_data]
        # generate 100 random ints and 100 names
        random_operators = numpy.random.choice(users_names, 1000)
        random_int_data = numpy.random.randint(1, 1000, 1000)
        dataframe = pandas.DataFrame({
            "name": random_operators,
            "signal": random_int_data
        })
        filename = "matrix_data.json"
        dataframe.to_json(filename, orient="records", indent=4)
        plt.plot(dataframe["signal"], color='red', linewidth=0.6)
        plt.title("Matrix Signel Analysis")
        plt.xlabel("Data Point (Index)")
        plt.ylabel("Signal Strength")
        plt.savefig("matrix_analyses.png")
        print("Analyzing Matrix data...")
        print("Processing 1000 data points...")
        print("Generating visualization...\n")
        print("Analysis complete!\n" +
              "Results saved to: matrix_analysis.png")
        plt.clf()
    except Exception as e:
        print(f"Error: {e}")
        return


def in_matrix() -> None:
    """
    to uninstall dependicies (pip) = pip uninstall -r requirements.txt -y
    """
    print("LOADING STATUS: Loading programs...\n")
    libs: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
        "numpy": "Generating the numerical dummy data"
    }
    libs_not_found: list[str] = []
    for module, description in libs.items():
        verify: dict[str, object] | bool = verify_module(module, description)
        if isinstance(verify, dict):
            print(f"[OK] {module} ({verify['version']}) - {description}")
        else:
            libs_not_found.append(module)
            print(f"[KO] {module} was not found")
    if not libs_not_found:
        print()
        creation_of_data()
    else:
        print("\nERROR: Missing dependencies.")
        print("Please load the programs into your environment:")
        print("Using pip: pip install -r requirements.txt")
        print("Using poetry: poetry install")


def main() -> None:
    env = check_env()
    if not env:
        print("===")
        print("LOADING STATUS: Can't load the progams not in the matrix")
        print("===")
        return
    else:
        in_matrix()


if __name__ == "__main__":
    main()
