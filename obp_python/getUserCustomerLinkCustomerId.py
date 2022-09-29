from .makeRequests import makeGetRequest
from .config import obp_api_host

def getUserCustomerLinkByCustomerId( bank_id=None, customer_id=None):
  """
  Get customer id by customer id.

  Required roles: CanGetCustomer
  e.g. obp addrole --role-name CanCreateCardsForBank --bank-id gh.29.uk.x
  """

  url = obp_api_host + '/obp/v4.0.0/banks/{bank_id}/user_customer_links/customers/{customer_id}'.format(bank_id=bank_id, customer_id=customer_id)
  req = makeGetRequest(url)
  return req