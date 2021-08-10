from dataclasses import dataclass
from typing import List, Optional

from openpyxl import load_workbook
import requests

@dataclass
class ApiRequest:
    iso: str
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
                iso=row[0].value,
                date=row[1].value,
            )
            result.append(request)

    return result


def get_report(api_requests: List[ApiRequest]):
    for req in api_requests:
        response = requests.get("https://covid-api.com/api/reports", params=req.__dict__)
    return response


def write_excel():
    pass
