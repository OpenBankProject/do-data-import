from .config import obp_api_host
from .makeRequests import makeDeleteRequest


def deleteUserCustomerLink(bank_id=None, user_customer_link_id=None):

  url = obp_api_host + \
        '/obp/v4.0.0/banks/{bank_id}/user_customer_links/{USER_CUSTOMER_LINK_ID}'.format(bank_id=bank_id, USER_CUSTOMER_LINK_ID=user_customer_link_id)
  req = makeDeleteRequest(url)
  return req
