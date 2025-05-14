from abc import ABC, abstractmethod

from core.entities import Employee


class Report(ABC):
    def __init__(self, employees: list[Employee]) -> None:
        self.employees = employees
        self._groups: dict[str, list[Employee]] = {}

    def grouping(self, attr: str = "department") -> None:
        for employee in self.employees:
            if (d := getattr(employee, attr)) not in self._groups:
                self._groups[d] = []
            self._groups[d].append(employee)

    @abstractmethod
    def execute(self) -> None: ...


class PayoutReport(Report):
    def __init__(self, employees: list[Employee]) -> None:
        super().__init__(employees)
        self._totals: dict[str, dict[str, int]] = {}

    def calc(self) -> None:
        for group in self._groups:
            total_hours = 0
            total_payout = 0
            for employee in self._groups[group]:
                total_hours += employee.hours_worked
                total_payout += employee.payout
            self._totals[group] = {
                "total_hours": total_hours,
                "total_payout": total_payout,
            }

    def execute(self) -> None:
        self.calc()
        print(f"{'report':^50}")
        print(f"{'':<12} {'name':<16} {'hours':<5} {'rate':<4} {'payout':<8}")
        for group in self._groups:
            print(f"{group}")
            for employee in self._groups[group]:
                print(
                    f"{'':-<12} {employee.name:<16} {employee.hours_worked:<5} {employee.rate:<4} ${employee.payout:<8}"
                )
            print(
                f"{self._totals[group]['total_hours']:>33} {'$' + str(self._totals[group]['total_payout']):>14}"
            )


class ReportFactory:
    def __init__(self) -> None:
        self.reports = {
            "payout": PayoutReport,
        }

    def get_report(self, report_type: str, employees: list[Employee]) -> Report:
        report_class = self.reports.get(report_type)
        if not report_class:
            raise ValueError("Report type not found")
        return report_class(employees)
