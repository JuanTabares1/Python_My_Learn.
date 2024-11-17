import json

file_path = 'archivosJSON/products.json'

new_product = {
    'name': 'Wireless Charger',
    'price': 20,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry': '2024-07-01'
}

#Agregar producto
with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_product)

with open(file_path, mode='w') as file:
    json.dump(products, file_path, indent=4)