from ..models.transactionmodel import TransactionItem
import pymongo
import json

client=pymongo.MongoClient("mongodb+srv://shawn:shawn@cluster0.uebyo.mongodb.net/plannerbee?retryWrites=true&w=majority")
db = client["plannerbee"]
col = db["transactions_users"]

def initiateTransactions():
    usertrans = {
       
    "_id": "16cecd11-2f83-4864-bf6b-f270f4be88cb",
    "local_currency_code": "SGD",
    "transactions": {
        "250773972570868310": {
            "base_currency_amount": -1.3,
            "base_currency_code": "SGD",
            "local_currency_amount": -1.3,
            "transacted_at": "2020-04-03T00:00:00Z",
            "description": "COLD STORAGE-BJ SINGAPORE SG",
            "category": "shopping"
        },
        "250773972570868311": {
            "base_currency_amount": -2.62,
            "base_currency_code": "SGD",
            "local_currency_amount": -2.62,
            "transacted_at": "2020-04-03T00:00:00Z",
            "description": "BUS/MRT 33803686 SINGAPORE SG",
            "category": "transfers"
        },
        "250773972570868312": {
            "base_currency_amount": -11.8,
            "base_currency_code": "SGD",
            "local_currency_amount": -11.8,
            "transacted_at": "2020-04-03T00:00:00Z",
            "description": "UNIQLO BUGIS+ SINGAPORE SG",
            "category": "shopping"
        },
        "250773972570868313": {
            "base_currency_amount": -4.32,
            "base_currency_code": "SGD",
            "local_currency_amount": -4.32,
            "transacted_at": "2020-04-05T00:00:00Z",
            "description": "POPULAR BOOK COMPANY-M SINGAPORE SG",
            "category": "education"
        },
        "250773972570868314": {
            "base_currency_amount": -50.29,
            "base_currency_code": "SGD",
            "local_currency_amount": -50.29,
            "transacted_at": "2020-05-05T00:00:00Z",
            "description": "SWENSEN'S-PWP SINGAPORE SG",
            "category": "shopping"
        },
        "250773972570868315": {
            "base_currency_amount": 271.86,
            "base_currency_code": "SGD",
            "local_currency_amount": 271.86,
            "transacted_at": "2020-05-07T00:00:00Z",
            "description": "GIRO PAYMENT",
            "category": "transfers"
        },
        "250773972570868316": {
            "base_currency_amount": -138.0,
            "base_currency_code": "SGD",
            "local_currency_amount": -138.0,
            "transacted_at": "2020-05-09T00:00:00Z",
            "description": "EU YAN SANG SINGAPORE SINGAPORE SG",
            "category": "personal_care"
        },
        "250773972579256925": {
            "base_currency_amount": -1.5,
            "base_currency_code": "SGD",
            "local_currency_amount": -1.5,
            "transacted_at": "2020-05-11T00:00:00Z",
            "description": "HAO MART - MANDARIN GA SINGAPORE SG",
            "category": "groceries"
        },
        "250773972579256926": {
            "base_currency_amount": 9.36,
            "base_currency_code": "SGD",
            "local_currency_amount": 9.36,
            "transacted_at": "2020-06-16T00:00:00Z",
            "description": "30CASHBACK",
            "category": "transfers"
        },
        "250773972579256927": {
            "base_currency_amount": -17.19,
            "base_currency_code": "SGD",
            "local_currency_amount": -17.19,
            "transacted_at": "2020-06-20T00:00:00Z",
            "description": "DELIVEROO SINGAPORE SG",
            "category": "shopping"
        },
        "250773972579256928": {
            "base_currency_amount": 614.87,
            "base_currency_code": "SGD",
            "local_currency_amount": 614.87,
            "transacted_at": "2020-06-21T00:00:00Z",
            "description": "PAYMENT - THANK YOU",
            "category": "income"
        },
        "250773972579256929": {
            "base_currency_amount": -46.53,
            "base_currency_code": "SGD",
            "local_currency_amount": -46.53,
            "transacted_at": "2020-06-07T00:00:00Z",
            "description": "FAIRPRICE FINEST-MARIN SINGAPORE SG",
            "category": "groceries"
        },
        "250773972579256930": {
            "base_currency_amount": 63.72,
            "base_currency_code": "SGD",
            "local_currency_amount": 63.72,
            "transacted_at": "2020-07-05T00:00:00Z",
            "description": "PAYMENT - THANK YOU",
            "category": "transfers"
        },
        "250773972579256931": {
            "base_currency_amount": -33.89,
            "base_currency_code": "SGD",
            "local_currency_amount": -33.89,
            "transacted_at": "2020-07-05T00:00:00Z",
            "description": "DELIVEROO SINGAPORE SG",
            "category": "shopping"
        },
        "250773972579256932": {
            "base_currency_amount": -55.27,
            "base_currency_code": "SGD",
            "local_currency_amount": -55.27,
            "transacted_at": "2020-07-05T00:00:00Z",
            "description": "DELIVEROO SINGAPORE SG",
            "category": "shopping"
        },
        "250773972579256933": {
            "base_currency_amount": 33.89,
            "base_currency_code": "SGD",
            "local_currency_amount": 33.89,
            "transacted_at": "2020-07-05T00:00:00Z",
            "description": "PAYMENT - THANK YOU",
            "category": "transfers"
        },
        "250773972587645542": {
            "base_currency_amount": -13.65,
            "base_currency_code": "SGD",
            "local_currency_amount": -13.65,
            "transacted_at": "2020-07-06T00:00:00Z",
            "description": "NTUC FP-BEDOK B SINGAPORE SG",
            "category": "groceries"
        },
        "250773972587645543": {
            "base_currency_amount": 2.5,
            "base_currency_code": "SGD",
            "local_currency_amount": 2.5,
            "transacted_at": "2020-07-06T00:00:00Z",
            "description": "30CASHBACK",
            "category": "transfers"
        },
        "250773972587645544": {
            "base_currency_amount": -10.5,
            "base_currency_code": "SGD",
            "local_currency_amount": -10.5,
            "transacted_at": "2020-07-06T00:00:00Z",
            "description": "HOMEGROUND COFFEE ROAS SINGAPORE SG",
            "category": "shopping"
        }
        }
    }
    
    x= col.update_one(
        {"_id": "16cecd11-2f83-4864-bf6b-f270f4be88cb"},
        {"$setOnInsert":usertrans},
        upsert=True
    )

    
    return str(x.modified_count)