from obp_model.obp_account import OBPAccount, OBPAccountBalance, OBPAccountRouting, OBPAccountAttribute
from obp_model.obp_products import OBPProduct
from obp_python.config import logger
from sb.util import get_string_from_string_or_date

def create_account_from_row(row, date_format):
	try:
		bank_id=row[0].value.strip()
		product_code = 'Basic'
		basic_product = OBPProduct(
			bank_id=bank_id,
			product_code=product_code
		)
		try:
			res = basic_product.create_product()

		except Exception as e:
			logger.error(f"could not create basic product: {e}")
		account_balance = OBPAccountBalance(
			currency=row[9].value.strip(),
			amount=row[8].value
		)
		account_routing = OBPAccountRouting(
			scheme="account_number",
			address=row[2].value
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
		res = account.create_account()
		account_id = res.json()["account_id"]
		customer_number = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			attribute_name='customer_number',
			attribute_type='STRING',
			attribute_value=row[1].value
		)
		customer_number.create_account_attribute()
		account_number = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			attribute_name='account_number',
			attribute_type='STRING',
			attribute_value=row[2].value
		)
		account_number.create_account_attribute()
		account_status = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			attribute_name='account_status',
			attribute_type='STRING',
			attribute_value=row[3].value
		)
		account_status.create_account_attribute()
		issue_date = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			attribute_name='issue_date',
			attribute_type='STRING',
			attribute_value=get_string_from_string_or_date(row[4].value, date_format)
		)
		issue_date.create_account_attribute()
		last_movement_date = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			attribute_name='last_movement_date',
			attribute_type='STRING',
			attribute_value=get_string_from_string_or_date(row[5].value, date_format)
		)
		last_movement_date.create_account_attribute()
		capital_amount = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			attribute_name='capital_amount',
			attribute_type='STRING',
			attribute_value=row[6].value
		)
		capital_amount.create_account_attribute()
		interest_amount = OBPAccountAttribute(
			bank_id=bank_id,
			account_id=account_id,
			product_code=product_code,
			attribute_name='interest_amount',
			attribute_type='STRING',
			attribute_value=row[7].value
		)
		interest_amount.create_account_attribute()
	except Exception as e:
		logger.exception(f'Could not create Account from line {row[0].row}. Reason: {e}')