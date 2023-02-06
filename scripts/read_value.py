from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]  # takes the most recent contract deployment
    print(simple_storage.retrieve())


def main():
    read_contract()
