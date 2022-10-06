from .config import obp_api_host, version
from .makeRequests import makeDeleteRequest


def deleteAuthorityDataRequestAtBank(bank_id=None, authority_data_request_id=None):

  url = obp_api_host + \
        f'//obp/dynamic-entity/banks/{bank_id}/authority_data_request/{authority_data_request_id}'
  req = makeDeleteRequest(url)
  return req
