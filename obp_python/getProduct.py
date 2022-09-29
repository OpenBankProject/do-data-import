from .makeRequests import makeGetRequest
from .config import obp_api_host

def getProduct(bank_id=None, product_code=None):


    url = obp_api_host + '/obp/v4.0.0/banks/{bank_id}//products/{product_code}'.format(bank_id=bank_id, product_code=product_code)

    req = makeGetRequest(url)
    return req
