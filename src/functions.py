import pathlib
from dataclasses import dataclass
from typing import List, Optional

from openpyxl import load_workbook
import requests

from src.data_classes import ApiRequest, Report


def read_excel() -> List[ApiRequest]:
    """return all the combinations of country and date from the excel file in config"""
    with open(pathlib.Path(__file__).parents[1] / 'input.config', 'r') as file:
        path = file.read()
        workbook = load_workbook(filename=path)
        result = []
        for row in workbook.active.rows:
            if row[0].value is not None:
                request = ApiRequest(
                    iso=row[0].value,
                    date=row[1].value,
                )
                result.append(request)

        return result


def query_api_for_report(api_request: ApiRequest):
    response = requests.get("https://covid-api.com/api/reports", params=api_request.__dict__)
    return response


def get_data_to_write(api_requests: List[ApiRequest]):
    results = []
    for req in api_requests:
        response = query_api_for_report(req)
        if response.status_code == 200 and response.json().get('data'):
            report = Report(
                date=response.json()['data']['date'],
                iso=response.json()['data']['iso'],
                num_confirmed=response.json()['data']['num_confirmed'],
                num_deaths=response.json()['data']['num_deaths'],
                num_recovered=response.json()['data']['num_recovered']
            )
            results.append(report)
    return results


def write_excel():
    pass
