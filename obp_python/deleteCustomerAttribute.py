from .config import obp_api_host
from .makeRequests import makeDeleteRequest


def deleteCustomerAttribute(bank_id=None, attribute=None):

  url = obp_api_host + \
        '/obp/v4.0.0/banks/{bank_id}/customers/attributes/{attribute}'.format(bank_id=bank_id, attribute=attribute)
  req = makeDeleteRequest(url)
  return req
