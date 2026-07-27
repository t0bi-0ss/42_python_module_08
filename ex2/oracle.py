"""
Module that demonstrates the use of enviroment variables
"""

import os

import sys

        
def show_config() -> None:
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

        mode = os.getenv('MATRIX_MODE')
        if str(mode) in ["production", "development"]:
            print(f"Mode: {os.getenv('MATRIX_MODE')}")

            connected = "Connected" if os.getenv('DATABASE_URL')\
            else "Not connected"
            print(f"Database: {connected} to local instance")

            access = "Authenticated" if os.getenv('API_KEY')\
            else "Not authenticated"
            print(f"API Access: {access}")

            log = str(os.getenv('MATRIX_MODE'))
            level = "DEBUG" if "development" in log else "INFO"
            print(f"Log Level: {level}")

            online = "Online" if os.getenv('ZION_ENDPOINT') \
            else "Offline"
            print(f"Zion Network: {online}")
        else:
            print("[ERROR] Mode not recognized or set")
            print("\nORACLE STATUS: closing...")


def security_check() -> None:
    """
    Makes an environment security check
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
        print("\nEnviroment security check:")
        load_dotenv()

    secrets = False
    properly = True
    override = True
    env_variables = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]

    for var in env_variables:
        if "default" in str(os.getenv(var, "default")):
            secrets = True

        if not os.getenv(var):
            properly = False

        os.environ[var] = "OVERRIDE"
        if os.environ.get(var) != "OVERRIDE":
            override = False

    if secrets:
        print(" [KO] Hardcoded secrets detected")
    else:
        print(" [OK] No hardcoded secrets detected")

    if not properly:
        print(" [KO] .env file is not properly configured")
    else:
        print(" [OK] .env file properly configured")

    if not override:
        print(" [KO] Production override unavailable")
    else:
        print(" [OK] Production override available")




if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    env_vars = show_config()

    security_check()
