from .config import obp_api_host, version
from .makeRequests import makePostRequest


def create_authority_data_request_instance_at_bank(bank_id):

    payload = {
        "authority_data_request": {
            "description": "Legal request to give customer data to the authorities",
            "required": [
                "customer_number"
            ],
            "properties": {
                "customer_number": {
                    "type": "string",
                    "example": "1234567",
                    "description": "Customer reference number"
                },
                 "mandate_name": {
                    "type": "string",
                    "example": "National Anti-Fraud Act",
                    "description": "The legal act the request is based on"
                },
                 "mandate_name_year": {
                    "type": "string",
                    "example": "1978",
                    "description": "The year when the legal act the request is based on was passed"
                }
            }
    }}
    url = obp_api_host + f'/obp/v4.0.0/management/banks/{bank_id}/dynamic-entities'

    return makePostRequest(url, payload)
