from src.functions import ApiRequest, query_api_for_report


def test_api_call():
    response = query_api_for_report(ApiRequest(iso='USA', date='2020-04-16'))
    assert response.status_code == 200
    assert response.json()['data']


def test_invalid_iso_api_call():
    response = query_api_for_report(ApiRequest(iso='d112', date=None))
    assert response.status_code == 200
    assert not response.json()['data']
