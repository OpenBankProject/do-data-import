import requests

from .config import obp_api_host
from .makeRequests import makePostRequest


def createHistoricalTransaction(from_account_id=None, from_bank_id=None,
                to_account_id=None, to_bank_id=None, currency=None,
                amount=None, description="", posted="2019-09-19T02:31:05Z",
                completed="2019-09-19T02:31:05Z"):
  """
  Create a historical transaction
  
  Requires entitlement: `CanCreateHistoricalTransaction`.
  
  e.g. using the cli:
  obp addrole --role-name CanCreateHistoricalTransaction 
  """

  payload = {
            "from": {
              "bank_id": from_bank_id,
              "account_id": from_account_id
            },
            "to": {
              "bank_id": to_bank_id,
              "account_id": to_account_id
              }, 
            "value": {
              "currency": currency, 
              "amount": amount
            },
            "description": description, 
            "posted": str(posted),
            "completed": str(completed),
            "type": "SANDBOX_TAN",
            "charge_policy": "SHARED"
            }

  
  url = obp_api_host + '/obp/v4.0.0/management/historical/transactions'

  req = makePostRequest(url, payload)
 
  return req
