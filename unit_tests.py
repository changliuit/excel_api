from datetime import datetime

from read_excel import ApiRequest, read_excel


def test_read_excel():
    result = read_excel()
    assert result == [
        ApiRequest(country_iso='AUS', date=datetime(2021, 8, 10, 0, 0)),
        ApiRequest(country_iso='USA', date=datetime(2021, 1, 1, 0, 0))
    ]
