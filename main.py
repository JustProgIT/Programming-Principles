import json
from datetime import datetime

def getProductsDetails():
    try:
        with open('products.txt', 'r') as file:
            products_list = json.loads(file.read())
        return products_list
    except FileNotFoundError:
        print('File products.txt doesnt exists...')
        return None

def showProducts():
    product_list = getProductsDetails()
    for product_items in product_list:
        print(f'''
        ID: {product_items['id']}
            Name: {product_items['name']}
            Quantity: {product_items['quantity']}
            Price: {product_items['price']}
            ''')

def getSupplierDetails():
    try:
        with open('suppliers.txt', 'r') as file:
            supplier_list = json.loads(file.read())
        return supplier_list
    except FileNotFoundError:
        print('File suppliers.txt doesnt exists...')
        return None

def showSuppliers():
    supplier_list = getSupplierDetails()
    for supplier_items in supplier_list:
        print(f'''
        ID: {supplier_items['id']}
            Name: {supplier_items['name']}
            Contact: {supplier_items['contact']}
            ''')

def getOrderDetails():
    try:
        with open('orders.txt', 'r') as file:
            order_list = json.loads(file.read())
        return order_list
    except FileNotFoundError:
        print('File orders.txt doesnt exists...')
        return None
    
def showOrders():
    order_list = getOrderDetails()
    products_list = getProductsDetails()
    for order_items in order_list:
        product_name = None
        for product_items in products_list:
            if product_items['id'] == order_items['product_id']:
                product_name = product_items['name']
                break
        print(f'''
        ID: {order_items['id']}
            Name: {product_name}
            Quantity: {order_items['quantity']}
            Date: {order_items['date']}
            ''')

def addNewProduct(name, description, quantity, price): 
    products_list = getProductsDetails()
    product_id = products_list[-1]['id'] + 1 if products_list else 1
    products_list.append({
            'id': product_id, 
            'name': name, 
            'description': description,
            'quantity' : int(quantity),
            'price': int(price)
        })        
    
    with open('products.txt', 'w') as file:
        file.write(json.dumps(products_list))        
    return products_list

def addNewSupplier(name, contact):
    supplier_list = getSupplierDetails()
    supplier_id = supplier_list[-1]['id'] + 1 if supplier_list else 1
    supplier_list.append({
            'id': supplier_id, 
            'name': name, 
            'contact' : contact
        })        
        
    with open('suppliers.txt', 'w') as file:
        file.write(json.dumps(supplier_list))        
    return supplier_list

def updateProduct(id, name=None, description=None, quantity=None, price=None):
    products_list = getProductsDetails()
    for product in products_list:
        if product['id'] == id:
            if name:
                product['name'] = name
            if description:
                product['description'] = description
            if quantity:
                product['quantity'] = int(quantity)
            if price is not None:
                product['price'] = int(price)
            break
    else:
        print(f"Product with name: {name} not found.")
        return products_list
    
    with open('products.txt', 'w') as file:
        file.write(json.dumps(products_list, indent=4))
    
    return products_list

def addNewOrderById(product_id, quantity):
    order_list = getOrderDetails()
    order_id = order_list[-1]['id'] + 1 if order_list else 1

    order_list.append({
            'id': order_id, 
            'product_id': product_id, 
            'quantity' : quantity, 
            'date' : datetime.now().ctime()
        })    
        
    with open('orders.txt', 'w') as file:
        file.write(json.dumps(order_list, indent=4))
        
    return order_list

def addNewOrder(product_name, quantity):
    order_list = getOrderDetails()
    order_id = order_list[-1]['id'] + 1 if order_list else 1

    product_list = getProductsDetails()

    product_id = None
    for product in product_list:
        if product['name'] == product_name:
            product_id = product['id']
            break

    order_list.append({
            'id': order_id, 
            'product_id': product_id, 
            'quantity' : quantity, 
            'date' : datetime.now().ctime()
        })    
        
    with open('orders.txt', 'w') as file:
        file.write(json.dumps(order_list, indent=4))
        
    return order_list


# products_list = getProductsDetails()
# supplier_list = getSupplierDetails()
# order_list = getOrderDetails()

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
                          
    Type the number to perform required action: ''')
    
    if choose_action == '1' or choose_action.lower().replace(' ', '') == 'product' or choose_action.lower().replace(' ', '') == 'viewproduct':
        showProducts()
    elif choose_action == '2' or choose_action.lower().replace(' ', '') == 'supplier' or choose_action.lower().replace(' ', '') == 'viewsupplier':
        showSuppliers()
    elif choose_action == '3' or choose_action.lower().replace(' ', '') == 'order' or choose_action.lower().replace(' ', '') == 'vieworder':
        showOrders()
    elif choose_action == '4' or choose_action.lower().replace(' ', '') == 'newproduct' or choose_action.lower().replace(' ', '') == 'np':
        new_product_name = input('Type the name of the product: ')
        new_product_description = input('Type the brief description of the product: ')
        while True:
            new_product_quantity = input('Type the quantity of the product: ')

            if new_product_quantity.isdigit():
                break
            else:
                print('The quantity should be a number!')
        while True:
            new_product_price = input('Type the price of the product: ')

            if new_product_price.isdigit():
                addNewProduct(new_product_name, new_product_description, new_product_quantity, new_product_price)
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
            for product_items in product_list:
                if product_items['id'] == product_id:
                    product_name = input('Type the name of the product: ')
                    product_description = input('Type the brief description of the product: ')
                    product_quantity = input('Type the quantity of the product: ')
                    product_price = input('Type the price of the product: ')

                    product_name = None if product_name == '' else product_name
                    product_description = None if product_description == '' else product_description
                    product_price = None if product_price == '' else product_price
                    product_quantity = None if product_quantity == '' else product_quantity

                    updateProduct(product_id, product_name, product_description, product_quantity, product_price)
                    showProducts()
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
            showProducts()                                                                  #show products have
            product_list = getProductsDetails()                                             #get lists of products
            product_id = input('Type the id of the product you want to add into order: ')   #getting id user wants to order
            if product_id.isdigit():                                                        #check if id is number
                product_id = int(product_id)                                                #convert to int if it is number
            else:
                print('Not an id! Try again...')                                            #if not then print error
                continue                                                                    #continue asking the id
            product_quantity_real = 0                                                       #new variable
            for product_item in product_list:                                               #going through the list of products
                if product_item['id'] == product_id:                                        #check if the id exists
                    product_quantity_real = int(product_item['quantity'])                   #assign the variable with the quantity of requested items available
                    print('Real:', product_quantity_real)                                   #
                    while True:                                                             
                        quantity = input('Type the quantity of the product you want to order: ') #getting quantity use wants to order
                        if quantity.isdigit():                                              #check if user typed number
                            quantity = int(quantity)                                        #make int if number
                            if product_quantity_real >= quantity:                           #check if the quantity user wants is sufficient to what have in storage
                                updateProduct(product_id, quantity=product_quantity_real-quantity) #updates the amount of products in the storage
                                break                                                       #finish and move to placing order if everythin good
                            else:                                                           
                                print('Not enough in storage! Try different amount...')     #print error if not sufficent amount
                        else:
                            print('Not an number! Try again...')                            #print error if quantity is not a number
                    addNewOrderById(product_id, quantity)                                   #add new order if everything good
                    break                                                                   #finish with this action
            else:
                print('No such product! Try again...')                                      #print error if no product with requested id
                continue
            break
    elif choose_action == '0':
        print('Goodbye!')
        break
    else:
        print('Sorry I dont understand your choice, try nunbers...')