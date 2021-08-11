import os

from data_classes import Report
from excel_popper import ApiRequest, ExcelPopper


def test_read_excel():
    result = ExcelPopper().read_excel()
    assert result == [
        ApiRequest(iso='AUS', date='2021-08-11'),
        ApiRequest(iso='USA', date='2021-01-01'),
        ApiRequest(iso='CHN', date=None),
        ApiRequest(iso='RUS', date='2011-08-01'),
    ]


def test_write_excel():
    test_file_name = "test.xlsx"
    reports = [
        Report(date='2020-04-16', iso='USA', num_confirmed=11057, num_deaths=579, num_recovered=0),
        Report(date='2020-04-16', iso='USA', num_confirmed=25734, num_deaths=1072, num_recovered=0),
        Report(date='2020-04-16', iso='USA', num_confirmed=27677, num_deaths=956, num_recovered=0),
        Report(date='2020-04-16', iso='USA', num_confirmed=4237, num_deaths=150, num_recovered=0),
    ]
    ExcelPopper(test_file_name).write_excel(reports)
    os.unlink(test_file_name)
