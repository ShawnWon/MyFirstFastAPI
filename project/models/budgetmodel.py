from pydantic import BaseModel
from typing import Optional, Set

class BudgetReq(BaseModel):
    pb_identifier:str
    category:str
    amount:float
    budget_type:str

