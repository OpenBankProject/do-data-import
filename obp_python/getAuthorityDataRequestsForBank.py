from .config import obp_api_host
from .makeRequests import makeGetRequest


def getAuthorityDataRequestsForBank(bank_id):



  url = obp_api_host + f'/obp/dynamic-entity/banks/{bank_id}/authority_data_request'
  return makeGetRequest(url)
