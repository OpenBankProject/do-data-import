from .config import obp_api_host, version
from .makeRequests import makeGetRequest


def get_user_customer_link_by_customer(bank_id, customer_id):

  url = obp_api_host + '/obp/{version}/banks/{BANK_ID}/user_customer_links/customers/{CUSTOMER_ID}'.format(version=version,BANK_ID=bank_id, CUSTOMER_ID=customer_id )
  
  return makeGetRequest(url)
