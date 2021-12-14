import json
import time

# Opening the file in read mode
fl = open("records.json", "r")
read = fl.read()
fl.close()
records = json.loads(read)
# Taking user input
cust_name = input("Enter customer's name: ")
cust_pno = int(input("Enter customer's phone number: "))
prod_id = int(input("Enter the Poduct ID: "))
prod_name = input("Enter the Product's Name: ")
prod_quant = int(input("Enter the Quantity: "))
if records[str(prod_id)]["Quantity"] < prod_quant:
    print("Item out of Stock")
    exit()  # exiting the code as the entered item is out of stock.
else:
    records[str(prod_id)]["Quantity"] -= prod_quant
    # making the changes in the records.json file
    f1 = open("records.json", "w")
    dp = json.dumps(records)
    f1.write(dp)
    f1.close()
# Printing the Bill
print("*******************")
print("Customer Name: ", cust_name)
print("Customer Phone Number: ", cust_pno)
print("Date & Time of Billing: ", time.ctime())
print("Product: ", prod_name)
print("Quantity: ", prod_quant)
print("Price: ", records[str(prod_id)]["Price"])
print("---------------------------")
print("Billing Amount: ", prod_quant * records[str(prod_id)]["Price"])
print("---------------------------")
print("*******************")
sales = {prod_id: {"Customer Name": cust_name, "Customer Phone Number": cust_pno, "Product Name": prod_name,
                   "Price": records[str(prod_id)]["Price"], "Quantity": records[str(prod_id)]["Quantity"]}}
# Appending the sales.json file
file = open("sales.json", "a+")
dp = json.dumps(sales)
file.write(dp)
file.close()
