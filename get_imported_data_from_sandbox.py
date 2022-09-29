from obp_python.getFirehoseAccountsForBank import getFirehoseAccountsforBank
from obp_python.getFirehoseCustomersForBank import getFirehoseCustomersforBank
from obp_python.getBanks import getBanks
from obp_python.getBranches import getBranches
from obp_python.getAuthorityDataRequestsForBank import getAuthorityDataRequestsForBank


# Set Bank Id here:
#bank_id = "tobank"
bank_id = "ADOPEM"
#bank_id = "POPULAR"
#bank_id = 'APAP'
# bank_id = "CONFISA"
#bank_id = 'SCOTIABANK'
#Check Bank

res = getBanks()
print(res)

# Check customers
try:
	all_customers = []
	offset = 0
	step_size = 50
	result_nr = step_size
	metrics_total = []
	count = 0

	while result_nr == step_size:
		res = getFirehoseCustomersforBank(bank_id=bank_id, limit=str(step_size), offset=str(offset))
		customers = res.json()["customers"]
		for i in customers:
			all_customers.append(i)
		result_nr = len(customers)
		offset = offset + step_size
except Exception as e:
	print(str(e))

# Check Accounts
offset = 0
step_size = 10
result_nr = step_size
metrics_total = []
count = 0
all_accounts = []
while result_nr == step_size:
	res = getFirehoseAccountsforBank(bank_id=bank_id, limit=str(step_size), offset=str(offset))
	accounts = res.json()["accounts"]
	for i in accounts:
		all_accounts.append(i)
	result_nr = len(accounts)
	offset = offset + step_size

print(all_accounts)

# Check Branches

res = getBranches(bank_id).json()["branches"]
print(res)

# Check Authority Data Requests

res = getAuthorityDataRequestsForBank(bank_id).json()['authority_data_request_list']
print(res)
