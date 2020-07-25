from ..models.budgetmodel import BudgetReq,BudgetItem
import pymongo
import datetime
import uuid
import json

client=pymongo.MongoClient("mongodb+srv://shawn:shawn@cluster0.uebyo.mongodb.net/plannerbee?retryWrites=true&w=majority")
db = client["plannerbee"]
col = db["budgets_users"]


def initiateBudget():

    userbudgets = {
    "_id": "16cecd11-2f83-4864-bf6b-f270f4be88cb",
    "local_currency_code": "SGD",
    "budgets": {
        "b93bf281-5d2f-456a-961b-511da2682df6": {
            "category": "dining",
            "type": "Annual",
            "period": "072020",
            "budget_advise": "SGD 0/day",
            "budget_period": "01 Jan 2020 - 31 Dec 2020",
            "local_currency_amount_allowed": 100,
            "local_currency_period_spent": -860.82,
            "local_currency_period_remaining": -760.82,
            "created_at": "2020-06-30T16:20:51Z",
            "budget_notes": "status_above_100"
        },
        "d302d551-ec51-4516-9bc1-48de692b4abc": {
            "category": "dining",
            "type": "Monthly",
            "period": "072020",
            "budget_advise": "SGD 0/day",
            "budget_period": "01 Jul 2020 - 31 Jul 2020",
            "local_currency_amount_allowed": 100,
            "local_currency_period_spent": -537.48,
            "local_currency_period_remaining": -437.48,
            "created_at": "2020-06-30T16:23:20Z",
            "budget_notes": "status_above_100"
        }
    }
    }

    x= col.update_one(
        {"_id": "16cecd11-2f83-4864-bf6b-f270f4be88cb"},
        {"$setOnInsert":userbudgets},
        upsert=True
    )

    
    return str(x.modified_count)

def createBudget(budgetreq:BudgetReq):
    userbudget = col.find_one({"_id": budgetreq.pb_identifier})
    budgetitem = BudgetItem()
    budgetitem.category = budgetreq.category
    budgetitem.type = budgetreq.budget_type
    budgetitem.created_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    budgetitem.period = "a"
    budgetitem.budget_advise = "a"
    budgetitem.budget_period = "a"
    budgetitem.local_currency_amount_allowed = 1
    budgetitem.local_currency_period_spent = 1
    budgetitem.local_currency_period_remaining = 1
    budgetitem.budget_notes = "a"
    uuidcode = str(uuid.uuid1())

    bitem ={
            "category": budgetreq.category,
            "type": budgetreq.budget_type,
            "period": "072020",
            "budget_advise": "SGD 0/day",
            "budget_period": "01 Jan 2020 - 31 Dec 2020",
            "local_currency_amount_allowed": 100,
            "local_currency_period_spent": -860.82,
            "local_currency_period_remaining": -760.82,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "budget_notes": "status_above_100"
        }

    userbudget["budgets"][uuidcode]=bitem

    myquery={"_id": budgetreq.pb_identifier}
    newvalue= {"$set":{"budgets":userbudget["budgets"]}}
    col.update_one(myquery,newvalue)
    print(type(userbudget["budgets"]))
    print(type({}))
    return userbudget["budgets"]