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
```
curl --location --request POST 'localhost:8080/my/logins/direct' \
--header 'Authorization: DirectLogin username="tobwoln8",password="password",consumer_key=zn52gyqmefztfiuylwup25timhaezqi0y3ej301n' \
--header 'Content-Type: application/json' 
```

### Get Bank

```
curl --location --request GET 'localhost:8080/obp/v3.1.0/banks/ADOPEM'
```

### Get Customer by CustomerNumber
```
curl --location --request POST 'localhost:8080/obp/v4.0.0/banks/ADOPEM/customers/customer-number' \
--header 'Authorization: DirectLogin token=eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.qkTKhbS-RmJO8qeFC3b_A83Od979KT3UQ3h7xv6gp_o' \
--header 'Content-Type: application/json' \
--data-raw '{  "customer_number":"4578102"}'
```
[API Explorer documentation](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv3_1_0-getCustomerByCustomerNumber&currentTag=Customer#OBPv3_1_0-getCustomerByCustomerNumber)
### Get Account by AccountRouting
```
curl --location --request POST 'localhost:8080/obp/v5.0.0/management/accounts/account-routing-query' \
--header 'Content-Type: application/json' \
--header 'Authorization: DirectLogin token=eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.qkTKhbS-RmJO8qeFC3b_A83Od979KT3UQ3h7xv6gp_o' \
--data-raw '{
    "bank_id": "ADOPEM",
    "account_routing": {
        "scheme": "account_number",
        "address": "50000210007693"
    }
}'
```
[API Explorer documentation](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv4_0_0-getAccountByAccountRouting&currentTag=Account#OBPv4_0_0-getAccountByAccountRouting)
### Get Branches for a Bank

```
curl --location --request GET 'localhost:8080/obp/v3.0.0/banks/ADOPEM/branches' \
--header 'Authorization: DirectLogin token=eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.qkTKhbS-RmJO8qeFC3b_A83Od979KT3UQ3h7xv6gp_o' \
--header 'Content-Type: application/json'
```

### Get Authority Data Requests

```
curl --location --request GET 'localhost:8080/obp/dynamic-entity/banks/POPULAR/authority_data_request' \
--header 'Authorization: DirectLogin token=eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.qkTKhbS-RmJO8qeFC3b_A83Od979KT3UQ3h7xv6gp_o' \
--header 'Content-Type: application/json'
```

### Another yet undisclosed Summary Endpoint

Will give ALL information by Customer Number.


### Get Banks
Use Endpoint [Get Bank](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv4_0_0-getBank&currentTag=Bank#OBPv4_0_0-getBank)

### Get Customers

Use Endpoint [Get Customers at Bank](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv5_0_0-getCustomersAtOneBank&currentTag=Customer#OBPv5_0_0-getCustomersAtOneBank)

### Get Accounts with Product attributes (Productos)

Use Endpoint [Get Fast Firehose Accounts at Bank](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv4_0_0-getFastFirehoseAccountsAtOneBank&currentTag=Account#OBPv4_0_0-getFastFirehoseAccountsAtOneBank)
### Get Branches

Use Endpoint [Get Branches for a Bank](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv5.0.0&operation_id=OBPv3_0_0-getBranches&currentTag=Branch#OBPv3_0_0-getBranches)

### Get Authority Data requests

Use Endpoint [Get Authority Data Requests List](https://ifcsandbox-explorer.openbankproject.com/)
## OBP  Data Integration internals



If you are interested in the scripts underlying api endpoints, or even creating your own upload scripts, 
follow the process below

### If the bank does not exist, create the bank

Use [this endpoint](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-createBank&currentTag=Bank&api-collection-id=#OBPv4_0_0-createBank)
to create your bank.

Needs role "CanCreateBank" on the sandbox.
Will give you the role "CanCreateEntitlementAtOneBank" , so you can grant yourself all roles needed below [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv2_0_0-addEntitlement&currentTag=Role#OBPv2_0_0-addEntitlement)


### If the customer does not exist, create the customer

Customer is the bank object representing the obp user at bank level. A user can have more than one customer object linked to.
See linking customer to user below.
As accounts belong to the (OBP) user in OBP, you do not necessarily need to create a customer if you are only uploading account related data.

Customer is created [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_1_0-createCustomer&currentTag=Customer&api-collection-id=#OBPv3_1_0-createCustomer)

This call will create the customer_id needed for subsequent customer related apis.
Needs role "CanCreateCustomer" for the bank (id), or "CanCreateCustomerAtAnyBank".


Create any bank specific customer attributes that you cannot map to obp generic attributes. [Here](https://apiexplorersandbox.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-createCustomerAttribute&currentTag=Customer&api-collection-id=#OBPv4_0_0-createCustomerAttribute)
Needs role "CanCreateCustomerAttributeAtOneBank" for the bank.

### If the user does not exist, create the user
If there is no suitable (OBP) user created on the sandbox, create the user with [this endpoint](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv2_0_0-createUser&currentTag=User&api-collection-id=#OBPv2_0_0-createUser)
This call will create the user_id needed for subsequent user related apis.

### If the customer object is not linked to the user, create user customer link

Link the user_id to the customer_id (created above) [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=#OBPv2_0_0-createUserCustomerLinks&currentTag=Customer&api-collection-id=#OBPv2_0_0-createUserCustomerLinks)

Needs role "CanCreateUserCustomerLink" at bank level or "CanCreateUserCustomerLinkAtAnyBank".

### Accounts: If the product does not exist, create the Product (optional)

An account is of a certain product in obp ( like "Gold Card", "Generic Debit", "any_arbitrary_string"). As you can specify an empty string for product_code in account creation, you can skip this if you must for some reason.
Create [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_1_0-createProduct&currentTag=Product&api-collection-id=#OBPv3_1_0-createProduct).

Needs role: "CanCreateProduct" at bank level or "CanCreateProductAtAnyBank".
### Accounts: Create Branch if not existing (optional)
If your accounts belong to a specific bank branch, create it [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_0_0-createBranch&currentTag=Branch&api-collection-id=&bank_id=#OBPv3_0_0-createBranch)
 
Needs role "CanCreateBranch" at bank level or "CanCreateBranchAtAnyBank"
### Create the Account 
Note that new created accounts must always  have an balance of zero.
create [here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-addAccount&currentTag=Account&api-collection-id=&bank_id=&account_id=&view_id=&counterparty_id=&transaction_id=#OBPv4_0_0-addAccount)

Needs role "CanCreateAccount" at bank level.

Create any bank specific account attributes that you cannot map to obp generic attributes. [Here](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv3_1_0-createAccountAttribute&currentTag=Account#OBPv3_1_0-createAccountAttribute)
Needs role "CanCreateAccountAttributeAtOneBank" for the bank.

### Deletion: Accounts

The [deleteAccountCascade Endpoint](https://ifcsandbox-explorer.openbankproject.com/?version=OBPv4.0.0&operation_id=OBPv4_0_0-deleteAccountCascade&currentTag=Account#OBPv4_0_0-deleteAccountCascade) will delete an account object along  with all account attributes.
