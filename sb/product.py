from obp_model.obp_account import OBPAccountAttribute, OBPAccount, OBPAccountBalance, OBPAccountRouting
from obp_model.obp_products import OBPProduct
from obp_python.getProduct import getProduct
from obp_python.createProduct import createProduct
from obp_python.getAccount_by_Account_Routing import getAccountByAccountRouting
from obp_python.config import logger


def create_product_from_row(row):
	try:
		bank_id = row[0].value.strip()
		account_number = row[5].value
		product_code = row[2].value
		res = getProduct(bank_id, product_code)
		if res.status_code != 200:
			attribute_product = OBPProduct(
				bank_id=bank_id,
				product_code=product_code
			)
			try:
				res = attribute_product.create_product()

			except Exception as e:
				logger.error(f"could not create basic product: {e}")
			createProduct(bank_id=bank_id, product_code=product_code)
		product_instance_code = row[3].value
		try:
			account_id = getAccountByAccountRouting(
				bank_id=bank_id,
				account_routing_scheme="account_number",
				account_routing_address=account_number
			).json()["id"]
		except KeyError:
			account_balance = OBPAccountBalance(
				currency="DOP",
				amount="0"
			)
			account_routing = OBPAccountRouting(
				scheme="account_number",
				address=account_number
			)
			account = OBPAccount(
				bank_id=bank_id,
				user_id="",
				label="",
				product_code=product_code,
				balance=account_balance,
				branch_id="",
				accountroutings=account_routing
			)
			account_id = account.create_account().json()["account_id"]


		product_description = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			product_instance_code=product_instance_code,
			attribute_name='product_description',
			attribute_type='STRING',
			attribute_value=row[5].value
		)
		product_description.create_account_attribute()
		issuance_amount = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			product_instance_code=product_instance_code,
			attribute_name='issuance_amount',
			attribute_type='STRING',
			attribute_value=row[6].value
		)
		issuance_amount.create_account_attribute()
		interest_rate = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			product_instance_code=product_instance_code,
			attribute_name='interest_rate',
			attribute_type='STRING',
			attribute_value=row[7].value
		)
		interest_rate.create_account_attribute()
		term = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			product_instance_code=product_instance_code,
			attribute_name='term',
			attribute_type='STRING',
			attribute_value=row[8].value
		)
		term.create_account_attribute()
		if row[9].value:
			form_of_payment = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='form_of_payment',
				attribute_type='STRING',
				attribute_value=row[9].value
			)
			form_of_payment.create_account_attribute()
		if row[10].value:
			interest_amount = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='interest_amount',
				attribute_type='STRING',
				attribute_value=row[10].value
			)
			interest_amount.create_account_attribute()
		if row[11].value:
			branch_code = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='branch_code',
				attribute_type='STRING',
				attribute_value=row[11].value
			)
			branch_code.create_account_attribute()
		if row[12].value:
			payment_method = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='payment_method',
				attribute_type='STRING',
				attribute_value=row[12].value
			)
			payment_method.create_account_attribute()
		if row[13].value:
			opening_date = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='opening_date',
				attribute_type='STRING',
				attribute_value=row[13].value
			)
			opening_date.create_account_attribute()
		if row[14].value:
			maturity_date = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='maturity_date',
				attribute_type='STRING',
				attribute_value=row[14].value
			)
			maturity_date.create_account_attribute()
		if row[15].value:
			renewal_date = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='renewal_date',
				attribute_type='STRING',
				attribute_value=row[15].value
			)
			renewal_date.create_account_attribute()
		if row[16].value:
			cancellation_date = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='cancellation_date',
				attribute_type='STRING',
				attribute_value=row[16].value
			)
			cancellation_date.create_account_attribute()
		instrument_status_code = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			product_instance_code=product_instance_code,
			attribute_name='instrument_status_code',
			attribute_type='STRING',
			attribute_value=row[17].value
		)
		instrument_status_code.create_account_attribute()
		instrument_status_definition = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			product_instance_code=product_instance_code,
			attribute_name='instrument_status_definition',
			attribute_type='STRING',
			attribute_value=row[18].value
		)
		instrument_status_definition.create_account_attribute()
		if row[19].value:
			is_substituted = OBPAccountAttribute(
				bank_id=bank_id,
				account_id=account_id,
				product_code=product_code,
				product_instance_code=product_instance_code,
				attribute_name='is_substituted',
				attribute_type='STRING',
				attribute_value=row[19].value
			)
			is_substituted.create_account_attribute()
	except Exception as e:
		logger.exception(f'Could not create Product attributes from line {row[0].row}. Reason: {e}')

