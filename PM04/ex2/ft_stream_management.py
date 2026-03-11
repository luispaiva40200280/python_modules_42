from sys import stdin, stdout, stderr


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    # archivist_id = input("Input Stream active. Enter archivist ID: ")
    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    archivist_id = stdin.readline().strip()
    # satus_report = input("Input Stream active. Enter status report: ")
    print("Input Stream active. Enter status report: ", end="", flush=True)
    status_report = stdin.readline().strip()
    print()
    msg_stderr = "Communication channels verified"
    print(f"[STANDERD] Archive status from {(archivist_id)}: " +
          f"{status_report}", file=stdout)
    print(f"[ALERT] System diagnostic: {str(msg_stderr)}", file=stderr)
    print("[STANDARD] Data transmission complete\n", file=stdout)
    active_chanels = 0
    if stdin.readable():
        active_chanels += 1
    if stdout.writable():
        active_chanels += 1
    if stderr.writable():
        active_chanels += 1
    if active_chanels == 3:
        print("Three-channel communication test successful.", file=stdout)
    else:
        print("[ERROR] Channel verification failed.", file=stderr)


if __name__ == "__main__":
    ft_stream_management()
