from obp_python.deleteBank import deleteBank
from obp_python.getAuthorityDataRequestsForBank import getAuthorityDataRequestsForBank
from obp_python.deleteDynamicEntity import deleteDynamicEntity

# Set Bank Id here:
#bank_id = "ADOPEM"
#bank_id = "POPULAR"
#bank_id = 'APAP'
# bank_id = "CONFISA"
bank_id = 'SCOTIABANK'

# Get rid of the bank with everything
authority_requests = getAuthorityDataRequestsForBank(bank_id).json()['authority_data_request_list']
for i in authority_requests:
 	deleteDynamicEntity(i['authority_data_request_id'])
res = deleteBank(bank_id)
#print(res.status_code)