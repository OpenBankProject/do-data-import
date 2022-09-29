from .config import obp_api_host, version
from .makeRequests import makePostRequest

def createBankAttribute(
        bank_id=None,
        name=None,
        _type=None,
        value=None,
        is_active=True):

    payload = {
        "name": name,
        "type": _type,
        "value": value,
        "is_active": is_active}
    url = obp_api_host + '/obp/{version}/banks/{BANK_ID}/attribute'.format(version=version, BANK_ID=bank_id)

    return makePostRequest(url, payload)
