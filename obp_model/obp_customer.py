from obp_python.createCustomer import createCustomer
from obp_python.createCustomerAttribute import createCustomerAttribute
from obp_model.constants import DUMMY_DATE


class OBPCustomer:
	def __init__(
			self,
			bank_id,
			legal_name
	):
		#  bank_id varchar 44
		self.bank_id = bank_id
		# legal_name varchar 255
		self.legal_name = legal_name
		# mobile_phone_number = varchar 50
		self.mobile_phone_number = ""
		# email = varchar 200
		self.email = ""
		# face image url = varchar 2000
		self.face_image_url = ""
		# timestamp
		self.face_image_date = DUMMY_DATE
		# timestamp
		self.date_of_birth = DUMMY_DATE
		# relation_ship status = varchar 16
		self.relationship_status = ""
		# dependents integer
		self.dependants = 0
		# timestamp
		self.dob_dependants = []
		# credit rating rating varchar 100
		self.credit_rating_rating = ""
		# credti rating source varchar 100
		self.credit_rating_source = ""
		# credit limit currency varchar 100
		self.credit_limit_currency = ""
		# credit limit amount varchar 100
		self.credit_limit_amount = ""
		# highest education attained varchar 32
		self.highest_education_attained = ""
		# employment status varchar 32
		self.employment_status = ""
		# kyc status boolean
		self.kyc_status = True
		# title varchar 255
		self.title = ""
		# branch id varchar 255
		self.branch_id = ""
		# timestamp
		self.last_ok_date = DUMMY_DATE
		# name suffix varchar 255
		self.name_suffix = ""

	def create_customer(self):
		res = createCustomer(
			bank_id=self.bank_id,
			legal_name=self.legal_name,
			mobile_phone_number=self.mobile_phone_number,
			email=self.email,
			face_image_url=self.face_image_url,
			face_image_date=self.face_image_date,
			date_of_birth=self.date_of_birth,
			relationship_status=self.relationship_status,
			dependants=self.dependants,
			dob_dependants=self.dob_dependants,
			credit_rating_rating=self.credit_rating_rating,
			credit_rating_source=self.credit_rating_source,
			credit_limit_currency=self.credit_limit_currency,
			credit_limit_amount=self.credit_limit_amount,
			highest_education_attained=self.highest_education_attained,
			employment_status=self.employment_status,
			kyc_status=self.kyc_status,
			last_ok_date=self.last_ok_date,
			title=self.title,
			branch_id=self.branch_id,
			name_suffix=self.name_suffix
		)
		return res


class OBPCustomerAttribute:
	def __init__(
			self,
			bank_id, customer_id, attribute_name,
			attribute_value):
			self.bank_id = bank_id
			self.customer_id = customer_id
			self.attribute_name = attribute_name
			self.attribute_type = "STRING"
			self.attribute_value = attribute_value
	def create_customer_attribute(self):
		res = createCustomerAttribute(
			self.bank_id,
			self.customer_id,
			self.attribute_name,
			self.attribute_type,
			self.attribute_value
			)
		return res.status_code
