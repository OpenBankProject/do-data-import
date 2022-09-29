from .config import obp_api_host, version
from .makeRequests import makePostRequest


def getAccountByAccountRouting(bank_id, account_routing_scheme, account_routing_address):

  payload = {
    "bank_id": bank_id,
    "account_routing": {
      "scheme": account_routing_scheme,
      "address": account_routing_address}
  }

  url = obp_api_host + '/obp/{version}//management/accounts/account-routing-query'.format(version=version)
  
  return makePostRequest(url, payload)
