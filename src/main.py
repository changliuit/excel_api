from excel_popper import ExcelPopper

ep = ExcelPopper()
requests = ep.read_excel()
reports = ep.get_report_to_write(requests)
ep.write_excel(reports)
