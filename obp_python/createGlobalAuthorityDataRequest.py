from .config import obp_api_host
from .makeRequests import makePostRequest


def createGlobalAuthorityDataRequest(
        bank_id=None,
        customer_nr=None,
        mandate_name=None,
        mandate_name_year=None):

    payload = {
        "customer_number": customer_nr,
        "bank_code": bank_id,
        "mandate_name": mandate_name,
        "mandate_name_year": mandate_name_year
    }
    url = obp_api_host + '/obp/dynamic-entity/authority_data_request'

    return makePostRequest(url, payload)
