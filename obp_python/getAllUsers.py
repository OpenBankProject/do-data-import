from .config import obp_api_host, version
from .makeRequests import makeGetRequest


def getAllUsers():

  url = obp_api_host + '/obp/{version}/users?limit=10000'.format(version=version)
  
  return makeGetRequest(url)
