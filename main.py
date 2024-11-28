import json
from datetime import datetime

def getProductsDetails():
    with open('products.txt', 'r') as file:
        products_list = json.loads(file.read())
    return products_list

def getSupplierDetails():
    with open('suppliers.txt', 'r') as file:
        supplier_list = json.loads(file.read())
    return supplier_list

def getOrderDetails():
    with open('orders.txt', 'r') as file:
        order_list = json.loads(file.read())
    return order_list

def addNewProduct(products_list, name, description, price):        
    product_id = products_list[-1]['id'] + 1 if products_list else 1
    products_list.append({
            'id': product_id, 
            'name': name, 
            'description': description, 
            'price': price
        })        
    
    with open('products.txt', 'w') as file:
        file.write(json.dumps(products_list))        
    return products_list

def addNewSupplier(supplier_list, name, contact):
    supplier_id = supplier_list[-1]['id'] + 1 if supplier_list else 1
    supplier_list.append({
            'id': supplier_id, 
            'name': name, 
            'contact' : contact
        })        
        
    with open('suppliers.txt', 'w') as file:
        file.write(json.dumps(supplier_list))        
    return supplier_list

def updateProduct(products_list, name, description=None, price=None):
    for product in products_list:
        if product['name'] == name:
            # product['name'] = name
            if description:
                product['description'] = description
            if price is not None:
                product['price'] = price
            break
    else:
        print(f"Product with name: {name} not found.")
        return products_list
    
    with open('products.txt', 'w') as file:
        file.write(json.dumps(products_list, indent=4))
    
    return products_list

def addNewOrder(order_list, product_name, quantity):
    order_id = order_list[-1]['id'] + 1 if order_list else 1

    with open('products.txt', 'r') as file:
        products_list = json.load(file)

    product_id = None
    for product in products_list:
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


products_list = getProductsDetails()
supplier_list = getSupplierDetails()
order_list = getOrderDetails()

# print(supplier_list, type(supplier_list))
# order_list = getOrderDetails()

# products_list = addNewProduct(products_list, 'potato', 'Australian potato', 3)
# products_list = updateProduct(products_list, name='eggs', description='casual eggs', price=11)

# supplier_list = addNewSupplier(supplier_list, 'Angela', '+6000')

# order_list = addNewOrder(order_list, 'eggs', 200)