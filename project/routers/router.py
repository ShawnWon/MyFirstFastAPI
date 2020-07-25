from fastapi import APIRouter
from ..functions.budget import createBudget,initiateBudget
from ..functions.transactions import initiateTransactions
from ..models.budgetmodel import BudgetReq,BudgetItem


router = APIRouter()


@router.post("/api/addbudget")
async def add_budget(budgetreq:BudgetReq):
    x = createBudget(budgetreq)
    if x>0:
        result={"status":"success","message":"successfully created budget"}
    else:
        result={"status":"error","message":"failed to create budget"}
    return result

@router.post("/api/initiatetransaction")
async def initiatetransaction():
    x=initiateTransactions()
    return x

@router.post("/api/initiatebudget")
async def initiatebudget():
    x=initiateBudget()
    return x