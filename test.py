
import sys


def requirements_parser(file_content: str) -> list[list[str]]:
    """Parses a venv requirements.txt file and
    returns list of package dependencies"""

    requirements_packages = []
    for line in file_content.split("\n"):
        operators = (
            "==", ">=", "<=", "~=", "!=", ">", "<", "[", ";", " "
        )
        for ind, operator in enumerate(operators):
            if operator in line:
                op_to_split = operators[ind]
        _ = line.split(op_to_split)
        if len(_) == 2:
            requirements_packages.append(_)
    return requirements_packages


def pyproject_parser(file_content: str) -> list[list[str]]:
    """Parses a poetry pyproject.toml file and
    returns list of package dependencies"""

    requirements_packages = []
    dependencies = ""
    for ind, line in enumerate(file_content.split("\n")):
        if "dependencies=" in line or "dependencies =" in line:
            for _ in file_content.split("\n")[(ind + 1):]:
                if "]" in _:
                    break
                else:
                    dependencies += _
    a = dependencies.replace('"', '')
    print(a)
    b = a.replace(' ', '')
    print(b)
    requirements_packages = b.split(",")
    print(requirements_packages)
    return requirements_packages


if __name__ == "__main__":
    is_requirements = False
    is_pyproject = False

    try:
        with open("requirements.txt", mode='r') as requirements:
            requirements_content = requirements.read()
    except (FileNotFoundError, IsADirectoryError):
        pass
    else:
        is_requirements = True

    try:
        with open("pyproject.toml", 'r') as file:
            content = file.read()
    except (FileNotFoundError, IsADirectoryError):
        pass
    else:
        is_pyproject = True

    if not is_requirements and not is_pyproject:
        print(
            "Error: No dependencies specificator file found. A "
            "'requirements.txt' or 'pyproject.toml' file must be provided"
        )
        sys.exit()


requirements = pyproject_parser(content)
# print(requirements)
