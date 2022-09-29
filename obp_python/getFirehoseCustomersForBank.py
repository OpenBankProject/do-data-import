from .makeRequests import makeGetRequest
from .config import obp_api_host, version


def getFirehoseCustomersforBank(bank_id=None, limit="50", offset="0"):

    url = obp_api_host + f'/obp/v4.0.0/banks/{bank_id}/firehose/customers?' # ?limit={(limit)}&offset={(offset)}'

    req = makeGetRequest(url)
    return req
