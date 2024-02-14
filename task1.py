import csv

# открытие файла и считывание данных
with open('products.csv', 'r', encoding='utf-8-sig') as file:
    first_line = True
    reader = csv.reader(file, delimiter=';')
    results = {}  # словарь, в котором хранится категория и список сумм выручки за все продукты в ней
    for category, product, date, price_per_unit, count in reader:
        # проверка, чтобы не записывать первую строку в список данных
        if price_per_unit == 'Price per unit':
            pass
        else:
            # добавить выручку к заданной категории
            try:
                results[category].append(float(price_per_unit)*float(count))
            # создать пару ключ - категория: значение - выручка, если заданная категория не найдена
            except:
                results[category] = [float(price_per_unit)*float(count)]

    # создание и запись в файл
    with open('new_products.csv', 'w', encoding='utf-8-sig') as new_file:
        writer = csv.writer(new_file, delimiter=';')
        # запись в файл первой строки с названиями столбцов
        writer.writerow(['Category', 'Total'])
        # для каждой категории считаем итоговую сумму и записываем
        for categ in results.keys():
            if categ == 'Закуски':
                print(sum(results[categ]))
            writer.writerow([categ, sum(results[categ])])
