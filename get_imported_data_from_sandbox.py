from obp_python.getFirehoseAccountsForBank import getFirehoseAccountsforBank
from obp_python.getCustomersForBank import getCustomersForBank
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

customers = getCustomersForBank(bank_id).json()["customers"]
print("Customers: \n\n\n")
print(customers)


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

print("Accounts: \n\n\n")
print(all_accounts)

# Check Branches

res = getBranches(bank_id).json()["branches"]
print("Branches: \n\n\n")
print(res)

# Check Authority Data Requests

res = getAuthorityDataRequestsForBank(bank_id).json()['authority_data_request_list']
print("Authority Data Requests: \n\n\n")
print(res)
