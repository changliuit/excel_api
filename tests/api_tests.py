import pytest as pytest

from excel_popper import ApiRequest, ExcelPopper
from exceptions import InputError


def test_api_call():
    response = ExcelPopper().query_api_for_report(ApiRequest(iso='USA', date='2020-04-16'))
    assert response.status_code == 200
    assert response.json()['data']


def test_invalid_iso_api_call():
    response = ExcelPopper().query_api_for_report(ApiRequest(iso='d112', date=None))
    assert response.status_code == 200
    assert not response.json()['data']


def test_invalid_date_api_call():
    response = ExcelPopper().query_api_for_report(ApiRequest(iso='d112', date='202102'))
    assert response.status_code == 422
    assert response.json() == {'error': {'date': ['The date does not match the format Y-m-d.']}}
    assert not response.json().get('data')


def test_return_report():
    ep = ExcelPopper()
    result = ep.get_report_to_write([ApiRequest(iso='USA', date='2020-04-16')])
    assert result


def test_return_report_raise_exception_with_invalid_date():
    ep = ExcelPopper()
    with pytest.raises(InputError):
        ep.get_report_to_write([ApiRequest(iso='USA', date='202102')])
