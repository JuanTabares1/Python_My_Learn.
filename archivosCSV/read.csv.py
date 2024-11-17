import csv

#Leer archivo
""" with open('archivosCSV/products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row) """

#Mostrar la informacion por columnas
""" with open('archivosCSV/products.csv', mode='r') as file:
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

""" with open('archivosCSV/products.csv', mode='a', newline='') as file:
    file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product) """

#nueva colummna y crear una copia del archivo csv
file_path = 'archivosCSV/products.csv'
updated_file_path = 'archivosCSV/products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total value']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #Escribir el encabezado

        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)