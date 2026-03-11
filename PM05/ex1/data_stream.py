from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    TYPE: str

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    # - Process a batch of data
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    # - Filter data based on criteria
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"total_processed": 0}


class SensorStream(DataStream):
    TYPE: str = "Environmental Data"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.total_readings: int = 0
        self.temp: float | int = 0.0

    """process a list of data that to see if any data is the wrong type"""
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_readings: List[Union[int, float]] = [
                data for data in data_batch if isinstance(data, (int, float))
            ][:3]
            if not valid_readings:
                raise ValueError("No valid sensor readings found in batch.")

            labels = ["temp", "humidity", "pressure"]
            count = len(valid_readings)
            self.temp = valid_readings[0]

            self.total_readings += count

            format_data = [
                f"{lable}:{value}"
                for lable, value in zip(labels, valid_readings)
            ]

            return (
                f"Processing snesor batch: [{', '.join(format_data)}]\n" +
                f"Sensor analysis: {count} readings processed," +
                f" avg temp: {self.temp:.1f}°C"
            )
        except ValueError as e:
            return f"Sensor error: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        data: List[dict[str, int]] = [
            d for d in data_batch if isinstance(d, dict)
            ]
        match criteria:
            case "temp":
                return [d[criteria] for d in data if criteria in d]
            case "humidity":
                return [d[criteria] for d in data if criteria in d]
            case "pressure":
                return [d[criteria] for d in data if criteria in d]
            case _:
                return data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"total_processed": self.total_readings}


class TransactionStream(DataStream):
    TYPE: str = "Financial Data"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.units: int = 0
        self.total_sum: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_readings: List[dict[str, int]] = [
                data for data in data_batch if isinstance(data, dict)
            ]
            if not valid_readings:
                raise ValueError("No valid sensor readings found in batch.")

            for trans in valid_readings:
                if 'buy' in trans:
                    self.units += trans['buy']
                elif 'sell' in trans:
                    self.units -= trans['sell']
            return (
                f"Processing transaction batch: {list(valid_readings)}\n" +
                f"Transaction analysis: {len(valid_readings)} operations,"
                + f"net flow: {self.units:+} units"
            )
        except ValueError as e:
            return f"Sensor error: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"total_processed": self.total_sum}


class EventStream(DataStream):
    TYPE: str = "System Events"

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.all_logs: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        logs = [data for data in data_batch if isinstance(data, str)]
        error_count = sum(1 for log in logs if log == "error")
        self.all_logs = len(logs)
        return (f"Processing event batch: {logs}\n" +
                f"Event analysis: {self.all_logs} events " +
                f"{error_count} error detected")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"total_processed": self.all_logs}


class StreamProcessor:
    def __init__(self) -> None:
        # The manager holds a list of ANY object that inherits from DataStream
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a new stream into the pipeline."""
        self.streams.append(stream)

    def run_pipeline(self, mixed_batch: List[Any]) -> str:
        """Process a mixed batch through all streams polymorphically."""
        for stream in self.streams:
            stream.process_batch(mixed_batch)
        report = ["Batch 1 Results:"]
        for stream in self.streams:
            stats = stream.get_stats()
            processed = stats.get("total_processed", 0)
            stream_name = stream.__class__.__name__.replace("Stream", "")
            report.append(f"- {stream_name} data: {processed} operations" +
                          "processed")
        report.append("Stream filtering active: High-priority data only")
        critical_alerts = 0
        large_txns = 0
        for stream in self.streams:
            if isinstance(stream, SensorStream):
                critical_alerts = len(stream.filter_data(mixed_batch,
                                                         "critical"))
            elif isinstance(stream, TransactionStream):
                large_txns = len(stream.filter_data(mixed_batch, "large"))
        report.append(f"Filtered results: {critical_alerts} critical sensor" +
                      f"alerts, {large_txns} large transaction")
        report.append("All streams processed successfully. Nexus throughput "
                      + "optimal.")
        return "\n".join(report)


def sensor_test(stream_type: type[DataStream]) -> None:
    match stream_type:
        case cls if cls is SensorStream:
            stream_name = "Sensor"
            stream_id = "SENSOR_001"
            batch = [22.5, "network_error", 45.0, 18, "rebooting", 52.1, 38.5]
        case cls if cls is TransactionStream:
            stream_name = "Transaction"
            stream_id = "TRANS_001"
            batch = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
        case cls if cls is EventStream:
            stream_name = "Event"
            stream_id = "EVENT_001"
            batch = ["login", "ola", "error", "logout"]
        case _:
            print("Unknown stream type detected.\n")
            return

    print(f"Initializing {stream_name} Stream...")
    test_stream = stream_type(stream_id)
    result = test_stream.process_batch(batch)
    print(f"Stream ID: {test_stream.stream_id}, " +
          f"Type: {test_stream.TYPE}")
    print(result)
    print()


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    streams: List[type[DataStream]] = [
        SensorStream, TransactionStream, EventStream
        ]
    for s in streams:
        sensor_test(s)
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    nexus = StreamProcessor()
    nexus.add_stream(SensorStream("SEN-001"))
    nexus.add_stream(TransactionStream("TXN-001"))
    nexus.add_stream(EventStream("EVT-001"))

    # 3. Create ONE massive, mixed batch of data
    mixed_data_batch = [
        {"temp": 105},           # Sensor
        {"buy": 5000},           # Transaction
        "login",                 # Event
        {"critical": 1},         # Sensor Filter
        {"critical": 2},         # Sensor Filter
        "error",                 # Event
        {"sell": 100},           # Transaction
        "logout",                # Event
        {"buy": 10000}
    ]

    # 4. Run the pipeline and print the final report!
    final_report = nexus.run_pipeline(mixed_data_batch)
    print(final_report)
    """ # test the filter data :
    sensor = SensorStream("TEST_002")
    dummy_data = [
        {
            "temp": 25,
            "humidity": 85,
            "pressure": 1013
         },
        {
            "temp": 55,
            "humidity": 185,
            "pressure": 13
         },
        {
            "temp": 5,
            "humidity": 805,
            "pressure": 113
         },
    ]
    print(f"TEMP: {sensor.filter_data(dummy_data, 'temp')}")
    print(f"HUMIDITY: {sensor.filter_data(dummy_data, 'humidity')}")
    print(f"PRESSURE: {sensor.filter_data(dummy_data, 'pressure')}")
 """


if __name__ == "__main__":
    main()
