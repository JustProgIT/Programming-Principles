import json
from datetime import datetime
from functions import *

while True:
    choose_action = input('''
    Choose the action:
    1 - View products
    2 - View suppliers
    3 - View orders
    4 - Add new product
    5 - Update product
    6 - Add new supplier
    7 - Place an order
    8 - Report of supply orders
    9 - Report of low stock items
    0 - To exit the program
                          
    Type the number to perform required action: ''')
    
    if choose_action == '1' or choose_action.lower().replace(' ', '') == 'product' or choose_action.lower().replace(' ', '') == 'viewproduct':
        showProducts()
    elif choose_action == '2' or choose_action.lower().replace(' ', '') == 'supplier' or choose_action.lower().replace(' ', '') == 'viewsupplier':
        showSuppliers()
    elif choose_action == '3' or choose_action.lower().replace(' ', '') == 'order' or choose_action.lower().replace(' ', '') == 'vieworder':
        showOrders()
    elif choose_action == '4' or choose_action.lower().replace(' ', '') == 'newproduct' or choose_action.lower().replace(' ', '') == 'np':
        supplier_list = getSupplierDetails()
        new_product_name = input('Type the name of the product: ')
        new_product_description = input('Type the brief description of the product: ')
        showSuppliers()
        while True:
            product_supplier_id = input('Type the id of the supplier: ')
            if product_supplier_id.isdigit():
                product_supplier_id = int(product_supplier_id)
                for supplier in supplier_list:
                    if supplier['id'] == product_supplier_id:
                        break
                else:
                    print('No supplier with such id! Try again...')
                    continue
                break
            else:
                print('It should be an integer! Try again...')
        while True:
            new_product_quantity = input('Type the quantity of the product: ')

            if new_product_quantity.isdigit():
                break
            else:
                print('The quantity should be a number!')
        while True:
            new_product_price = input('Type the price of the product: ')

            if new_product_price.isdigit():
                addNewProduct(new_product_name, new_product_description, product_supplier_id, new_product_quantity, new_product_price)
                break
            else:
                print('The price should be a number!')
        showProducts()
    elif choose_action == '5' or choose_action.lower().replace(' ', '') == 'update' or choose_action.lower().replace(' ', '') == 'updateproduct':
        while True:
            showProducts()
            product_list = getProductsDetails()
            product_id = input('Type the id of the product you want to update: ')
            if product_id.isdigit():
                product_id = int(product_id)
            else:
                print('Not an id! Try again...')
                continue
            # Check if the product exists in the product list
            delete_product_choice = 0
            for product_items in product_list:
                if product_items['id'] == product_id:
                    while True:
                        delete_product_choice = input('Do you want to delete this product (y/n): ')
                        if delete_product_choice == '1' or delete_product_choice.lower() == 'y':
                            deleteProduct(product_id)
                            showProducts()
                            break
                        elif delete_product_choice == '0' or delete_product_choice.lower() == 'n':
                            break
                        else:
                            print('I dont understand! Type y or n...')
                    if delete_product_choice == 'n' or delete_product_choice == 0:
                        product_name = input('Type the new NAME of the product (or leave empty if no changes): ')
                        product_description = input('Type the new brief DESCRIPTION of the product (or leave empty if no changes): ')
                        product_quantity = input('Type the new QUANTITY of the product (or leave empty if no changes): ')
                        product_price = input('Type the new PRICE of the product (or leave empty if no changes): ')

                        product_name = None if product_name == '' else product_name
                        product_description = None if product_description == '' else product_description
                        product_price = None if product_price == '' else product_price
                        product_quantity = None if product_quantity == '' else product_quantity

                        updateProduct(product_id, product_name, product_description, product_quantity, product_price)
                        showProducts()
                        break
                    break
            else:
                print('No such product! Try again...')
                continue
            break

    elif choose_action == '6' or choose_action.lower().replace(' ', '') == 'newsupplier' or choose_action.lower().replace(' ', '') == 'ns':
        new_supplier_name = input('Type the name of the supplier: ')
        while True:
            new_supplier_contact = input('Type the contact of the supplier (including + sign): ')
            if 10 <= len(new_supplier_contact) <= 15 and new_supplier_contact[0] == '+':
                addNewSupplier(new_supplier_name, new_supplier_contact)
                break
            else:
                print('Phone number is incorrect or in the incorrect form. Try other number...')
        showSuppliers()
    elif choose_action == '7' or choose_action.lower().replace(' ', '') == 'placeorder' or choose_action.lower().replace(' ', '') == 'po':
        while True: 
            showProducts()                                                                                                                      #show products have
            product_list = getProductsDetails()                                                                                                 #get lists of products
            product_id = input('Type the id of the product you want to add into order: ')                                                       #getting id user wants to order
            if product_id.isdigit():                                                                                                            #check if id is number
                product_id = int(product_id)                                                                                                    #convert to int if it is number
            else:                                                   
                print('Not an id! Try again...')                                                                                                #if not then print error
                continue                                                                                                                        #continue asking the id
            product_quantity_real = 0                                                                                                           #new variable
            for product_item in product_list:                                                                                                   #going through the list of products
                if product_item['id'] == product_id:                                                                                            #check if the id exists
                    product_quantity_real = int(product_item['quantity'])                                                                       #assign the variable with the quantity of requested items available
                    price_of_product = product_item['price']
                    while True:                                                             
                        quantity = input('Type the quantity of the product you want to order: ')                                                #getting quantity use wants to order
                        if quantity.isdigit():                                                                                                  #check if user typed number
                            quantity = int(quantity)                                                                                            #make int if number
                            if product_quantity_real >= quantity:                                                                               #check if the quantity user wants is sufficient to what have in storage
                                updateProduct(product_id, quantity=product_quantity_real-quantity)                                              #updates the amount of products in the storage
                                break                                                                                                           #finish and move to placing order if everythin good
                            else:                                                                                                               
                                print('Not enough in storage! Try different amount...')                                                         #print error if not sufficent amount
                        else:                                                   
                            print('Not an number! Try again...')                                                                                #print error if quantity is not a number
                    addNewOrderById(product_id, quantity, price_of_product*quantity)                                                            #add new order if everything good
                    break                                                                                                                       #finish with this action
            else:                                                   
                print('No such product! Try again...')                                                                                          #print error if no product with requested id
                continue
            break
    elif choose_action == '8' or choose_action.lower().replace(' ', '') == 'supplyorder' or choose_action.lower().replace(' ', '') == 'so':
        product_list = getProductsDetails()
        supplier_list = getSupplierDetails()
        order_list = getOrderDetails()
        supplier_order_list = []
        showSuppliers()
        while True:
            supplier_id = input('Type the id of the supplier: ')
            if supplier_id.isdigit():
                supplier_id = int(supplier_id)
                for supplier in supplier_list:
                    if supplier['id'] == supplier_id:
                        break
                else:
                    print('No supplier with such id! Try again...')
                    continue
                break
            else:
                print('It should be an integer! Try again...')
        for product in product_list:
            if product['supplier_id'] == supplier_id:
                for order in order_list:
                    if  order['product_id'] == product['id']:
                        supplier_order_list.append(order)
        if len(supplier_order_list) >= 1:
            with open('reports/supply_orders.txt', 'w') as file:
                file.write(str(supplier_order_list))
            print('Succesfully generated report!')
        else:
            print('No records of order from this supplier!')

    elif choose_action == '9' or choose_action.lower().replace(' ', '') == 'lowstock' or choose_action.lower().replace(' ', '') == 'ls':
        product_list = getProductsDetails()
        low_stock_items = []
        for product in product_list:
            if product['quantity'] < 10:
                low_stock_items.append(product['name'])
        if len(low_stock_items) > 1:
            for low_stock_item in low_stock_items:
                print(f'{low_stock_item}', end=' ')
            print('are low in stock')
        elif len(low_stock_items) == 1:
            print(f'{low_stock_items[0]} is low on stock!')
        else:
            print('There is enough items in storage!')
    elif choose_action == '0':
        print('Goodbye!')
        break
    else:
        print('Sorry I dont understand your choice, try nunbers...')