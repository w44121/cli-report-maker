import os
from pathlib import Path
import pytest

from core.entities import Employee


tmp_path = Path("./")


@pytest.fixture
def csv_data_1():
    return """department,id,email,name,hours_worked,rate
HR,101,grace@example.com,Grace Lee,160,45
Marketing,102,henry@example.com,Henry Martin,150,35
HR,103,ivy@example.com,Ivy Clark,158,38"""


@pytest.fixture
def csv_data_2():
    return """id,email,name,department,hours_worked,hourly_rate
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
3,carol@example.com,Carol Williams,Design,170,60"""


@pytest.fixture
def csv_file_1(csv_data_1):
    file_path = tmp_path / "data1.csv"
    file_path.write_text(csv_data_1)
    yield file_path
    os.remove(file_path)


@pytest.fixture
def csv_file_2(csv_data_2):
    file_path = tmp_path / "data2.csv"
    file_path.write_text(csv_data_2)
    yield file_path
    os.remove(file_path)


@pytest.fixture
def employee_data():
    return [
        {
            "id": "101",
            "name": "Grace Lee",
            "email": "grace@example.com",
            "department": "HR",
            "hours_worked": "160",
            "rate": "45",
        },
        {
            "id": "102",
            "name": "Henry Martin",
            "email": "henry@example.com",
            "department": "Marketing",
            "hours_worked": "150",
            "rate": "35",
        },
        {
            "id": "103",
            "name": "Ivy Clark",
            "email": "ivy@example.com",
            "department": "HR",
            "hours_worked": "158",
            "rate": "38",
        },
    ]


@pytest.fixture
def employee(employee_data):
    return Employee(**employee_data[0])


@pytest.fixture
def employee_list(employee_data):
    return [Employee(**data) for data in employee_data]
