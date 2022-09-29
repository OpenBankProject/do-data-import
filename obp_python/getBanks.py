from .config import obp_api_host, version
from .makeRequests import makeGetRequest


def getBanks():

  url = obp_api_host + '/obp/{version}/banks'.format(version=version)
  res = makeGetRequest(url)
  return res
