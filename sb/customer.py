from obp_model.obp_customer import OBPCustomer, OBPCustomerAttribute
from obp_python.config import logger
from obp_python.updateCustomerNumber import updateCustomerNumber

def create_customer_from_row(row):
	try:
		bank_id = row[0].value.strip()
		customer = OBPCustomer(
			bank_id=bank_id,
			legal_name=row[3].value
		)
		res = customer.create_customer()
		customer_id = res.json()['customer_id']
		updateCustomerNumber(
			bank_id=bank_id,
			customer_id=customer_id,
			customer_number=row[1].value
		)

		customer_type = OBPCustomerAttribute(
			bank_id=bank_id,
			customer_id=customer_id,
			attribute_name="customer_type",
			attribute_value=row[2].value
		)
		customer_type.create_customer_attribute()
		surname_or_acronym = OBPCustomerAttribute(
			bank_id=bank_id,
			customer_id=customer_id,
			attribute_name="surname_or_acronym",
			attribute_value=row[4].value
		)
		surname_or_acronym.create_customer_attribute()
		relationship = OBPCustomerAttribute(
			bank_id=bank_id,
			customer_id=customer_id,
			attribute_name="relationship",
			attribute_value=row[5].value
		)
		relationship.create_customer_attribute()
		relationship_description = OBPCustomerAttribute(
			bank_id=bank_id,
			customer_id=customer_id,
			attribute_name="relationship_description",
			attribute_value=row[6].value
		)
		relationship_description.create_customer_attribute()
		if row[7].value:
			client_consents = OBPCustomerAttribute(
				bank_id=bank_id,
				customer_id=customer_id,
				attribute_name="client_consents",
				attribute_value=row[7].value
			)
			client_consents.create_customer_attribute()
	except Exception as e:
		logger.exception(f'Could not create Customer from line {row[0].row}. Reason: {e}')