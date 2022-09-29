from .config import obp_api_host, version
from .makeRequests import makeGetRequest


def getAccountByIdFull(bank_id, account_id):

  url = obp_api_host + '/obp/{version}/banks/{bank_id}/accounts/{account_id}/owner/account'.format(version=version, bank_id=bank_id, account_id=account_id)
  
  return makeGetRequest(url)
