from ..models.budgetmodel import BudgetReq,BudgetItem
import pymongo
from datetime import datetime
import uuid
import json
import calendar

client=pymongo.MongoClient("mongodb+srv://shawn:shawn@cluster0.uebyo.mongodb.net/plannerbee?retryWrites=true&w=majority")
db = client["plannerbee"]
col = db["budgets_users"]
transcol = db["transactions_users"]


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
    uuidcode = str(uuid.uuid1())
    now=datetime.now()
    year=now.strftime("%Y")
    mon=now.strftime("%m")
    calmon = now.strftime("%b")
    if budgetreq.budget_type=="Annual":
        bperiod= "01 Jan "+now.strftime("%Y")+" - 31 Dec "+now.strftime("%Y")
        start = datetime.strptime(year+"/1/1",'%Y/%m/%d')
        end = datetime.strptime(year+"/12/31",'%Y/%m/%d')
    elif budgetreq.budget_type=="Monthly": 
        bperiod= "01 "+calmon+" "+year+" - "+str(calendar.monthrange(int(year), int(mon))[1])+" "+calmon+" "+year
        start=datetime.strptime(year+"/"+mon+"/1",'%Y/%m/%d')
        end = datetime.strptime(year+"/"+mon+"/"+str(calendar.monthrange(int(year), int(mon))[1]),'%Y/%m/%d')
    
    usertrans = transcol.find_one({"_id": budgetreq.pb_identifier})["transactions"]
    periodspent=0
    for key in usertrans:
        dateobj= datetime.strptime(usertrans[key]["transacted_at"],'%Y-%m-%dT%H:%M:%SZ')
        if dateobj>start and usertrans[key]["category"]==budgetreq.category  :
            periodspent+=usertrans[key]["base_currency_amount"]

    
    if (budgetreq.amount+round(periodspent,2))<0 :
        status="status_above_100"
    else:
        status="status_below_100"

    advise = round((budgetreq.amount+round(periodspent,2))/(end-now).days,2)
    
    bitem ={
            "category": budgetreq.category,
            "type": budgetreq.budget_type,
            "period": now.strftime("%m%Y"),
            "budget_advise": "SGD "+str(advise)+"/day",
            "budget_period": bperiod,
            "local_currency_amount_allowed": budgetreq.amount,
            "local_currency_period_spent": round(periodspent,2),
            "local_currency_period_remaining": round(budgetreq.amount+periodspent,2),
            "created_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "budget_notes": status
        }

    userbudget["budgets"][uuidcode]=bitem

    myquery={"_id": budgetreq.pb_identifier}
    newvalue= {"$set":{"budgets":userbudget["budgets"]}}
    result=col.update_one(myquery,newvalue)

    
    return result.modified_count