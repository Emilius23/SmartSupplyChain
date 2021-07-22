# Import accounts(library), config (private key), Smart Contract
from brownie import accounts, config, SupplyChainV1

# Begin main function
def main():
    # ===========RFID SMART CONTRACT VARIABLES TO BE UPDATED===========
    # Step 1:
    # Retrieve product_ID & trasnsactionStage variables from RFID RC522
    f = open("rfid_info.txt", "r")
    product_ID = (f.readline())
    transStage  = (f.readline())
    f.close() 
    # ============SET KEY PARAMETERS FOR THIS PYTHON SCRIPT============
    # Step 2:
    #Get PRIVATE KEY of the account to be charged Transaction Gas Fees for “writing” into Smart Contract
    account = accounts.add(config["wallets"]["from_key"])
    # Step 3:
    # Create an object used to identify the latest deployment
    SupplyChainV1_contract = SupplyChainV1[len(SupplyChainV1) - 1]
    # =============RUN FUNCTION TO SET NEW RFID VARIABLES===============
    # Step 4:
    x = SupplyChainV1_contract.updateStage(product_ID, transStage, {"from": account})
    #Open the file
    file = open("trans_log.txt", "a")
    #Convert values to string type
    x_str = repr(x.txid)
    #Write with elimination 
    file.write(x_str + "\n")
    #close the file
    file.close()