from .config import obp_api_host, version
from .makeRequests import makePostRequest


def create_settlement_account(bank_id,
                              currency,
                              scheme,
                              address,
                              user_id="",
                              payment_system="SANDBOX-TAN",
                              label="",
                              branch_id="",
                              amount="0"
                              ):

    payload = {
    "user_id": user_id,
    "payment_system": payment_system,
    "balance": {
        "currency": currency,
        "amount": amount
    },
    "label": label,
    "branch_id": branch_id,
    "account_routings": [
        {
            "scheme": scheme,
            "address": address
        }
        ]
    }
    url = obp_api_host + f'/obp/{version}/banks/{bank_id}/settlement-accounts'

    return makePostRequest(url, payload)
