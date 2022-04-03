from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_LOCAL_ENV = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENV
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_keys"])


def get_pricefeed():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        deploy_mocks()
        return MockV3Aggregator[-1].address
    else:
        return config["networks"][network.show_active()]["eth_usd_pricefeed"]


def deploy_mocks():
    # print(f"The active network is {network.show_active()}")
    print(f"the active network is {network.show_active()}")
    print("deploying mocks")
    if len(MockV3Aggregator) == 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        print("mocks deployed")
