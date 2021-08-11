from excel_popper import ApiRequest, ExcelPopper


def test_read_excel():
    result = ExcelPopper().read_excel()
    assert result == [
        ApiRequest(iso='AUS', date='2021-08-11'),
        ApiRequest(iso='USA', date='2021-01-01'),
        ApiRequest(iso='CHN', date=None),
        ApiRequest(iso='RUS', date='2011-08-01'),
    ]
