from .config import obp_api_host, version
from .makeRequests import makeDeleteRequest


def deleteGlobalAuthorityDataRequest(authority_data_request_id=None):

  url = obp_api_host + \
        f'/obp/dynamic-entity/authority_data_request/{authority_data_request_id}'
  req = makeDeleteRequest(url)
  return req
