from obp_python.getUserCustomerLinkCustomerId import getUserCustomerLinkByCustomerId
from obp_python.getCustomerIdByCustomerNumber import getCustomerIdByCustomerNumber
from obp_python.getFirehoseAccountsForBank import getFirehoseAccountsforBank
from config import bank_id, user_prefix, run_prefix, max_row
import config


def get_obp_date_string(datetimeobject):
    return datetimeobject.strftime("%Y-%m-%dT%H:%M:%SZ")


def get_user_id_from_customer_id(bank_id, customer_id):
    try:
        user_id = getUserCustomerLinkByCustomerId(bank_id, customer_id).json()["user_customer_links"][0]["user_id"]
    except IndexError:
        user_id = ""
    return user_id


def get_all_customers_and_accounts(sheet):
    client_ids_with_duplicates = []
    for row in sheet.iter_rows(min_row=2, max_col=31, max_row=max_row):
        client_ids_with_duplicates.append(row[config.ClientID].value)
    client_ids = set(client_ids_with_duplicates)
    customer_ids = []
    user_accounts = []
    res = getFirehoseAccountsforBank(bank_id)
    all_accounts = res.json()['accounts']
    for client_id in client_ids:
        try:
            customer_id = getCustomerIdByCustomerNumber(bank_id, client_id).json()["customer_id"]
            customer_ids.append(customer_id)
        except KeyError:
            continue
        except Exception as e:
            continue
        user_accounts.append([x["id"] for x in all_accounts if x["owners"][0]["id"] == user_prefix + run_prefix + str(client_id)])
    user_accounts_flat = [item for sublist in user_accounts for item in sublist]
    return customer_ids, user_accounts_flat

def create_dummy_dob_dependants(dependants):
    dependants_dob = []
    if dependants == 0:
        return dependants_dob
    for i in range(0, dependants):
        dependants_dob.append("2013-01-21T23:08:00Z")
    return dependants_dob







