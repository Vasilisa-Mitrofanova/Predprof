import csv

def promo(name, date):
    '''
    Функция генерирует промокод.

    параметр name: название продукта
    параметер date: дата поступления продукта

    Возвращает сгенерированный промокод.
    '''
    promo = name.upper()[:2] + date[:2] + name.upper()[-2:][::-1] + date[3:5][::-1]
    return promo

# открытие файла и считывание данных
with open('products.csv', 'r', encoding='utf-8-sig') as file:
    first_line = True
    reader = csv.reader(file, delimiter=';')
    # запись в новый файл данных сразу по мере их обработки
    with open('products_promo.csv', 'w', encoding='utf-8-sig') as new_file:
        writer = csv.writer(new_file, delimiter=';')
        # запись строки с названиями столбцов
        writer.writerow(['Category', 'product', 'Date', 'Price per unit', 'Count', 'Promocode'])
        # обработка и запись данных
        for category, product, date, price_per_unit, count in reader:
            if category != 'Category':
                writer.writerow([category, product, date, price_per_unit, count, promo(product, date)])