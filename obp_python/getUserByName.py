from .config import obp_api_host, version
from .makeRequests import makeGetRequest


def getUserByName(name=None):
  url = obp_api_host + '/obp/{version}/users/username/{name}'.format(version=version, name=name)
  return makeGetRequest(url)
