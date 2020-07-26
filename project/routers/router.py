from fastapi import APIRouter
from ..functions.budget import createBudget,initiateBudget
from ..functions.transactions import initiateTransactions
from ..models.budgetmodel import BudgetReq


router = APIRouter()


@router.post("/api/budget")
async def add_budget(budgetreq:BudgetReq):
    x = createBudget(budgetreq)
    if x > 0:
        result = {"status":"success","message":"successfully created budget"}
    else:
        result = {"status":"error","message":"failed to create budget"}
    return result

@router.post("/api/initialtransaction")
async def initiatetransaction():
    x = initiateTransactions()
    if x > 0:
        result = {"status":"success","message":"successfully initiated transactions"}
    else:
        result = {"status":"error","message":"failed to initiated transactions"}
    return result

@router.post("/api/initialbudget")
async def initiatebudget():
    x = initiateBudget()
    if x > 0:
        result = {"status":"success","message":"successfully initiated budgets"}
    else:
        result = {"status":"error","message":"failed to initiated budgets"}
    return result