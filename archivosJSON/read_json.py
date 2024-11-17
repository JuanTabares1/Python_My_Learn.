import json

#Lectura del archivo
with open('archivosJSON/products.json', mode='r') as file:
    products = json.load(file)

#Mostrar el contenido
for product in products:
    #print(product)
    print(f"Producto: {product['name']}, Price: {product['price']}")

