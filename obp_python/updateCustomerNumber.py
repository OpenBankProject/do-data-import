from obp_python.makeRequests import makePutRequest
from .config import obp_api_host, version

def updateCustomerNumber(bank_id=None, customer_id=None, customer_number=None):


  payload = {
      "customer_number": customer_number
    }

  url = obp_api_host + '/obp/{version}/banks/{bank_id}/customers/{customer_id}/number'.format(version=version, bank_id=bank_id, customer_id=customer_id)

  req = makePutRequest(url, payload)



  return req
