import csv

#Leer archivo
""" with open('archivosCSV/products_updated.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row) """

#Mostrar la informacion por columnas
""" with open('archivosCSV/products_updated.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"El producto: {row['name']}, Precio: {row['price']}") """

#Crear un nuevo producto
new_product = {
    'name': 'Wireless Charger',
    'price': 20,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry': '2024-07-01'
}

with open('archivosCSV/products_updated.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)