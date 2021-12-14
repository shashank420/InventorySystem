import json

file = open("records.json", "r")
read = file.read()
file.close()
records = json.loads(read)
# static record for reference
# record = {
#     1001: {"Product Name": "Biscuit", "Price": 20, "Quantity": 40, "Mfg date": "01/07/21", "Best Before": "6 Months"
#                                                                                                           + "\n"},
#     1002: {"Product Name": "Maggie", "Price": 10, "Quantity": 50, "Mfg date": "01/07/21", "Best Before": "8 Months"
#                                                                                                          + "\n"},
#     1003: {"Product Name": "Frooti", "Price": 20, "Quantity": 30, "Mfg date": "06/07/21", "Best Before": "6 Months"
#                                                                                                          + "\n"},
#     1004: {"Product Name": "Bisleri Water", "Price": 10, "Quantity": 20, "Mfg date": "01/07/21",
#            "Best Before": "1 Month" + "\n"},
#     1005: {"Product Name": "Wai Wai", "Price": 10, "Quantity": 50, "Mfg date": "01/07/21", "Best Before": "6 Months"
#                                                                                                           + "\n"},
#     1006: {"Product Name": "Pens", "Price": 10, "Quantity": 100, "Mfg date": "01/07/21", "Best Before": "NA" + "\n"},
#     1007: {"Product Name": "Pencils", "Price": 5, "Quantity": 50, "Mfg date": "01/07/21", "Best Before": "NA" + "\n"},
#     1008: {"Product Name": "Sharpeners", "Price": 7, "Quantity": 50, "Mfg date": "01/07/21",
#            "Best Before": "NA" + "\n"},
#     1009: {"Product Name": "Erasers", "Price": 5, "Quantity": 50, "Mfg date": "01/07/21", "Best Before": "NA" + "\n"},
#     1010: {"Product Name": "File Papers", "Price": 25, "Quantity": 20, "Mfg date": "01/07/21", "Best Before": "NA"
#                                                                                                               + "\n"},
#     1011: {"Product Name": "Sketch Pens", "Price": 50, "Quantity": 10, "Mfg date": "01/07/21", "Best Before": "NA"
#                                                                                                               + "\n"},
#     1012: {"Product Name": "Dairy Milk", "Price": 20, "Quantity": 20, "Mfg date": "15/07/21",
#            "Best Before": "6 Months" + "\n"},
#     1013: {"Product Name": "Lays", "Price": 10, "Quantity": 40, "Mfg date": "27/07/21",
#            "Best Before": "6 Months" + "\n"},
#     1014: {"Product Name": "Tomato Ketchup", "Price": 20, "Quantity": 20, "Mfg date": "28/07/21",
#            "Best Before": "6 Months" + "\n"},
#     1015: {"Product Name": "Pizza-Pasta Sauce", "Price": 60, "Quantity": 100, "Mfg date": "28/07/21",
#            "Best Before": "6 Months" + "\n"},
#     1016: {"Product Name": "Pencil box", "Price": 30, "Quantity": 10, "Mfg date": "28/07/21",
#            "Best Before": "NA" + "\n"},
#     1017: {"Product Name": "Bread", "Price": 24, "Quantity": 20, "Mfg date": "28/07/21",
#            "Best Before": "5 Days" + "\n"},
#     1018: {"Product Name": "Hair Oil", "Price": 40, "Quantity": 10, "Mfg date": "28/07/21",
#            "Best Before": "36 Months" + "\n"},
#     1019: {"Product Name": "Shampoo", "Price": 60, "Quantity": 20, "Mfg date": "31/07/21",
#            "Best Before": "24 Months" + "\n"},
#     1020: {"Product Name": "Deodorant", "Price": 60, "Quantity": 10, "Mfg date": "31/07/21",
#            "Best Before": "24 Months" + "\n"},
#     1021: {"Product Name": "Sanitizer bottle", "Price": 20, "Quantity": 10, "Mfg date": "31/07/21",
#            "Best Before": "NA" + "\n"},
#     1022: {"Product Name": "Hand wash Liquid", "Price": 50, "Quantity": 20, "Mfg date": "31/07/21",
#            "Best Before": "12 Months" + "\n"},
#     1023: {"Product Name": "Body Lotion", "Price": 40, "Quantity": 10, "Mfg date": "01/08/21",
#            "Best Before": "12 Months" + "\n"},
#     1024: {"Product Name": "Masks", "Price": 10, "Quantity": 30, "Mfg date": "01/08/21", "Best Before": "NA" + "\n"},
#     1025: {"Product Name": "Hair Conditioner", "Price": 50, "Quantity": 10, "Mfg date": "01/08/21",
#            "Best Before": "24 Months" + "\n"},
#     1026: {"Product Name": "Fried Rice Masala", "Price": 10, "Quantity": 20, "Mfg date": "01/08/21",
#            "Best Before": "6 Months" + "\n"},
#     1027: {"Product Name": "Manchurian Masala", "Price": 20, "Quantity": 10, "Mfg date": "05/08/21",
#            "Best Before": "6 Months" + "\n"},
#     1028: {"Product Name": "Chow mein", "Price": 20, "Quantity": 10, "Mfg date": "08/08/21", "Best Before": "6 Months"
#                                                                                                             + "\n"},
#     1029: {"Product Name": "Pasta", "Price": 50, "Quantity": 5, "Mfg date": "05/08/21",
#            "Best Before": "6 Months" + "\n"},
#     1030: {"Product Name": "Fevicol", "Price": 10, "Quantity": 30, "Mfg date": "10/08/21", "Best Before": "NA" + ""}}

# Taking user input to add more items in the inventory
inp = int(input("What you want to do?" + "\n" + "Press 1 for adding new Products." + "\n" +
                "Press 2 for adding existing Products." + "\n"))
prod_id = int(input("Enter the Product's ID: "))
prod_name = input("Enter the Product's Name: ")
prod_quantity = int(input("Enter the Product's Quantity: "))
if inp == 1:
    prod_price = int(input("Enter the Product's Price: "))
    prod_mfg_date = input("Enter the Product's Manufacturing Date: ")
    prod_best_bef = input("Enter the Product's Best Before: ")
    records[prod_id] = {"Product Name": prod_name, "Price": prod_price, "Quantity": prod_quantity,
                        "Mfg Date": prod_mfg_date, "Best Before": prod_best_bef}
elif inp == 2 and str(prod_id) in records:
    records[str(prod_id)]["Quantity"] += prod_quantity
else:
    print("Invalid Input.")

# Creating a dictionary of stated items in records.json file
js = json.dumps(records)
fd = open("records.json", "w")
fd.write(js)
print("Changes successfully made!")
fd.close()
