from pydantic import BaseModel
from typing import Optional, Set

class BudgetReq(BaseModel):
    pb_identifier:str
    category:str
    amount:float
    budget_type:str

class BudgetItem(BaseModel):
    category:Optional[str] = None
    type:Optional[str] = None
    period:Optional[str] = None
    budget_advise:Optional[str]=None
    budget_period:Optional[str]=None
    local_currency_amount_allowed:Optional[float]=None
    local_currency_period_spent:Optional[float]=None
    local_currency_period_remaining:Optional[float]=None
    created_at:Optional[str]=None
    budget_notes:Optional[str]=None

class Budgets_Users(BaseModel):
    _id:str
    Local_currency_code:str
    budgets:Optional[Set[BudgetItem]]= None    
