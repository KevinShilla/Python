import time

TRANSFER_TIME = 1
def USD_TSH(USD_to_TSH,TSH,USD,EURO):
    print("Transferring the money...")
    for i in range(TRANSFER_TIME, TRANSFER_TIME+4):
        time.sleep(TRANSFER_TIME)
    print("DONE!")
    print("Current Money: ")
    TSH += 2355.00 * USD_to_TSH
    USD -= USD_to_TSH
    print("USD: $" + str(USD))
    print("TSH: TSH " + str(TSH))
    print("EURO: €" + str(EURO))

def TSH_USD(TSH_to_USD,TSH,USD,EURO):
    print("Transferring the money...")
    for i in range(TRANSFER_TIME, TRANSFER_TIME+4):
        time.sleep(TRANSFER_TIME)
    TSH_TO_USD_RATE = 0.42/1000
    print("DONE!")
    print("Current Money: ")
    TSH -= TSH_to_USD 
    USD += TSH_to_USD * TSH_TO_USD_RATE
    print("USD: $" + str(USD))
    print("TSH: TSH " + str(TSH))
    print("EURO: €" + str(EURO))    
    
def USD_EURO(USD_to_EURO,TSH,USD,EURO):
    print("Transferring the money...")
    for i in range(TRANSFER_TIME, TRANSFER_TIME+4):
        time.sleep(TRANSFER_TIME)
    print("DONE!")
    print("Current Money: ")
    USD_TO_EURO_RATE = 0.89
    EURO += USD_to_EURO * USD_TO_EURO_RATE
    USD -= USD_to_EURO
    print("USD: $" + str(USD))
    print("TSH: TSH " + str(TSH))
    print("EURO: €" + str(EURO))    

def TSH_EURO(TSH_to_EURO,TSH,USD,EURO):
    print("Transferring the money...")
    for i in range(TRANSFER_TIME, TRANSFER_TIME+4):
        time.sleep(TRANSFER_TIME)
    print("DONE!")
    print("Current Money: ")
    TSH_TO_EURO_RATE = 0.38/1000
    TSH -= TSH_to_EURO
    EURO += TSH_to_EURO * TSH_TO_EURO_RATE
    print("USD: $" + str(USD))
    print("TSH: TSH " + str(TSH))
    print("EURO: €" + str(EURO))    
    
def EURO_TSH(EURO_to_TSH,TSH,USD,EURO):
    print("Transferring the money...")
    for i in range(TRANSFER_TIME, TRANSFER_TIME+4):
        time.sleep(TRANSFER_TIME)
    print("DONE!")
    print("Current Money: ")
    EURO_TO_TSH_RATE = 2640.13
    TSH += EURO_to_TSH * EURO_TO_TSH_RATE
    EURO -= EURO_to_TSH
    print("USD: $" + str(USD))
    print("TSH: TSH " + str(TSH))
    print("EURO: €" + str(EURO))    

def EURO_USD(EURO_to_USD,TSH,USD,EURO):
    print("Transferring the money...")
    for i in range(TRANSFER_TIME, TRANSFER_TIME+4):
        time.sleep(TRANSFER_TIME)
    print("DONE!")
    print("Current Money: ")
    EURO_TO_USD_RATE = 1.12
    USD += EURO_to_USD * EURO_TO_USD_RATE
    EURO -= EURO_to_USD
    print("USD: $" + str(USD))
    print("TSH: TSH " + str(TSH))
    print("EURO: €" + str(EURO))     


USD_to_TSH = 0.00
TSH_to_USD = 0.00
USD_to_EURO = 0.00
TSH_to_EURO = 0.00
EURO_to_TSH = 0.00
EURO_to_USD = 0.00
USD = 50000.00
TSH = 100000000.00
EURO = 75000.00
print("Welcome to Bank of the world!")
print()
print("--------------------------------------")
print("Current Money: ")
print("USD: $50,000")
print("TSH: TSH 100,000,000")
print("EURO: €75,000")
print("--------------------------------------")
print("Transfer your money currency from one place to another: ")
print()
print("1: Transfer USD to TSH (1.00 USD = 2355.00)")
print("2: Transfer TSH to USD (1000 TSH = 0.42)")
print("3: Transfer USD to EURO (1.00 USD = 0.89)")
print("4: Transfer TSH to EURO (1000 TSH = 0.38)")
print("5: Transfer EURO to TSH (1.00 EURO = 2640.13 TSH)")
print("6: Transfer EURO to USD (1.00 EURO = 1.12 USD )")

choice = int(input("Transfer #: "))

while choice < 1 or choice > 6:
    choice = int(input("Please pick one of the numbers given: "))

if choice == 1:
    USD_to_TSH = float(input("How much money do you want to transfer from USD to TSH: "))
    USD_TSH(USD_to_TSH,TSH,USD,EURO)
if choice == 2:
    TSH_to_USD = float(input("How much money do you want to transfer from TSH to USD: "))
    TSH_USD(TSH_to_USD,TSH,USD,EURO)
if choice == 3:
    USD_to_EURO = float(input("How much money do you want to transfer from USD to EURO: "))
    USD_EURO(USD_to_EURO,TSH,USD,EURO)
if choice == 4:
    TSH_to_EURO = float(input("How much money do you want to transfer from TSH to EURO: "))
    TSH_EURO(TSH_to_EURO,TSH,USD,EURO)
if choice == 5:
    EURO_to_TSH = float(input("How much money do you want to transfer from EURO to TSH: "))
    EURO_TSH(EURO_to_TSH,TSH,USD,EURO)
if choice == 6:
    EURO_to_USD = float(input("How much money do you want to transfer from EURO to USD: "))
    EURO_USD(EURO_to_USD,TSH,USD,EURO)

print()
print()
print("--------------------------------------")
print("THANK YOU FOR USING BANK OF THE WORLD!")

