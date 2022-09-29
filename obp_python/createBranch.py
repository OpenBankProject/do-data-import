from .config import obp_api_host, version
from .makeRequests import makePostRequest

def createBranch(
        bank_id=None,
        branch_id=None,
        name=None,
        line_1=None,
        city=None,
        county=None):

    payload = {
    "id": branch_id,
    "bank_id": bank_id,
    "name": name,
    "address": {
        "line_1": line_1,
        "line_2": "",
        "line_3": "",
        "city": city,
        "county": county,
        "state": "",
        "postcode": "",
        "country_code": ""
    },
    "location": {
        "latitude": 0,
        "longitude": 0
    },
    "meta": {
        "license": {
            "id": "ODbL-1.0",
            "name": "Open Database License"
        }
    },
    "lobby": {
        "monday": [
            {
                "opening_time": "",
                "closing_time": ""
            }
        ],
        "tuesday": [
            {
                "opening_time": "",
                "closing_time": ""
            }
        ],
        "wednesday": [
            {
                "opening_time": "",
                "closing_time": ""
            }
        ],
        "thursday": [
            {
                "opening_time": "",
                "closing_time": ""
            }
        ],
        "friday": [
            {
                "opening_time": "",
                "closing_time": ""
            }
        ],
        "saturday": [
            {
                "opening_time": "",
                "closing_time": ""
            }
        ],
        "sunday": [
            {
                "opening_time": "",
                "closing_time": ""
            }
        ]
    },
    "drive_up": {
        "monday": {
            "opening_time": "",
            "closing_time": ""
        },
        "tuesday": {
            "opening_time": "",
            "closing_time": ""
        },
        "wednesday": {
            "opening_time": "",
            "closing_time": ""
        },
        "thursday": {
            "opening_time": "",
            "closing_time": ""
        },
        "friday": {
            "opening_time": "",
            "closing_time": ""
        },
        "saturday": {
            "opening_time": "",
            "closing_time": ""
        },
        "sunday": {
            "opening_time": "",
            "closing_time": ""
        }
    },
    "branch_routing": {
        "scheme": "OBP",
        "address": branch_id
    },
    "is_accessible": "",
    "accessibleFeatures": "",
    "branch_type": "",
    "more_info": "",
    "phone_number": ""
}
    url = obp_api_host + '/obp/{version}/banks/{BANK_ID}/branches'.format(version=version, BANK_ID=bank_id)

    return makePostRequest(url, payload)
