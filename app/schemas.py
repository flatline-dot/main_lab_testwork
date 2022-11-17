from pydantic import BaseModel
from datetime import date


class Bill(BaseModel):
    client_name = str
    client_org = str
    num_bill = int
    sum_bill = int
    date_bill = date
    service = str
