from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """ """
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            return False
        else:
            for d in data:
                if type(d) not in (int, float):
                    return False
        return True

    def process(self, data: Any) -> str:
        try:
            if self.validate(data) is False:
                raise ValueError
            lenght: int = len(data)
            total: int | float = sum(d for d in data)
            avg: int | float = total / lenght if data else 0
            output: str = (f"Processed {lenght} numeric values,"
                           + f" sum={total:.1f}, avg={avg:.1f}")
            return super().format_output(output)
        except ValueError:
            return "Error: Invalid numeric Data"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            return False
        else:
            return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError
            else:
                w_count: int = len(data.split())
                c_count: int = len(data)
                output: str = (f"Processed text: {c_count} characters, "
                               + f"{w_count} words")
                return super().format_output(output)
        except ValueError:
            return "Error: Invalid text data"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            return False
        elif ":" not in data:
            return False
        else:
            return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError
            level, message = data.split(":", 1)
            output: str = f"{level} level detected: {message}"
            return super().format_output(output)
        except ValueError:
            return "Unknown log format"


def auto_process(data: Any) -> str:
    # 1. Put all our available tools in a list
    available_processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    # 2. Loop through them
    for processor in available_processors:
        # 3. Ask if they can handle the data
        if processor.validate(data):
            # 4. If yes, process it and stop looking!
            return processor.process(data)

    return "Error: No suitable processor found for this data."


def main() -> None:
    # ---- Initialicing the processors ----#
    proc_numeric: NumericProcessor = NumericProcessor()
    proc_text: TextProcessor = TextProcessor()
    proc_log: LogProcessor = LogProcessor()

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    # --- processing the data for numbers ---- #
    print("Initializing Numeric Processor...")

    numbers = [10, 25, 12]
    numeric = proc_numeric.process(numbers)
    print(f"Processing data: {numbers}")
    # --- see the data already processed for numbers --- #
    if proc_numeric.validate(numbers):
        print("Validation: Numeric data verified")
        print(numeric)
    else:
        print(numeric)

    # --- processing the data for txt ---- #
    print("\nInitializing Text Processor...")

    txt = "Hello Nexus World"
    txt_process = proc_text.process(txt)
    # --- see the data already processed for the text --- #
    print(f"Processing data: {txt}")
    if proc_text.validate(txt):
        print("Validation: Text data verified")
        print(txt_process)
    else:
        print(txt_process)

    # --- processing the data for logs ---- #
    print("\nInitializing log Processor...")

    log = "Error Timeout on loading"
    log_process = proc_log.process(log)
    # --- see the data already processed for the text --- #
    print(f"Processing data: {log}")
    if proc_log.validate(log):
        print("Validation: log entry verified")
        print(log_process)
    else:
        print(log_process)
    print()
    print()
    # Processing multiple data types through same interface...
    print("Processing multiple data types through same interface...")
    print("Result 1 " + auto_process([1, 2, 3]))
    print("Result 2 " + auto_process("Hello World"))
    print("Result 3 " + auto_process("INFO: booting up"))


if __name__ == "__main__":
    main()
