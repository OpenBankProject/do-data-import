from obp_python.deleteBank import deleteBank



bank_ids = ["ADOPEM", "POPULAR", 'APAP', "CONFISA", "SCOTIABANK", "SCOTIABANK "]

for bank_id in bank_ids:
	res = deleteBank(bank_id)
	print(res.status_code)