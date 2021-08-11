from excel_popper import ApiRequest, ExcelPopper


def test_api_call():
    response = ExcelPopper().query_api_for_report(ApiRequest(iso='USA', date='2020-04-16'))
    assert response.status_code == 200
    assert response.json()['data']


def test_invalid_iso_api_call():
    response = ExcelPopper().query_api_for_report(ApiRequest(iso='d112', date=None))
    assert response.status_code == 200
    assert not response.json()['data']


def test_return_report():
    ep = ExcelPopper()
    result = ep.get_report_to_write([ApiRequest(iso='USA', date='2020-04-16')])
    assert result
