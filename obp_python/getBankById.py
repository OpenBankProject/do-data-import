from .config import obp_api_host, version
from .makeRequests import makeGetRequest


def getBankById(bank_id):

  url = obp_api_host + '/obp/{version}/banks/{bank_id}'.format(version=version, bank_id=bank_id)
  
  return makeGetRequest(url)
