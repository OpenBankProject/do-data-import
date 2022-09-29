import requests
from .config import logger, verify, username, user_password, consumer_key, obp_api_host
from obp_python.createDirectLoginToken import createDirectLoginToken
obp_auth_token = createDirectLoginToken(username, user_password, consumer_key, obp_api_host, verify)
authorization = 'DirectLogin token="{}"'.format(obp_auth_token)
default_headers = {'Content-Type': 'application/json',
           'Authorization': authorization}


def check400status(req):
    if req.status_code >= 400:
        logger.error("Request: " + req.url + " has bad result, code: " + str(req.status_code))
        logger.error(req.text)
    else:
        logger.debug("Result for request: " + req.url + " :")
        logger.debug(req.status_code)
        logger.debug(req.text)
    return req


def makeGetRequest(url, headers=default_headers):
    req = requests.get(url, headers=headers, verify=verify)
    return check400status(req)


def make_get_request_with_body(url, payload, headers=default_headers):
    req = requests.request(method='get', url=url, headers=headers, json=payload, verify=verify)
    return check400status(req)


def makePutRequest(url,payload, headers=default_headers):
    req = requests.put(url, headers=headers, json=payload, verify=verify)
    return check400status(req)


def makePostRequest(url,payload, headers=default_headers):
    req = requests.post(url, headers=headers, json=payload, verify=verify)
    return check400status(req)


def makeDeleteRequest(url, headers=default_headers):
    req = requests.delete(url, headers=headers, verify=verify)
    return check400status(req)


def makePostRequestData(url, payload, headers=default_headers):
    req = requests.post(url, headers=headers, data=payload, verify=verify)
    return check400status(req)
