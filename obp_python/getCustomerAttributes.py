from .makeRequests import makeGetRequest
from .config import obp_api_host

def getCustomerAttributes(bank_id=None, customer_id=None):


    url = obp_api_host + '/obp/v4.0.0/banks/{bank_id}/customers/{customer_id}/attributes'.format(bank_id=bank_id, customer_id=customer_id)

    req = makeGetRequest(url)
    return req
