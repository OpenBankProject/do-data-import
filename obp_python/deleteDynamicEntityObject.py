from .config import obp_api_host
from .makeRequests import makeDeleteRequest


def deleteDynamicEntityObject(bank_id, entity_id, entity_object_id):

  url = obp_api_host + \
        f'/obp/dynamic-entity/banks/{bank_id}/{entity_id}/{entity_object_id}'
  req = makeDeleteRequest(url)
  return req
