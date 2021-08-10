from datetime import datetime

from read_excel import ApiRequest, read_excel


def test_read_excel():
    result = read_excel()
    assert result == [
        ApiRequest(country_iso='AUS', date='2021-08-11'),
        ApiRequest(country_iso='USA', date='2021-01-01'),
        ApiRequest(country_iso='CHN', date=None),
        ApiRequest(country_iso='RUS', date='2011-08-01'),
    ]
