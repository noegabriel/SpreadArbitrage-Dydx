# from decouple import config
from dydx3 import Client
from web3 import Web3
from program.filled_constants import (
    HOST,
    ETHEREUM_ADDRESS,
    DYDX_API_KEY,
    DYDX_API_SECRET,
    DYDX_API_PASSPHRASE,
    STARK_PRIVATE_KEY,
    HTTP_PROVIDER,
)


# Connect to DYDX
def connect_dydx():

    # Create Client Connection
    client = Client(
        host=HOST,
        api_key_credentials={
            "key": DYDX_API_KEY,
            "secret": DYDX_API_SECRET,
            "passphrase": DYDX_API_PASSPHRASE,
        },
        stark_private_key=STARK_PRIVATE_KEY,
        eth_private_key="0x79dba39a833d9bc44d2dde00586fcf743f01d2c4925bf7015608c646d61a42a4",
        default_ethereum_address=ETHEREUM_ADDRESS,
        web3=Web3(Web3.HTTPProvider(HTTP_PROVIDER)),
    )

    # Confirm client
    account = client.private.get_account()
    account_id = account.data["account"]["id"]
    quote_balance = account.data["account"]["quoteBalance"]
    print("Connection Successful")
    print("Account ID: ", account_id)
    print("Quote Balance: ", quote_balance)

    # Return Client
    return client
