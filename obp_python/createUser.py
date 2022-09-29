from .config import obp_api_host, version
from .makeRequests import makePostRequest


def createUser(username=None, email=None, password=None,
                first_name=None, last_name=None):

    payload = {
          "username": username,
          "email": email,
          "password": password,
          "first_name": first_name,
          "last_name": last_name
        }
    url = obp_api_host + '/obp/{version}/users'.format(version=version)

    return makePostRequest(url, payload)
