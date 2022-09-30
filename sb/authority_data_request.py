from obp_python.createAuthorityDataRequest import createAuthorityDataRequest
from obp_python.createGlobalAuthorityDataRequest import createGlobalAuthorityDataRequest
from obp_python.config import logger


def create_authority_data_request_from_row(row):
	try:
		createAuthorityDataRequest(
			bank_id=row[0].value.strip(),
			customer_nr=str(row[1].value),
			mandate_name=str(row[2].value),
			mandate_name_year=str(row[3].value)
		)
	except Exception as e:
		logger.exception(f'Could not create Autority Data Request from line {row[0].row}. Reason: {e}')


def create_global_authority_data_request_from_row(row):
	try:
		createGlobalAuthorityDataRequest(
			bank_id=row[0].value.strip(),
			customer_nr=str(row[1].value),
			mandate_name=str(row[2].value),
			mandate_name_year=str(row[3].value)
		)
	except Exception as e:
		logger.exception(f'Could not create Autority Data Request from line {row[0].row}. Reason: {e}')

