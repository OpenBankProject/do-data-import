from .config import obp_api_host, version
from .makeRequests import makeDeleteRequest


def deleteAccountCascade(bank_id=None, account_id=None):

  url = obp_api_host + \
        '/obp/{version}/management/cascading/banks/{bank_id}/accounts/{account_id}'.format(version=version, bank_id=bank_id, account_id=account_id)
  req = makeDeleteRequest(url)
  return req
