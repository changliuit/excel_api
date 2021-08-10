from dataclasses import dataclass
from typing import List, Optional

from openpyxl import load_workbook


@dataclass
class ApiRequest:
    country_iso: str
    date: Optional[str]


def read_config():
    pass


def read_excel() -> List[ApiRequest]:
    """return all the combinations of country and date"""
    workbook = load_workbook(filename="test_excel.xlsx")
    result = []
    for row in workbook.active.rows:
        if row[0].value is not None:
            request = ApiRequest(
                country_iso=row[0].value,
                date=row[1].value,
            )
            result.append(request)

    return result


def call_api(request: ApiRequest):
    pass


def write_excel():
    pass
