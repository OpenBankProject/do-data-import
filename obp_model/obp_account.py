from obp_python.createAccount import createAccount
from obp_python.createAccountAttribute import createAccountAttribute
from obp_python.config import settlement_accounts_bank,  settlement_account_sandbox
from obp_python.createHistoricalTransaction import createHistoricalTransaction
from obp_python.createSettlementAccount import create_settlement_account
from obp_python.config import logger
from random import randrange
class OBPAccountBalance:
	def __init__(
			self,
			currency: str,
			amount: str
	):
		self.currency = currency
		self.amount = amount


class OBPAccountRouting:
	def __init__(
			self,
			scheme: str,
			address: str
	):
		self.scheme = scheme
		self.address = address


class OBPAccount:
	def __init__(
			self,
			bank_id,
			user_id,
			label,
			product_code,
			balance: OBPAccountBalance,
			branch_id,
			accountroutings: [OBPAccountRouting]):

		self.bank_id = bank_id
		self.userid = user_id
		self.label = label
		self.product_code = product_code
		self.balance = balance
		self.branchid = branch_id
		self.accountroutings = accountroutings

	# creates account on sandbox
	def create_account(self):
		res = createAccount(
			# bank varchar 44
			self.bank_id,
			# userid
			self.userid,
			# varchar 10
			self.balance.currency,
			# varchar 255
			self.label,
			# varchar 50? from mappedproduct..
			self.product_code,
			# varchar 44
			self.branchid,
			# varchar 32
			self.accountroutings.scheme,
			# varchar 128
			self.accountroutings.address
		)
		balance_amount = float(self.balance.amount)
		logger.debug(f"creating balance transaction for amount: {str(balance_amount)}")
		if balance_amount != 0:
			account_id = res.json()["account_id"]
			if balance_amount < 0:
				createHistoricalTransaction(
					from_account_id=account_id,
					from_bank_id=self.bank_id,
					to_bank_id=settlement_accounts_bank,
					to_account_id=f'{settlement_account_sandbox}_{self.balance.currency}',
					currency=self.balance.currency,
					amount=abs(balance_amount)
					)
			if balance_amount > 0:
				createHistoricalTransaction(
					from_account_id=f'{settlement_account_sandbox}_{self.balance.currency}',
					from_bank_id=settlement_accounts_bank,
					to_bank_id=self.bank_id,
					to_account_id=account_id,
					currency=self.balance.currency,
					amount=balance_amount
				)


		return res


class OBPAccountAttribute:
	def __init__(
			self,
			bank_id, account_id, product_code, attribute_name, attribute_type,
			attribute_value, product_instance_code=None):

		self.bank_id = bank_id
		self.account_id = account_id
		self.product_code = product_code
		self.attribute_name = attribute_name
		self.attribute_type = attribute_type
		self.attribute_value = attribute_value
		self.product_instance_code = product_instance_code

	# creates account attribute on sandbox
	def create_account_attribute(self):
		res = createAccountAttribute(
			bank_id=self.bank_id,
			account_id=self.account_id,
			product_code=self.product_code,
			product_instance_code=self.product_instance_code,
			attribute_name=self.attribute_name,
			attribute_type=self.attribute_type,
			attribute_value=self.attribute_value
			)
		return res


def create_settlement_accounts(bank_id):
	currencies = ["DOP", "USD", "EUR"]
	for currency in currencies:
		create_settlement_account(
			bank_id=bank_id,
			currency=currency,
			scheme="settlement_account",
			address=randrange(100000000000,9999999999999)
		)









