import pathlib

import click as click

from excel_popper import ExcelPopper

config_file_name = 'input.config'

print(f"Opening config file {config_file_name}")
with open(pathlib.Path(__file__).parents[1] / config_file_name, 'r') as file:
    path = file.read()
ep = ExcelPopper(config_path=path)
click.confirm(f"Reading {path} to submit to api and writing to {ep.output_filepath}. Are you sure?", abort=True)
requests = ep.read_excel()
reports = ep.get_report_to_write(requests)
ep.write_excel(reports)
