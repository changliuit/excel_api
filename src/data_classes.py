from dataclasses import dataclass
from typing import Optional


@dataclass
class ApiRequest:
    iso: str
    date: Optional[str]


@dataclass
class Report:
    date: str
    iso: str
    num_confirmed: str
    num_deaths: str
    num_recovered: str
