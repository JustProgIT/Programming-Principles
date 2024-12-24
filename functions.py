import json
from datetime import datetime

def programIsReady():
    supply_order_list = getReportSupplOrdersDetails()
    product_list = getProductsDetails()
    supplier_list = getSupplierDetails()
    order_list = getOrderDetails()
    if supply_order_list and product_list and supplier_list and order_list:
        return 1
    else:
        return 0

def getReportSupplOrdersDetails():                                                              #Function getting details of the generated report
    try:
        with open('reports/supply_orders.txt', 'r') as file:
            data = file.read().replace("'", '"')
        supply_orders = json.loads(data)
        return supply_orders
    except FileNotFoundError:
        print('File supply_orders.txt doesnt exists...')
        return None
    
def viewReportSupplyOrders():                                                                   #Views the details of the generated report
    supply_orders_list = getReportSupplOrdersDetails()
    product_list = getProductsDetails()
    if supply_orders_list and product_list:
        for supply_order in supply_orders_list:
            for product_item in product_list:
                if product_item['id'] == supply_order['product_id']:
                    print(f'''
                    ID: {supply_order['id']}
                        Name: {product_item['name']}
                        Quantity: {supply_order['quantity']}
                        Cost: {supply_order['cost']}
                        Date: {supply_order['date']}
                        ''')

def getProductsDetails():                                                                       #Get Product list
    try:
        with open('products.txt', 'r') as file:
            products_list = json.loads(file.read())
        return products_list
    except FileNotFoundError:
        print('File products.txt doesnt exists...')
        return None

def showProducts():                                                                             #Views Product list
    product_list = getProductsDetails()
    if product_list:
        for product_item in product_list:
            print(f'''
            ID: {product_item['id']}
                Name: {product_item['name']}
                Quantity: {product_item['quantity']}
                Price: {product_item['price']}
                ''')

def getSupplierDetails():                                                                       #Get Supplier list
    try:
        with open('suppliers.txt', 'r') as file:
            supplier_list = json.loads(file.read())
        return supplier_list
    except FileNotFoundError:
        print('File suppliers.txt doesnt exists...')
        return None

def showSuppliers():                                                                            #View Supplier list
    supplier_list = getSupplierDetails()
    if supplier_list:
        for supplier_item in supplier_list:
            print(f'''
            ID: {supplier_item['id']}
                Name: {supplier_item['name']}
                Contact: {supplier_item['contact']}
                ''')

def getOrderDetails():                                                                          #Get Order list
    try:
        with open('orders.txt', 'r') as file:
            order_list = json.loads(file.read())
        return order_list
    except FileNotFoundError:
        print('File orders.txt doesnt exists...')
        return None
    
def showOrders():                                                                               #View order list
    order_list = getOrderDetails()
    products_list = getProductsDetails()
    if order_list and products_list:
        for order_item in order_list:
            product_name = None
            for product_items in products_list:
                if product_items['id'] == order_item['product_id']:
                    product_name = product_items['name']
                    break
            print(f'''
            ID: {order_item['id']}
                Name: {product_name}
                Quantity: {order_item['quantity']}
                Cost: {order_item['cost']}
                Date: {order_item['date']}
                ''')

def addNewProduct(name, description, supplier_id, quantity, price):                             #Adds new product
    products_list = getProductsDetails()
    if products_list:
        product_id = products_list[-1]['id'] + 1 if products_list else 1
        products_list.append({
                'id': product_id, 
                'name': name, 
                'description': description,
                'supplier_id' : int(supplier_id),
                'quantity' : int(quantity),
                'price': int(price)
            })        
        
        with open('products.txt', 'w') as file:
            file.write(json.dumps(products_list))        
        return products_list

def addNewSupplier(name, contact):                                                              #Adds new supplier
    supplier_list = getSupplierDetails()
    if supplier_list:
        supplier_id = supplier_list[-1]['id'] + 1 if supplier_list else 1
        supplier_list.append({
                'id': supplier_id, 
                'name': name, 
                'contact' : contact
            })        
            
        with open('suppliers.txt', 'w') as file:
            file.write(json.dumps(supplier_list, indent=4))        
        return supplier_list

def deleteProduct(id):                                                                          #Deletes product
    products_list = getProductsDetails()
    if products_list:
        for product_item in products_list:
            if product_item['id'] == id:
                products_list.remove(product_item)  # Remove the product from the list
                print(f"Product with id: {id} has been deleted.")
                break
        else:
            print(f"Product with id: {id} not found.")
            return products_list
        with open('products.txt', 'w') as file:
            file.write(json.dumps(products_list, indent=4))  # Save the updated list back to the file
        return products_list

def updateProduct(id, name=None, new_description=None, new_quantity=None, new_price=None):      #Updates product details
    products_list = getProductsDetails()
    if products_list:
        for product_item in products_list:
            if product_item['id'] == id:
                if name:
                    product_item['name'] = name
                if product_item:
                    product_item['description'] = new_description
                if new_quantity or new_quantity == 0:
                    product_item['quantity'] = int(new_quantity)
                if new_price is not None:
                    product_item['price'] = int(new_price)
                break
        else:
            print(f"Product with name: {name} not found.")
            return products_list
        with open('products.txt', 'w') as file:
            file.write(json.dumps(products_list, indent=4))
        
        return products_list

def addNewOrderById(product_id, quantity, total_cost):                                              #Adds new order by id
    order_list = getOrderDetails()
    if order_list:
        order_id = order_list[-1]['id'] + 1 if order_list else 1

        order_list.append({
                'id': order_id, 
                'product_id': product_id, 
                'quantity' : quantity,
                'cost' : total_cost,
                'date' : datetime.now().ctime()
            })    
            
        with open('orders.txt', 'w') as file:
            file.write(json.dumps(order_list, indent=4))
            
        return order_list

def addNewOrder(product_name, quantity):                                                            #Adds new order by name(old version/not used anymore)
    order_list = getOrderDetails()
    if order_list:
        order_id = order_list[-1]['id'] + 1 if order_list else 1

        product_list = getProductsDetails()

        product_id = None
        for product_item in product_list:
            if product_item['name'] == product_name:
                product_id = product_item['id']
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

def checkForSupplier(supplierID):
    supplier_list = getSupplierDetails()
    if supplier_list:
        if supplierID.isdigit():                                                                                                                           #Check if is int
            supplierID = int(supplierID)                                                                                                                  #Convert to int
            for supplier in supplier_list:                                                                                                                  #Goes through each supplier
                if supplier['id'] == supplierID:                                                                                                           #Checks if supplier exists
                    break
            else:
                print('No supplier with such id! Try again...')                                                                                             #Asks again if no suppliers with given id
                return 0
            return supplierID
        else:
            print('It should be an integer! Try again...')                                                                                                  #Asks for id of supplier
            return 0

def checkForDigitMoreZero(value):
    if value == '':
        return 'ok'
    if value.isdigit():
        value = int(value)
        if value > 0:
            return value
        print('Not acceptable number! Try again...')  
        return 0
    print('This is not a number! Try again...')  
    return 0

# def generateReportSupplyOrder():
#     product_list = getProductsDetails()
#     supplier_list = getSupplierDetails()
#     showSuppliers()
#     while True:
#         supplier_id = input('Type the id of the supplier: ')
#         if supplier_id.isdigit():
#             supplier_id = int(supplier_id)
#             for supplier in supplier_list:
#                 if supplier['id'] == supplier_id:
#                     break
#             else:
#                 print('No supplier with such id! Try again...')
#                 continue
#             break
#         else:
#             print('It should be an integer! Try again...')