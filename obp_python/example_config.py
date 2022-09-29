import logging
#Edit

# obp username and password as registered with official! bank email address here:
# https://ifcsandbox.openbankproject.com/user_mgt/sign_up
username = "username"
user_password = "userpasswd"
# Your consumer key, get it here:
# https://ifcsandbox.openbankproject.com/consumer-registration
consumer_key = "customerkey"
# End Edit
# defaults below should be fine, just change loglevel to Debug if needed
obp_api_host = "https://ifcsandbox.openbankproject.com/"
# change below to this if you need debugging: logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("obp_python")
logger.propagate = True
settlement_accounts_bank = "obp1"
settlement_account_sandbox = "SANDBOX-TAN_SETTLEMENT_ACCOUNT"
version = "v4.0.0"
verify = True

#pycharm