from .makeRequests import makePostRequest
from .config import obp_api_host

def getCustomerIdByCustomerNumber(bank_id=None, customer_number=None):

  payload = { "customer_number": customer_number }

  url = obp_api_host + '/obp/v3.1.0/banks/{bank_id}/customers/customer-number'.format(bank_id=bank_id)
  req = makePostRequest(url, payload)
  return req