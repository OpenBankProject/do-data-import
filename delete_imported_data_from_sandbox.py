from obp_python.deleteBank import deleteBank
from obp_python.config import obp_api_host, logger
from obp_python.getAuthorityDataRequestsForBank import getAuthorityDataRequestsForBank
from obp_python.deleteAuthorityDataRequestAtBank import deleteAuthorityDataRequestAtBank
from obp_python.getCustomersForBank import getCustomersForBank
from obp_python.deleteCustomer import deleteCustomer

# Set Bank Id here:

bank_id = 'bank_id'

# Get rid of the bank with everything

try:
	authority_data_requests = getAuthorityDataRequestsForBank(bank_id).json()["authority_data_request_list"]
	for authority_data_reqest in authority_data_requests:
		res = deleteAuthorityDataRequestAtBank(bank_id, authority_data_reqest["authority_data_request_id"])
except Exception as e:
	logger.exception(f"Could not delete authority data requests: {e}")
try:
	customers = getCustomersForBank(bank_id).json()["customers"]
	for customer in customers:
		deleteCustomer(bank_id, customer["customer_id"])
except Exception as e:
	logger.exception(f"Could not delete customers: {e}")

try:
	res = deleteBank(bank_id)
except Exception as e:
	logger.exception(f"Could not delete bank data: {e}")