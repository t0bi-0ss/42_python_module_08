"""
Module that demonstrates the use of enviroment variables
"""

import os

import sys


def show_config() -> dict[str, str]:
    """
    Show configuration accoring to environment variables
    """

    try:
        from dotenv import load_dotenv
    except ImportError:
        print(
            "Error: python-dotenv package is missing.\n"
            "Install with 'pip install python-dotenv'"
        )
        sys.exit(1)
    else:
        print("Configuration loaded:")
        load_dotenv()

    matrix_mode = os.getenv('MATRIX_MODE', 'default')
    database_url = os.getenv('DATABASE_URL', 'default')
    api_key = os.getenv('API_KEY', 'default key')
    log_level = os.getenv('LOG_LEVEL', 'default')
    zion_endpoint = os.getenv('ZION_ENDPOINT', 'default')
    env_variables = {
        "mode": matrix_mode,
        "database": database_url,
        "api_access": api_key,
        "log_level": log_level,
        "zion_network": zion_endpoint}
    for var, value in env_variables.items():
        print(f"{var} : ", end="")
        if "default" in value:
            print(
                f"No value set for '{var}':"
                f" setting to default value '{value}'"
            )
        else:
            print(f"{value}")
    return env_variables


def security_check(env_variables: dict[str, str]) -> None:
    """
    Makes an environment security check
    """

    


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    show_config()

