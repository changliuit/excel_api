from read_excel import ApiRequest, get_report, read_excel


def test_read_excel():
    result = read_excel()
    assert result == [
        ApiRequest(iso='AUS', date='2021-08-11'),
        ApiRequest(iso='USA', date='2021-01-01'),
        ApiRequest(iso='CHN', date=None),
        ApiRequest(iso='RUS', date='2011-08-01'),
    ]


def test_api_call():
    response = get_report([ApiRequest(iso='AUS', date='2021-08-11')])
    assert response.status_code == 200
