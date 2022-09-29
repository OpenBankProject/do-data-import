from .config import obp_api_host
from .makeRequests import makePostRequest


def createCustomerAttribute(bank_id=None, customer_id=None,  attribute_name=None, attribute_type=None, attribute_value=None):
    """Create a customer in Open Bank Project.
  
  Requires entitlements: CanCreateCustomer or CanCreateCustomerAtAnyBank
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """

    payload = {
        "name": attribute_name,
        "type": attribute_type,
        "value": attribute_value
    }
    url = obp_api_host + '/obp/v4.0.0/banks/{bank_id}/customers/{customer_id}/attribute'.format(bank_id=bank_id,
                                                                                                customer_id=customer_id)
    req = makePostRequest(url, payload)
    return req
