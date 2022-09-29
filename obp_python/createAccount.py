from .makeRequests import makePostRequest
from .config import obp_api_host


def createAccount(bankid=None, userid=None, currency=None, label=None, productcode=None, branchid=None, accountrouting_scheme=None, accountrouting_address=None):

  payload = {
      "user_id": userid,
      "label": label,
      "product_code": productcode,
      "balance": {"currency": currency, "amount": "0"},
      "branch_id": branchid,
      "account_routings": [{"scheme": accountrouting_scheme, "address": accountrouting_address}],
  }

  url = obp_api_host + '/obp/v4.0.0/banks/{BANK_ID}/accounts'.format(BANK_ID=bankid)
  
  return makePostRequest(url,payload)
