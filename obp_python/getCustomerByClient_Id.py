from .makeRequests import makeGetRequest
from .config import obp_api_host, version

def get_customer_by_client_id( bank_id=None, client_id=None):

  url = obp_api_host + '/obp/{version}/banks/{bank_id}/customers?client_id={client_id}'.format(version=version, bank_id=bank_id, client_id=client_id)
  req = makeGetRequest(url)
  return req
