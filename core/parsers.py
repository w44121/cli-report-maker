from abc import ABC, abstractmethod

from core.entities import Employee
from core.utils import set_dict_key


class Parser(ABC):
    @abstractmethod
    def parse(self): ...


class CSVParser(Parser):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.records: list[Employee] = []

    def parse(self) -> list[Employee]:
        with open(self.file_path, "r") as f:
            data = f.read().strip().split("\n")

        headers = data[0].split(",")

        for line in data[1:]:
            values = line.split(",")
            record = dict(zip(headers, values))
            set_dict_key(record, "rate", ["rate", "hourly_rate", "salary"])
            self.records.append(Employee(**record))

        return self.records
