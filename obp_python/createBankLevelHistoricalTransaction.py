import requests

from .config import obp_api_host
from .makeRequests import makePostRequest


def createBankLevelHistoricalTransaction(
        bank_id=None,
        from_account_id=None,
        to_account_id=None,
        currency=None,
        amount=None,
        description="",
        posted="2019-09-19T02:31:05Z",
        completed="2019-09-19T02:31:05Z"):


  payload = {
    "from_account_id": from_account_id,
    "to_account_id": to_account_id,
    "value": {
        "currency": currency,
        "amount": amount
    },
    "description": description,
    "posted": posted,
    "completed": completed,
    "type": "SANDBOX_TAN",
    "charge_policy": "SHARED"
}

  
  url = f'{obp_api_host}/obp/v5.0.0/banks/{bank_id}/management/historical/transactions'

  req = makePostRequest(url, payload)
 
  return req
