from brownie import fundme, MockV3Aggregator
from scripts.helpful_scripts import get_account
from web3 import Web3


def fund():
    account = get_account()
    fund_me = fundme[-1]
    amount = 1000000000000000
    agg_contract = MockV3Aggregator[-1]
    (fksdkfl, price, sdnfls, nsnf, nfsjn) = agg_contract.latestRoundData()
    print(price)
    print(fund_me.valueofEthintermsofUsd())
    # print(fund_me.getEntranceFee())
    print(fund_me.convert(10000000000000000))
    fund_me.fund({"value": amount, "from": account})


def withdraw():
    account = get_account()
    fund_me = fundme[-1]
    fund_me.withdraw({"from": account})


def main():
    # print(get_account().balance())
    fund()
    # print(get_account().balance())
    # print(fundme[-1].get_value_paid(get_account()))
    withdraw()
    # print(get_account().balance())
    # print(fundme[-1].get_value_paid(get_account()))
