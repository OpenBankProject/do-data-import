from .config import obp_api_host, version
from .makeRequests import makePostRequest


def createAccountAttribute(bank_id=None, account_id=None, product_code=None, product_instance_code=None, attribute_name=None, attribute_type=None,
                            attribute_value=None):
    """Create a customer in Open Bank Project.
  
  Requires entitlements: CanCreateCustomer or CanCreateCustomerAtAnyBank
  To add entitlements with cli: `obp addrole --role-name=<role-name>`
  """

    payload = {
        "name": attribute_name,
        "type": attribute_type,
        "value": attribute_value,
        "product_instance_code": product_instance_code
    }
    url = obp_api_host + '/obp/v5.0.0/banks/{bank_id}/accounts/{account_id}/products/{product_code}/attribute'.format(bank_id=bank_id,account_id=account_id, product_code=product_code)
    req = makePostRequest(url, payload)
    return req
