import csv

data = {} # создание словаря для упорядоченного хранения данных
# чтение файла и обработка данных
with open('products.csv', 'r', encoding='utf-8-sig') as file:
    first_line = True
    reader = csv.reader(file, delimiter=';')
    for category, product, date, price_per_unit, count in reader:
        # проверка, что первая линия не является названиями столбцов
        if price_per_unit == 'Price per unit':
            pass
        else:
            # добавление данных в data
            try:
                data[category][product] += float(count)
            except:
                try:
                    data[category][product] = float(count)
                except:
                    data[category] = {product: float(count)}

command = None
# бесконечный цикл, пока пользователь не введёт команду "молоко"
while True:
    command = input('Введите категорию: ')
    if command == 'молоко':
        break
    # ошибка возникнет только в случае, если товара нет в БД
    try:
        min_price = 10**10
        min_price_product = ''
        for product in data[command].keys():
            if data[command][product] < min_price:
                min_price_product = product
                min_price = data[command][product]
        print(f'В категории: {command} товар: {min_price_product} был куплен {min_price} раз')
    except:
        print('Такой категории не существует в нашей БД')