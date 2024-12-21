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
            Cost: {order_items['cost']}
            Date: {order_items['date']}
            ''')

def addNewProduct(name, description, supplier_id, quantity, price): 
    products_list = getProductsDetails()
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

def deleteProduct(id):
    products_list = getProductsDetails()
    for product in products_list:
        if product['id'] == id:
            products_list.remove(product)  # Remove the product from the list
            print(f"Product with id: {id} has been deleted.")
            break
    else:
        print(f"Product with id: {id} not found.")
        return products_list
    with open('products.txt', 'w') as file:
        file.write(json.dumps(products_list, indent=4))  # Save the updated list back to the file
    return products_list

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

def addNewOrderById(product_id, quantity, total_cost):
    order_list = getOrderDetails()
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