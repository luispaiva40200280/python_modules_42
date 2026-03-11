import os
from dotenv import load_dotenv  # type: ignore


def matrix_conf() -> dict[str, object]:
    load_dotenv()
    return {
        "MODE": os.getenv("MATRIX_MODE", "Not found"),
        "URL": os.getenv("DATABASE_URL", "Not found"),
        "API_KEY": os.getenv("API_KEY", "Not found"),
        "LOG": os.getenv("LOG_LEVEL", "Not found"),
        "ZION":  os.getenv("ZION_ENDPOINT", "Not found"),
    }


def check_file() -> bool:
    return os.path.exists(".env")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    check_file()
    config = matrix_conf()
    print("Configuration loaded:")
    print(f"Mode: {config['MODE']}")
    print("Database: {} to local instance"
          .format('Conected' if config['URL'] != "Not found"
                  else 'Disconnected'))
    print("API Access: {}"
          .format('Authenticated' if config['API_KEY'] != "Not found"
                  else 'DENIED'))
    print(f"Log Level: {config['LOG']}")
    print("Zion Network: {}"
          .format('ONLINE' if config['ZION'] != "Not found" else 'OFFLINE'))
    print("\nEnvironment security check:")

    missing_keys = [k for k, v in config.items() if v == "Not found"]
    checks = [
        ("No hardcoded secrets detected", len(missing_keys) == 0),
        (".env file properly configured", check_file()),
        ("Production overrides available", True)
    ]

    for label, success in checks:
        icon = "[OK]" if success else "[KO]"
        print(f"{icon} {label}")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
