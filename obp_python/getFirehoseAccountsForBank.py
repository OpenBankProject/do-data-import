from .makeRequests import makeGetRequest
from .config import obp_api_host, version

def getFirehoseAccountsforBank(bank_id=None,limit="50", offset="0"):

    url = obp_api_host + f'/obp/v3.0.0/banks/{bank_id}/firehose/accounts/views/owner' #?limit={str(limit)}&offset={str(offset)}'

    req = makeGetRequest(url)
    return req
