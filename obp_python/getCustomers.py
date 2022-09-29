from .makeRequests import makeGetRequest
from .config import obp_api_host

def getCustomers(bank_id=None):

    url = obp_api_host + '/obp/v3.1.0/banks/{bank_id}/firehose/customers'.format(bank_id=bank_id)

    req = makeGetRequest(url)
    return req
