from brownie import accounts, config, SimpleStorage, network


def get_account():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():
    account = get_account()
    # account = accounts.add(config["wallets"]["from_key"])

    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = (
        simple_storage.retrieve()
    )  # no need to add from account because it is a view function only
    print(stored_value)

    transaction = simple_storage.storeNumber(
        69, {"from": account}
    )  # need to add from account since it changes state
    transaction.wait(1)  # wait for 1 block

    updated_value = simple_storage.retrieve()
    print(updated_value)


def main():
    deploy_simple_storage()
