from dataclasses import dataclass
from datetime import datetime
from typing import List

from openpyxl import load_workbook


@dataclass
class ApiRequest:
    country_iso: str
    date: datetime


def read_config():
    pass


def read_excel() -> List[ApiRequest]:
    """return all the combinations of country and date"""
    workbook = load_workbook(filename="test_excel.xlsx")
    result = []
    row = 1
    while workbook.active.cell(row=row, column=1).value is not None:
        request = ApiRequest(
            country_iso=workbook.active.cell(row=row, column=1).value,
            date=workbook.active.cell(row=row, column=2).value,
        )
        result.append(request)
        row += 1
    return result


def call_api():
    pass


def write_excel():
    pass
