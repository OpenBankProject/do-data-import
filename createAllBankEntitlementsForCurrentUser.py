from obp_python.getAllRoles import getAllRoles
from obp_python.addRole import addRole
from obp_python.getCurrentUser import getCurrentUser
from json import loads


def create_bank_entitlements_for_user(bank_id):
	user_id = getCurrentUser().json()["user_id"]
	all_roles = loads(getAllRoles().text)["roles"]
	all_bank_role_names = [x["role"] for x in all_roles if x["requires_bank_id"]]

	for role in all_bank_role_names:
		try:
			addRole(role, bank_id, user_id)
		except:
			print("did not work")

def create_authority_data_request_roles(bank_id):
	try:
		user_id = getCurrentUser().json()["user_id"]
		addRole('CanCreateDynamicEntity_authority_data_request', "", user_id)
	except Exception as e:
		print(f"could not create auth data request roles: {e}")

