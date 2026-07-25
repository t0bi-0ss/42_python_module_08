import sys
import os


# Get packages install path
pkg_install_path = ""
for element in sys.path:
    if "site-package" in element \
            or "dist-package" in element:
        pkg_install_path = element


# Get virtual enviroment name if any
def get_env_name() -> str:
    # If true means a standard venv virtual enviroment is active
    if sys.prefix != sys.base_prefix:
        return os.path.basename(os.path.abspath(sys.prefix))

    # Check for Conda enviroment
    elif "CONDA_DEFAULT_ENV" in os.environ:
        return os.environ["CONDA_DEFAULT_ENV"]

    else:
        return ""


env_name = get_env_name()

if env_name:
    print("\nMATRIX STATUS: Welcome to the construct\n")

    print("Current Python:", sys.executable)
    print(f"Virtual Eviroment: {env_name}")
    print("Eviroment Path:", os.path.abspath(sys.prefix))

    print("\nSUCCESS: You're in an isolated enviroment!")
    print(
        "Safe to install packages without affecting\n"
        "the global system\n"
    )

    print("Package installation Path:")
    print(pkg_install_path)

else:
    print("\nMATRIX STATUS: You're still plugged in\n")

    print("Current Python:", sys.executable)
    print("Virtual Eviroment: None detected\n")

    print(
        "WARNING: You're in the global eviroment!\n"
        " The machines can see everything you install.\n"
    )

    print(
        "To enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\\Scripts\\activate # On Windows\n\n"
        "Then run this program again"
    )
