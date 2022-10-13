## Usage Guide

This document explains how to load the Dominican Republic SB Data Dictionary into the IFC OBP Sandbox and query it.

Python Scripts are provided which read the spreadsheets and call the OBP APIs.


### Configure the script

We need to copy the script config and modify it - and add our username / password and consumer key.

1) cp ./obp_python/example_config.py to ./obp_python/config.py 
2) add your [username / password](https://ifcsandbox.openbankproject.com/user_mgt/sign_up) and [consumer key](https://ifcsandbox.openbankproject.com/consumer-registration) 

### Copy your data set to  the data  sheet

We need to copy the spreadsheet template and then add your own data. Please do not change the structure of the spreadsheet in any way.

1) cp resources/sb_import_template.xlsx to resources/sb_import.xlsx
2) import your data set into the spreadsheet resources/sb_import.xlsx_

### Use the script

We need to import the data and check it loaded ok. We can also remove the data.

1) To import data:
 run upload_data_set_to_sandbox.py
   
2) To check imported data:
run get_imported_data_from_sandbox.py
Note: sb data set productos are account attributes within obp accounts
   
3) To delete imported data:
 run delete_imported_data_from_sandbox.py

   
## Endpoints for retrieving the data

There are multiple endpoints you can use to inspect and update the data. Here we list a basic set. 

You need to be authenticated and authorised before you can call most of the endpoints.

The simplest way to authenticate is via Direct Login. You can also try the endpoints in API Explorer. API Explorer will tell you if you need a Role and you can request it on API Explorer by clicking a button there. Please contact support in case you need a Role.

### Get Direct Login Token

For development purposes, you could use an easy access authentication, called direct login:
Register your username and password [here](https://ifcsandbox.openbankproject.com/user_mgt/sign_up)
Get your consumer key [here](https://ifcsandbox.openbankproject.com/consumer-registration)

Example (replace $YOUR_CONSUMER_KEY with your consumer key, not consumer secret):
```
curl --location --request POST 'https://ifcsandbox.openbankproject.com/my/logins/direct' \
--header 'Authorization: DirectLogin username="YOURUSERNAME",password="password",consumer_key=$YOUR_CONSUMER_KEY' \
--header 'Content-Type: application/json' 
```
Replace $YOUR_DIRECT_LOGIN_TOKEN in the Examples below with the token you get!

### Get Bank
Use Endpoint [Get Bank](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv5_0_0-getBank&currentTag=Bank#OBPv5_0_0-getBank)

Example:
```
curl --location --request GET 'https://ifcsandbox.openbankproject.com/obp/v5.0.0/banks/ADOPEM'
```
### Get Customers

Use Endpoint [Get Customers at Bank](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv5_0_0-getCustomersAtOneBank&currentTag=Customer#OBPv5_0_0-getCustomersAtOneBank)

Example:
```
curl --location --request GET 'https://ifcsandbox.openbankproject.com//obp/v5.0.0/banks/ADOPEM/customers' \
--header 'Authorization: DirectLogin token=$YOUR_DIRECT_LOGIN_TOKEN'
```
### Get Customer by CustomerNumber
Use Endpoint [Get Customer by CustomerNumber](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv3_1_0-getCustomerByCustomerNumber&currentTag=Customer#OBPv3_1_0-getCustomerByCustomerNumber)

Example:

```
curl --location --request POST 'https://ifcsandbox.openbankproject.com/obp/v4.0.0/banks/ADOPEM/customers/customer-number' \
--header 'Authorization: DirectLogin token=$YOUR_DIRECT_LOGIN_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{  "customer_number":"4578102"}'
```
### Get all accounts for one Bank
Use Endpoint [Get Fast Firehose Accounts at Bank](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv4_0_0-getFastFirehoseAccountsAtOneBank&currentTag=Account#OBPv4_0_0-getFastFirehoseAccountsAtOneBank).
Take a look at the documentation regarding the pagination

Example:
```
curl --location --request GET 'https://ifcsandbox.openbankproject.com//obp/v5.0.0/management/banks/ADOPEM/fast-firehose/accounts?limit=100&offset=0' \
--header 'Authorization: DirectLogin token=$YOUR_TOKEN' 
```
### Get Account by AccountRouting
Use this Endpoint [Get Account by AccountRouting](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv4_0_0-getAccountByAccountRouting&currentTag=Account#OBPv4_0_0-getAccountByAccountRouting)

Example
```
curl --location --request POST 'https://ifcsandbox.openbankproject.com/obp/v5.0.0/management/accounts/account-routing-query' \
--header 'Content-Type: application/json' \
--header 'Authorization: DirectLogin token=$YOUR_DIRECT_LOGIN_TOKEN' \
--data-raw '{
    "bank_id": "ADOPEM",
    "account_routing": {
        "scheme": "account_number",
        "address": "50000210007693"
    }
}'
```
### Get Branches for a Bank

```
curl --location --request GET 'https://ifcsandbox.openbankproject.com/obp/v3.0.0/banks/ADOPEM/branches' \
--header 'Authorization: DirectLogin token=$YOUR_DIRECT_LOGIN_TOKEN' \
--header 'Content-Type: application/json'
```

### Get Authority Data Requests
Use the Endpoint [Get Authority Data Request List](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv4_0_0-dynamicEntity_getauthority_data_requestList_ADOPEM&currentTag=_Authority%20Data%20Request(ADOPEM)#OBPv4_0_0-dynamicEntity_getauthority_data_requestList_ADOPEM)

Technically, each bank has its own endpoint, but those only differ in the BANK_ID.
Example:
```
curl --location --request GET 'https://ifcsandbox.openbankproject.com//obp/dynamic-entity/banks/POPULAR/authority_data_request' \
--header 'Authorization: DirectLogin token=$YOUR_DIRECT_LOGIN_TOKEN' 
```

### Get Customer Overview

Use the endpoint [Get Customer Overview Flat](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv5_0_0-getCustomerOverviewFlat&currentTag=Customer#OBPv5_0_0-getCustomerOverviewFlat) to get all relavent information of a customer by their Customer Number.

Example:
```
curl --location --request POST 'https://ifcsandbox.openbankproject.com//obp/v5.0.0/banks/ADOPEM/customers/customer-number-query/overview-flat' \
--header 'Authorization: DirectLogin token=$YOUR_DIRECT_LOGIN_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customer_number": "4578102"
```
## Endpoints for uploading the data



If you are interested in the scripts underlying api endpoints, or even creating your own upload scripts, 
follow the process below

### Create bank

Use Endpoint  [create Bank](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-createBank&currentTag=Bank&api-collection-id=#OBPv4_0_0-createBank)
to create your bank.

Needs role "CanCreateBank" on the sandbox.
Will give you the role "CanCreateEntitlementAtOneBank" , so you can grant yourself all roles needed below [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv2_0_0-addEntitlement&currentTag=Role#OBPv2_0_0-addEntitlement)


### Create customer

Use Endpoint [Create Customer](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_1_0-createCustomer&currentTag=Customer&api-collection-id=#OBPv3_1_0-createCustomer)
The OBP modell demands information that you do not have. So for creation, there is the need to add some default values.
Those could be hidden in the responses by query parameter, though.

Example of minimal working create Customer:

```
curl --location --request POST 'https://ifcsandbox.openbankproject.com//obp/v5.0.0/banks/APAP/customers' \
--header 'Authorization: DirectLogin token=YOUR_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
    "legal_name": "Herbert Muller",
    "mobile_phone_number": "",
    "email": "",
    "face_image": {
        "url": "",
        "date": "1100-01-01T00:00:00Z"
    },
    "date_of_birth": "1100-01-01T00:00:00Z",
    "relationship_status": "",
    "dependants": 0,
    "dob_of_dependants": [
    ],
    "credit_rating": {
        "rating": "",
        "source": ""
    },
    "credit_limit": {
        "currency": "",
        "amount": ""
    },
    "highest_education_attained": "",
    "employment_status": "",
    "kyc_status": true,
    "last_ok_date": "1100-01-01T00:00:00Z",
    "title": "",
    "branch_id": "",
    "name_suffix": ""
}'
```
This call will create the customer_id needed for subsequent customer related apis.
Needs role "CanCreateCustomer" for the bank (id), or "CanCreateCustomerAtAnyBank".


Create any bank specific customer attributes that you cannot map to obp generic attributes. [Here](https://apiexplorersandbox.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-createCustomerAttribute&currentTag=Customer&api-collection-id=#OBPv4_0_0-createCustomerAttribute)
Needs role "CanCreateCustomerAttributeAtOneBank" for the bank.
### Update customer number

Use Endpoint [Update the number of a Customer](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_1_0-updateCustomerNumber&currentTag=Customer&api-collection-id=#OBPv3_1_0-updateCustomerNumber) to change the automatically created Customernumber to the real value

Example: 
```
curl --location --request PUT 'https://ifcsandbox.openbankproject.com//obp/v5.0.0/banks/APAP/customers/7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh/number' \
--header 'Authorization: DirectLogin token=$YOUR_TOKEN' \
--header 'Content-Type: application/json' 
--data-raw '{
    "customer_number": "5987953"
}'
```
### Accounts: If the product does not exist, create the Product

An account is of a certain product in obp ( like "Gold Card", "Generic Debit", "any_arbitrary_string"). If you want to add account attributes, which is what you want to do, you  need to name a product for account creation (next step)
Create [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_1_0-createProduct&currentTag=Product&api-collection-id=#OBPv3_1_0-createProduct).

Needs role: "CanCreateProduct" at bank level or "CanCreateProductAtAnyBank".
### Create the Account 
Note that new created accounts must always  have an balance of zero. So we need to make a initial transaction to/from the account to a settlement account 
create [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-addAccount&currentTag=Account&api-collection-id=&bank_id=&account_id=&view_id=&counterparty_id=&transaction_id=#OBPv4_0_0-addAccount)

Example:
```
curl --location --request POST 'https://ifcsandbox.openbankproject.com/obp/v5.0.0/banks/APAP/accounts' \
--header 'Content-Type: application/json' \
--header 'Authorization: DirectLogin token=$YOUR_TOKEN' \
--data-raw '{
    "user_id": "",
    "label": "",
    "product_code": "Basic",
    "balance": {
        "currency": "DOP",
        "amount": "0"
    },
    "branch_id": "",
    "account_routings": [
        {
            "scheme": "account_number",
            "address": "799245353490933"
        }
    ]
}'
```
Needs role "CanCreateAccount" at bank level.

Create any bank specific account attributes that you cannot map to obp generic attributes. [Here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_1_0-createAccountAttribute&currentTag=Account#OBPv3_1_0-createAccountAttribute)
Needs role "CanCreateAccountAttributeAtOneBank" for the bank.
### Create the settlement accounts

To make the initial transfer to set the balance, you will need a settlement account on the bank where this transaction goes to/ comes from.
You will need one settlement account per currency.

Example:
```
curl --location --request POST 'https://ifcsandbox.openbankproject.com/obp/v5.0.0/banks/APAP/settlement-accounts' \
--header 'Content-Type: application/json' \
--header 'Authorization: DirectLogin token=$YOUR_TOKEN' \

--data-raw '{
    "user_id": "",
    "payment_system": "SANDBOX-TAN",
    "balance": {
        "currency": "DOP",
        "amount": "0"
    },
    "label": "",
    "branch_id": "",
    "account_routings": [
        {
            "scheme": "settlement",
            "address": "12345678"
        }
    ]
}'
```

### Create the balance
Use Endpoint [Create Historical Transactions](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-createHistoricalTransactionAtBank&currentTag=Transaction-Request#OBPv4_0_0-createHistoricalTransactionAtBank)
to create a transaction from (positive balance) or from (negative balance) the settlement account.
Settlement account_id will be: SANDBOX-TAN_SETTLEMENT_ACCOUNT_$CURRENCY <- replace $CURRENCY with the currency.

E.g. : SANDBOX-TAN_SETTLEMENT_ACCOUNT_DOP

Example:
```
curl --location --request POST 'https://ifcsandbox.openbankproject.com/obp/v5.0.0/banks/ADOPEM/management/historical/transactions' \
--header 'Content-Type: application/json' \
--header 'Authorization: DirectLogin token=$YOUR_TOKEN' \
--data-raw '{
    "from_account_id": "SANDBOX-TAN_SETTLEMENT_ACCOUNT_DOP",
    "to_account_id": "6153fd73-c5c8-449f-8f2c-a360f4ee2f9f",
    "value": {
        "currency": "DOP",
        "amount": "2230"
    },
    "description": "this is for work",
    "posted": "1100-01-01T01:01:01Z",
    "completed": "1100-01-01T01:01:01Z",
    "type": "SANDBOX_TAN",
    "charge_policy": "SHARED"
```

### Create Branch
Use Endpoint [Create Branch](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_0_0-createBranch&currentTag=Branch&api-collection-id=&bank_id=#OBPv3_0_0-createBranch)
Needs role "CanCreateBranch" at bank level or "CanCreateBranchAtAnyBank"


### Create Authority Data Requests

Use Endpoint [Create new Authority Data Request](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-dynamicEntity_createauthority_data_request_ADOPEM&currentTag=_Authority%20Data%20Request(ADOPEM)#OBPv4_0_0-dynamicEntity_createauthority_data_request_ADOPEM)

Technically, each bank has its own endpoint, but those only differ in the BANK_ID.
