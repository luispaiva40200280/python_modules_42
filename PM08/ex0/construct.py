import sys
import os
import site


def check_if_matrix() -> bool:
    """
    Detects if the script is running inside a virtual environment.
    It does this by comparing the base OS Python path (sys.base_prefix)
    with the currently active Python path (sys.prefix). If they are
    different, a virtual environment is active.
    """
    try:
        return sys.base_prefix != sys.prefix
    except Exception as e:
        print(f"error: {e}")
    return False


def get_pkg_paths() -> str:
    """
    Retrieves the primary directory where pip installs third-party packages.
    Uses the site module to fetch the site-packages list and returns
    the first path, handling any potential exceptions gracefully.
    """
    try:
        pkg_paths = site.getsitepackages()
        return pkg_paths[0]
    except Exception as e:
        return f"Error: {e}"


def main() -> None:
    in_matrix: bool = check_if_matrix()
    # The absolute path to the exact Python program running right now.
    py_path: str = sys.executable
    env_path: str = sys.prefix
    env_name: str = os.path.basename(env_path)
    pkg_paths: str = get_pkg_paths()
    if in_matrix:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {py_path}")
        print(f"Environment Path: {env_path}")
        print(f"Virtual Environment: {env_name}\n")
        print("SUCCESS: You're in an isolated environment! " +
              "Safe to install packages without affecting the global system.")
        print()
        print("Package installation path:\n" + pkg_paths)

    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {py_path}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!\n" +
              "The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("== On unix based system (Linux/Apple)==")
        print("source matrix_env/bin/activate")
        print("== On windows systems==")
        print("matrix_env\\Scripts\\activate")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
