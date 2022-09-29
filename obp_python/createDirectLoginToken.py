import requests
from json import loads


def createDirectLoginToken(username, user_password, consumer_key, obp_api_host, verify):
	authorization = "DirectLogin username={username},password={user_password},consumer_key={consumer_key}".format(username=username, user_password=user_password, consumer_key=consumer_key)
	headers = {'Content-Type': 'application/json', 'Authorization': authorization}

	payload = None
	url = obp_api_host + "/my/logins/direct"
	try:
		req = requests.post(url, headers=headers, json=payload, verify=verify)
		token = loads(req.text)["token"]
	except Exception as e:
		# no logger here to not have circle dependencies with .config
		print('could not get direct login for: ' + url + " " + username + " " + str(headers))
	return token

