from .config import obp_api_host
from .makeRequests import makePutRequest


def createProduct(
        bank_id="",
        product_code="",
        name="",
        parent_product_code="",
        more_info_url="",
        details="",
        description="",
        license_id="",
        license_name=""
        ):

    payload = {
        "parent_product_code": parent_product_code,
        "name": name,
        "more_info_url": more_info_url,
        "terms_and_conditions_url": details,
        "description": description,
        "meta": {
            "license": {
                "id": license_id,
                "name": license_name}
        }
    }

    url = obp_api_host \
    + '/obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}'.format(BANK_ID=bank_id,PRODUCT_CODE=product_code)

    return makePutRequest(url, payload)
