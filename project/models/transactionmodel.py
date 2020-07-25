from pydantic import BaseModel
from typing import Optional, Set

class TransactionItem(BaseModel):
    base_currency_amount:float
    base_currency_code:str
    local_currency_amount:float
    transacted_at:str
    description:str
    category:str
    
