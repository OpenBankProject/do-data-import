from .config import obp_api_host
from .makeRequests import makeDeleteRequest


def deleteDynamicEntity(entity_id=None):

  url = obp_api_host + \
        f'/obp/v5.0.0/management/dynamic-entities/{entity_id}'
  req = makeDeleteRequest(url)
  return req
