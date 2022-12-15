from decouple import config
import plaid
from plaid.api import plaid_api
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.transactions_sync_request import TransactionsSyncRequest
import json
from werkzeug.wrappers import response
from plaid.exceptions import ApiException


from model import Transaction, Budget, Category, User, connect_to_db
# from server import BANK_ID


def generate_access_token(banknum):
    client_id = config('PLAID_CLIENT_ID')
    secret = config('PLAID_SECRET')

    configuration = plaid.Configuration(
        host=plaid.Environment.Sandbox,
        api_key={
            'clientId': client_id,
            'secret': secret,
            'plaidVersion': '2020-09-14'
        }
    )
    api_client = plaid.ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)

    # # INSTITUTION_ID="ins_109508" # first platypus bank https://plaid.com/docs/sandbox/institutions/

    pt_request = SandboxPublicTokenCreateRequest(
        institution_id=banknum,
        initial_products=[Products('transactions')],
    )
    pt_response = client.sandbox_public_token_create(pt_request)
    # The generated public_token can now be exchanged for an access_token
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )
    exchange_response = client.item_public_token_exchange(exchange_request)
    access_token = exchange_response['access_token']

    return access_token

# request = TransactionsSyncRequest(
#     access_token=access_token
# )

# def get_api_data():
#     cursor = '' #empty cursor to recieve historical updates

#     global added # only made added global for now bc none of the 
#     added = []
#     modified = []
#     removed = []
#     has_more = True

#     try:
#     # Iterate through each page of new transaction updates for item
#         while has_more:# and count <5:
#             request = TransactionsSyncRequest(
#                 access_token=access_token,
#                 cursor=cursor,
#             )
#             response = client.transactions_sync(request)
#             added.extend(response['added'])
#             modified.extend(response['modified'])
#             removed.extend(response['removed'])
#             has_more = response['has_more']
#             # Update cursor to the next cursor
#             cursor = response['next_cursor']


#     except plaid.ApiException as e:
#         print("Plaid api error")
#         # error_response = format_error(e)
#         # return jsonify(error_response)
#     return modified

# def load_transactions():
#     # first drop all existing data from the database
#     for item in added:
#         trans = Transaction(user_id=5,
#                             account_id=item['account_id'],
#                             bank_name=,
#                             vendor=item['merchant_name'],
#                             amount=item['amount'],
#                             date=item['date'])


# def send_response_to_file(listname):
#     print("Writing to json file")
#     with open("saved_response.json", "w") as fp:
#         json.dump(listname,fp)
#     print("writing complete")

# def read_response_from_file(filename):
#     with open(filename, 'rb') as fp:
#         n_list = json.load(fp)
#         return n_list

#if __name__ == "__main__":
    #transactions_list  = get_api_data()
    # send_response_to_file(transactions_list)
    # new_trans_list = read_response_from_file("saved_response.json")

