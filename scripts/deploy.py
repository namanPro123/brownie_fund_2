from brownie import fundme, network, config
from scripts.helpful_scripts import get_account, get_pricefeed


def deploy_fund_me():
    account = get_account()
    fund_me = fundme.deploy(
        get_pricefeed(),
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("publish_source"),
    )
    print(fund_me.address)
    return fund_me


def main():
    deploy_fund_me()
