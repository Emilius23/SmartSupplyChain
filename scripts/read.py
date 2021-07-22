# Import accounts(library), config (private key), Smart Contract (SC)
from brownie import accounts, config, SupplyChainV1
# Import module that supplies classes for manipulating dates and times.
import datetime
# Import module that enables processing of arrays
from array import *

#Declare global variable array of unsigned long values
my_array = array('L',[0,0,0])



# Begin MAIN function
def main():

    # ============SET KEY PARAMETERS FOR THIS PYTHON SCRIPT============
    # Step 1:
    # Create an object used to identify the latest deployment
    SupplyChainV1_contract = SupplyChainV1[len(SupplyChainV1) - 1]
    # =============RUN FUNCTION TO READ RFID VARIABLES=================
    # Step 2:
    my_array = SupplyChainV1_contract.readStage()
    # ================PERFORM VARIABLE CONVERSIONS=====================
    # Step 3:
    # Convert received timestamp to human readable date
    datetime_time = datetime.datetime.fromtimestamp(my_array[2])
    # Step 4:
    # Print the received RFID variables from SC to Terminal
    print(f"Searched product_ID is: {my_array[0]}")
    print(f"Current Stage is: {my_array[1]}")
    print(f"Last update was at: {datetime_time}")