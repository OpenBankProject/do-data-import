from .config import obp_api_host
from .makeRequests import makePostRequest

def createBank500(bank_code, id=None, full_name=None,
                logo_url=None, website_url=None,
                bank_routing_scheme=None, bank_routing_address=None, attributes=None):

    payload = {
    "bank_code": bank_code
    }
    if id is not None:
        payload['id'] = id
    if full_name is not None:
        payload["full_name"] = full_name
    if logo_url is not None:
        payload["logo"] = logo_url
    if website_url is not None:
        payload["website"] = website_url
    if bank_routing_scheme is not None and bank_routing_address is not None:
        payload["bank_routings"] = [{
        "scheme": bank_routing_scheme,
        "address": bank_routing_address
        }]
    if attributes is not None:
        payload["attributes"] = attributes

    url = obp_api_host + '/obp/v5.0.0/banks'

    return makePostRequest(url, payload)
