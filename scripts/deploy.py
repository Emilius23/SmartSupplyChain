#Import Smart COntract object, config, network for Kovan and accounts
from brownie import SupplyChainV1, config, network, accounts

#Define main function
def main():
    #Declare an object that stores PRIVATE KEY value of Kovan account
    my_account = accounts.add(config["wallets"]["from_key"])
    #Run .deploy METHOD to deploy the smart contract
    SupplyChainV1.deploy({'from': my_account})