from obp_python.createBank500 import createBank500
from obp_python.config import logger
from obp_model.obp_bank import upload_bank_type


def create_bank_from_row(row):
	try:
		bank_id = row[0].value.strip()
		res = createBank500(
			id=bank_id,
			bank_code=bank_id,
			full_name=row[2].value,
			logo_url=row[3].value,
			website_url=row[4].value
		)
	except Exception as e:
		logger.exception(f'Could not create Bank: {e}')


def create_bank_attribute_from_row(row):
	bank_id = row[0].value.strip()
	res = upload_bank_type(
		bank_id=bank_id,
		bank_type=row[1].value
	)


