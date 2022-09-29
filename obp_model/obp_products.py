from obp_python.createProduct import createProduct
from obp_python.getProduct import getProduct


class OBPProduct:
	def __init__(
			self,
			bank_id: str,
			product_code: str
	):
		self.bank_id = bank_id
		self.product_code = product_code
		self.name = ""
		self.parent_product_code = ""
		self.more_info_url = ""
		self.details = ""
		self.description = ""
		self.license_id = ""
		self.license_name = ""

	def create_product(self):
		res = createProduct(
			bank_id=self.bank_id,
			product_code=self.product_code,
			name=self.name,
			parent_product_code=self.parent_product_code,
			more_info_url=self.more_info_url,
			details=self.details,
			description=self.description,
			license_id=self.license_id,
			license_name=self.license_name
		)
		return res

def check_product_exists(bank_id: str, product_code: str):
	res = getProduct(bank_id=bank_id, product_code=product_code)
	if res.status == 200:
		return True
	else:
		return False








