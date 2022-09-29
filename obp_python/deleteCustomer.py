from .config import obp_api_host
from .makeRequests import makeDeleteRequest


def deleteCustomer(bank_id=None, customer_id=None):

  url = obp_api_host + \
        f'/obp/v4.0.0/management/cascading/banks/{bank_id}/customers/{customer_id}'
  req = makeDeleteRequest(url)
  return req
