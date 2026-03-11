
import psutil
from time import perf_counter
import os
import random
from typing import Generator


# FIBOONACCI GENORATER
def fibonaci_seq(limits: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(limits):
        yield a
        a, b = b, a + b


# Prime generator
def prime_seq(number: int) -> Generator[int, None, None]:
    count: int = 0
    n: int = 2
    while count < number:
        is_prime: bool = True
        for i in range(2, int(n ** 0.5) + 1):
            if (n % i == 0):
                is_prime = False
                break
        if is_prime:
            yield n
            count += 1
        n += 1


def game_event_generator(limit: int) -> Generator[str, None, None]:
    """Small function that generates a given number of events"""
    names: list[str] = [
        "alice", "bob", "charlie", "dave", "eve", "filips",
        "gui", "hugo", "ines", "john", "kirk", "luis", "mario",
        "nini", "otto", "paulo", "quip", "rat", "stu", "tom",
        "uni", "volt", "watt", "xilo", "yuri", "zed"
        ]
    actions: list[str] = [
        "killed monster", "found treasure", "found a child",
        "leveled up", "joined guild", "got married",
        "offended a dwarf", "built a house", "found a secret"
        ]
    for _ in range(limit):
        name: str = random.choice(names)
        level: int = random.randint(1, 15)
        action: str = random.choice(actions)
        yield f"Player {name} (level {level}) {action}"


def ft_data_stream(count: int = 1000) -> None:
    # see the memory usage at the start
    p: psutil.Process = psutil.Process(os.getpid())
    baseline: float = p.memory_info().rss / 1024 / 1024

    # time of the strt of the program
    start_time: float = perf_counter()
    events_processed: int = 0
    level_up_count: int = 0
    treasure_count: int = 0
    high_lvl_count: int = 0
    stream_events: Generator[str, None, None] = game_event_generator(count)
    print(
        "=== Game Data Stream Processor ===\n"
        f"\nProcessing {count} game events...\n"
    )
    i: int = 0
    iterator: object = iter(stream_events)
    while True:
        try:
            event: str = next(iterator)
            i += 1
            if i <= 3:
                print(f"event {i}: {event}")
            elif i == 4:
                print("----")
            try:
                start: int = event.find("(level ") + 7
                end: int = event.find(")")
                level: int = int(event[start:end])
                if level >= 10:
                    high_lvl_count += 1
            except ValueError:
                pass
            if "found treasure" in event:
                treasure_count += 1
            if "leveled up" in event:
                level_up_count += 1
            events_processed += 1
        except StopIteration:
            break
    # after processor of the events
    end_time: float = perf_counter()
    duration: float = end_time - start_time
    # see the use of the memory
    mem: float = p.memory_info().rss / 1024 / 1024
    diff: float = (mem - baseline)

    print("=== Stream Analytics ===\n"
          f"Total events processed: {events_processed}\n"
          f"High-level players (10+): {high_lvl_count}\n"
          f"Level-up events: {level_up_count}\n"
          )
    if diff == 0:
        print("\nMemory usage: Constant (streaming)\n")
    else:
        print(f"\nMemory usage: {diff} (streaming)\n")
    print(f"Processing time: {duration:.3f} seconds\n")

    fib_nunb: int = 10
    fib_gen: Generator[int, None, None] = fibonaci_seq(fib_nunb)
    itr_fib: object = iter(fib_gen)
    list_n_fib: list = []
    while True:
        try:
            list_n_fib.append(str(next(itr_fib)))
        except StopIteration:
            break

    seq_pr: int = 5
    prime_gen: Generator[int, None, None] = prime_seq(seq_pr)
    prime_iter: object = iter(prime_gen)
    prime_results: list[str] = []
    while True:
        try:
            prime_results.append(str(next(prime_iter)))
        except StopIteration:
            break
    print("=== Generator Demonstration ===\n"
          f"Fibonacci sequence (first {fib_nunb}): {', '.join(list_n_fib)}\n"
          f"Prime numbers (first {seq_pr}): {', '.join(prime_results)}")


if __name__ == "__main__":
    ft_data_stream()
