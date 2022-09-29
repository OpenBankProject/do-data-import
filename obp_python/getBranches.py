from .config import obp_api_host, version
from .makeRequests import makeGetRequest


def getBranches(bank_id):

  url = obp_api_host + f'/obp/{version}/banks/{bank_id}/branches'
  
  return makeGetRequest(url)
