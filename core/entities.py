from dataclasses import dataclass


@dataclass
class Employee:
    id: int
    name: str
    email: str
    department: str
    hours_worked: int
    rate: float

    def __post_init__(self):
        self.id = int(self.id)
        self.hours_worked = int(self.hours_worked)
        self.rate = float(self.rate)

    @property
    def payout(self) -> float:
        return self.hours_worked * self.rate
