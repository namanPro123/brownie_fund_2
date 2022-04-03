from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENV
from scripts.deploy import deploy_fund_me
from brownie import network, exceptions, accounts
import pytest


def test_can_fund_winthdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    expected = 1000000000000000
    fund_txn = fund_me.fund({"from": account, "value": expected})
    fund_txn.wait(1)
    assert fund_me.get_value_paid(account) == expected
    withdrw_txn = fund_me.withdraw({"from": account})
    withdrw_txn.wait(1)
    assert fund_me.get_value_paid(account) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip("only for local blockchains")
    account = get_account()
    fund_me = deploy_fund_me()
    actor_wallet = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": actor_wallet})
