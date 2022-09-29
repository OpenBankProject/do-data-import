import requests
from .config import obp_api_host
from .makeRequests import makePostRequest

def addRole(role=None, bank_id=None, user_id=None):

  if bank_id is None:
    payload = {"bank_id":"", "role_name": role}
  elif bank_id is not None:
    payload = {"bank_id": bank_id, "role_name": role}
  
  url = obp_api_host + '/obp/v3.1.0/users/{user_id}/'.format(user_id=user_id) + 'entitlements'

  req = makePostRequest(url, payload)

  return req

