from .config import obp_api_host
from .makeRequests import makeGetRequest


def getCurrentUser():

  url = obp_api_host + '/obp/v4.0.0/users/current'
  
  return makeGetRequest(url)
