from .config import obp_api_host, version
from .makeRequests import makeDeleteRequest


def deleteAccountAttributeDefinition(bank_id=None, attribute_definition_id=None):

  url = obp_api_host + \
        '/obp/{version}/banks/{bank_id}/attribute-definitions/{attribute_definition_id}/account'.format(version=version, bank_id=bank_id, attribute_definition_id=attribute_definition_id)
  req = makeDeleteRequest(url)
  return req
