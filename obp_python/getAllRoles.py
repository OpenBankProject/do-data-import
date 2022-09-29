from .config import obp_api_host, version
from .makeRequests import makeGetRequest


def getAllRoles():

  url = obp_api_host + '/obp/{version}/roles'.format(version=version)
  
  return makeGetRequest(url)
