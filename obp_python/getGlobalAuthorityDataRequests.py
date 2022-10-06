from .config import obp_api_host
from .makeRequests import makeGetRequest


def getGlobalAuthorityDataRequests():



  url = obp_api_host + f'/obp/dynamic-entity/authority_data_request'
  return makeGetRequest(url)
