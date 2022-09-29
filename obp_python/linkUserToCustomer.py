from .makeRequests import makePostRequest
from .config import obp_api_host, logger

def linkUserToCustomer(bank_id=None, user_id=None, customer_id=None):

  payload = {
    "user_id": user_id,  "customer_id": customer_id
    }

  url = obp_api_host + '/obp/v3.1.0/banks/{bank_id}/user_customer_links'.format(bank_id=bank_id)

  req = makePostRequest(url, payload)

  return req
