import json
from functions import *

while True:
    if programIsReady():
        choose_action = input('''
        Choose the action:
        [1] - View products
        [2] - View suppliers
        [3] - View orders
        [4] - Add new product
        [5] - Update product
        [6] - Add new supplier
        [7] - Place an order
        [8] - Report of supplier sales
        [9] - Report of low stock items
        [10] - Report of supply products
        [0] - To exit the program
                            
        Type the number to perform required action: ''')                                                                                                            #Asking user to pick action
        
        
        if choose_action == '1' or choose_action.lower().replace(' ', '') == 'product' or choose_action.lower().replace(' ', '') == 'vp':
            showProducts()                                                                                                                                          #If 1 shows products available
        
        elif choose_action == '2' or choose_action.lower().replace(' ', '') == 'supplier' or choose_action.lower().replace(' ', '') == 'vs':
            showSuppliers()                                                                                                                                         #If  2 shows suppliers available
        
        elif choose_action == '3' or choose_action.lower().replace(' ', '') == 'order' or choose_action.lower().replace(' ', '') == 'vo':
            showOrders()                                                                                                                                            #If 3 shows orders available
        
        elif choose_action == '4' or choose_action.lower().replace(' ', '') == 'newproduct' or choose_action.lower().replace(' ', '') == 'np':
            new_product_name = input('Type the name of the product: ')                                                                                              #Ask name of new product
            new_product_description = input('Type the brief description of the product: ')                                                                          #Ask new description
            showSuppliers()                                                                                                                                         #Shows suppliers available
            while True:
                supplier_id = input('Type the id of the supplier: ')                                                                                                #Asks for the id of supplier who produce new product
                supplier_id = checkForSupplier(supplier_id)
                if supplier_id == 0:
                    continue
                else:
                    break                                                                                                                                           #if not integer asks again
            while True:
                new_product_quantity = input('Type the quantity of the product: ')                                                                                  #Asks for quantity of new product
                new_product_quantity = checkForDigitMoreZero(new_product_quantity)
                if new_product_quantity == 0:
                    continue
                else:
                    break
            while True:
                new_product_price = input('Type the price of the product: ')                                                                                        #Ask for price of new product
                new_product_price = checkForDigitMoreZero(new_product_price)
                if new_product_price == 0:
                    continue
                else:
                    addNewProduct(new_product_name, new_product_description, supplier_id, new_product_quantity, new_product_price)                                  #Adds new product with provided details
                    break
            showProducts()                                                                                                                                          #Shows updated list of products with new product
        
        elif choose_action == '5' or choose_action.lower().replace(' ', '') == 'update' or choose_action.lower().replace(' ', '') == 'updateproduct':               #Starts update product if 5
            while True:
                showProducts()                                                                                                                                      #Shows products available
                product_list = getProductsDetails()                                                                                                                 #Gets product list
                product_id = input('Type the id of the product you want to update: ')                                                                               #Asks for user to choose id of product to edit
                if product_id.isdigit():                                                                                                                            #Checks if it is int
                    product_id = int(product_id)                                                                                                                    #Converts to int if int
                else:
                    print('Not an id! Try again...')                                                                                                                #Asks again for id
                    continue
                delete_product_choice = 0                                                                                                                           #Variable for delete choice
                for product_item in product_list:                                                                                                                   #Goes through every product
                    if product_item['id'] == product_id:                                                                                                            #Checks if product exists
                        while True: 
                            delete_product_choice = input('Do you want to delete this product (y/n): ')                                                             #Asks to choose delete or not
                            if delete_product_choice == '1' or delete_product_choice.lower() == 'y':                                                                #If y then delete
                                deleteProduct(product_id)
                                showProducts()                                                                                                                      #Show new products with deleted product
                                break
                            elif delete_product_choice == '0' or delete_product_choice.lower() == 'n':                                                              #If n then goes to edit settings
                                break
                            else:
                                print('I dont understand! Type y or n...')                                                                                          #Asks again if not y or n
                        if delete_product_choice == 'n' or delete_product_choice == 0:
                            product_name = input('Type the new NAME of the product (or leave empty if no changes): ')                                               #Asks for new name of product
                            product_description = input('Type the new brief DESCRIPTION of the product (or leave empty if no changes): ')                           #Asks for new description of product
                            while True:
                                product_quantity = input('Type the new QUANTITY of the product (or leave empty if no changes): ')                                   #Asks for new quantity of product
                                if product_quantity == "":                                                                                                          #Check if quantity is empty then ok
                                    break   
                                product_quantity = checkForDigitMoreZero(product_quantity)
                                if product_quantity == 0:
                                    continue
                                else:
                                    break
                            while True:
                                product_price = input('Type the new PRICE of the product (or leave empty if no changes): ')                                         #Asks for new price of product
                                if product_price == "":                                                                                                             #Check if price is empty then ok
                                    break
                                product_price = checkForDigitMoreZero(product_price)
                                if product_price == 0:
                                    continue
                                else:
                                    break                                                                                                                           #if acceptable then ok

                            product_name = None if product_name == '' else product_name                                                                             #Convert to None if variables are empty
                            product_description = None if product_description == '' else product_description
                            product_price = None if product_price == '' else product_price
                            product_quantity = None if product_quantity == '' else product_quantity

                            print(product_description)
                            updateProduct(product_id, product_name, product_description, product_quantity, product_price)                                           #Update the product details
                            showProducts()                                                                                                                          #View products with updated product
                            break
                        break
                else:
                    print('No such product! Try again...')                                                                                                          #Asks again for exisiting product
                    continue
                break

        elif choose_action == '6' or choose_action.lower().replace(' ', '') == 'newsupplier' or choose_action.lower().replace(' ', '') == 'ns':                     #If 6 then add new supplier
            new_supplier_name = input('Type the name of the supplier: ')                                                                                            #Asks for supplier name
            while True:
                new_supplier_contact = input('Type the contact of the supplier (including + sign): ')                                                               #Asks for supplier contact number
                if 10 <= len(new_supplier_contact) <= 15 and new_supplier_contact[0] == '+' and new_supplier_contact[1::].isdigit():                                #Checks if contact looks real
                    addNewSupplier(new_supplier_name, new_supplier_contact)                                                                                         #Adds new supplier
                    break
                else:
                    print('Phone number is incorrect or in the incorrect form. Try other number...')                                                                #Asks again for contact number
            showSuppliers()
        
        elif choose_action == '7' or choose_action.lower().replace(' ', '') == 'placeorder' or choose_action.lower().replace(' ', '') == 'po':                      #If 7 then place new order
            while True: 
                showProducts()                                                                                                                                      #show products have
                product_list = getProductsDetails()                                                                                                                 #get lists of products
                product_id = input('Type the id of the product you want to add into order: ')                                                                       #getting id user wants to order
                if product_id.isdigit():                                                                                                                            #check if id is number
                    product_id = int(product_id)                                                                                                                    #convert to int if it is number
                else:                                                                   
                    print('Not an id! Try again...')                                                                                                                #if not then print error
                    continue                                                                                                                                        #continue asking the id
                product_quantity_real = 0                                                                                                                           #new variable
                for product_item in product_list:                                                                                                                   #going through the list of products
                    if product_item['id'] == product_id:                                                                                                            #check if the id exists
                        product_quantity_real = int(product_item['quantity'])                                                                                       #assign the variable with the quantity of requested items available
                        price_of_product = product_item['price']                
                        while True:                                                                             
                            quantity = input('Type the quantity of the product you want to order: ')                                                                #getting quantity use wants to order
                            if quantity.isdigit():                                                                                                                  #check if user typed number
                                quantity = int(quantity)                                                                                                            #make int if number
                                if product_quantity_real >= quantity:                                                                                               #check if the quantity user wants is sufficient to what have in storage
                                    updateProduct(product_id, new_quantity=product_quantity_real - quantity)                                                        #updates the amount of products in the storage
                                    break                                                                                                                           #finish and move to placing order if everythin good
                                else:                                                                                                                               
                                    print('Not enough in storage! Try different amount...')                                                                         #print error if not sufficent amount
                            else:                                                                   
                                print('Not an number! Try again...')                                                                                                #print error if quantity is not a number
                        addNewOrderById(product_id, quantity, price_of_product*quantity)                                                                            #add new order if everything good
                        break                                                                                                                                       #finish with this action
                else:                                                                   
                    print('No such product! Try again...')                                                                                                          #print error if no product with requested id
                    continue
                break

        elif choose_action == '8' or choose_action.lower().replace(' ', '') == 'suppliersales' or choose_action.lower().replace(' ', '') == 'ss':                     #If 8 then make report of supplier orders
            showSuppliers()                                                                                                                                         #Show suppliers available
            while True:
                supplier_id = input('Type the id of the supplier: ')                                                                                                #Asks for id of supplier
                supplier_id = checkForSupplier(supplier_id)
                if supplier_id == 0:
                    continue
                else:
                    break
            getReportSupplierSales(supplier_id)

        elif choose_action == '9' or choose_action.lower().replace(' ', '') == 'lowstock' or choose_action.lower().replace(' ', '') == 'ls':                        #If 9 then say low stock items
            product_list = getProductsDetails()                                                                                                                     #Gets product list
            low_stock_list = []                                                                                                                                     #Variable for products which are low in stock
            for product_item in product_list:                                                                                                                       #Goes through every product
                if product_item['quantity'] < 10:                                                                                                                   #Check if quantity of products is less than 10
                    low_stock_list.append(product_item['name'])                                                                                                     #Add low stock items to variable
            if len(low_stock_list) > 1:                                                                                                                             #Check if several products are low on stock
                for low_stock_item in low_stock_list:                                                                                                              
                    print(f'{low_stock_item}', end=' ')
                print('are low in stock')
            elif len(low_stock_list) == 1:                                                                                                                          #Check if only one product is low on stock
                print(f'{low_stock_list[0]} is low on stock!')
            else:                                                                                                                                                   #Check if no products are low in stock
                print('There is enough items in storage!')
        
        elif choose_action == '10' or choose_action.lower().replace(' ', '') == 'supplyproducts' or choose_action.lower().replace(' ', '') == 'sp':                 #Shows all products that belongs to requested supplier
            showSuppliers()
            while True:
                supplier_id = input('Type the id of the supplier: ')                                                                                                #Asks for id of supplier
                supplier_id = checkForSupplier(supplier_id)
                if supplier_id == 0:
                    continue
                else:
                    break
            getReportSupplyProducts(supplier_id)

        elif choose_action == '0':                                                                                                                                  #If 0 then close program
            print('Goodbye!')
            break
        
        else:                                                                                                                                                       #Asks user to choose action again
            print('Sorry I dont understand your choice, try nunbers...')
    else:
        print('The program is missing some of the text files! Please add them in order to start the program. Thanks...')
        break