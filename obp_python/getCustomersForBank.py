from .makeRequests import makeGetRequest
from .config import obp_api_host

def getCustomersForBank(bank_id=None):

    url = obp_api_host + f'/obp/v5.0.0/banks/{bank_id}/customers'

    req = makeGetRequest(url)
    return req
