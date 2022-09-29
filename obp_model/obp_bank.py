from obp_python.createBankAttribute import createBankAttribute

def upload_bank_type(bank_id: str, bank_type: str):
	res = createBankAttribute(
		bank_id=bank_id,
		name="bank_type",
		_type="STRING",
		value=bank_type
	)
	return res