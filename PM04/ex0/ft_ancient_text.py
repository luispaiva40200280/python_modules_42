def ft_ancient_text(name: str) -> str | None:
    try:
        file = open(name, "r", encoding="utf-8")
        content: str | None = file.read()
        file.close()
        return content
    except FileNotFoundError:
        return


def main() -> None:
    file_name: str = "ancient_fragment.txt"
    content: str | None = ft_ancient_text(file_name)
    if not content:
        print()
        print("ERROR: Storage vault not found. Run data generator first")
    else:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()
        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(content)
        print()
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
