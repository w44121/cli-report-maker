import pytest

from core.parsers import CSVParser
from core.entities import Employee
from core.reports import PayoutReport, ReportFactory


def test_valid_csv_file(csv_file_1):
    data = CSVParser(csv_file_1).parse()
    assert data[0].rate == 45
    assert data[-1].rate == 38
    assert len(data) == 3


def test_invalid_rate_header_csv_file(csv_file_2):
    data = CSVParser(csv_file_2).parse()
    assert data[0].rate == 50
    assert data[-1].rate == 60
    assert len(data) == 3


def test_employee_create(employee_data):
    e = Employee(**employee_data[0])
    assert isinstance(e.id, int)
    assert isinstance(e.name, str)
    assert isinstance(e.department, str)
    assert isinstance(e.hours_worked, int)
    assert isinstance(e.rate, float)


def test_employee_payout(employee):
    assert employee.payout == 7200.0


def test_report_grouping(employee_list):
    r = PayoutReport(employee_list)
    r.grouping()

    assert len(r._groups) == 2
    assert "HR" in r._groups
    assert "Marketing" in r._groups


def test_payout_reporter(employee_list):
    pr = PayoutReport(employee_list)
    pr.grouping()
    pr.calc()

    assert pr._totals == {
        "HR": {"total_hours": 318, "total_payout": 13_204.0},
        "Marketing": {
            "total_hours": 150,
            "total_payout": 5_250.0,
        },
    }


def test_get_valid_report_from_factory(employee_list):
    report = ReportFactory().get_report("payout", employee_list)

    assert isinstance(report, PayoutReport)


def test_get_invalid_report_from_factory(employee_list):
    with pytest.raises(ValueError):
        _ = ReportFactory().get_report("unknown report type", employee_list)


def test_payout_reporter_execute(employee_list):
    pr = PayoutReport(employee_list)
    pr.grouping()
    pr.execute()
