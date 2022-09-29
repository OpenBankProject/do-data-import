from .config import obp_api_host
from .makeRequests import makeDeleteRequest


def deleteBank(bank_id=None):

  url = obp_api_host + \
        f'/obp/v5.0.0/management/cascading/banks/{bank_id}'
  req = makeDeleteRequest(url)
  return req
