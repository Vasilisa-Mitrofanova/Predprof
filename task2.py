import csv

def insertion_sort(arr):
    sorted_arr = []
    not_sorted_arr = arr.copy()
    sorted_arr.append(not_sorted_arr[0])
    not_sorted_arr.pop(0)

    for elem in not_sorted_arr:
        for i in range(len(sorted_arr)):
            if sorted_arr[i] < elem:
                sorted_arr.insert(i, elem)
                break
            sorted_arr.append(elem)
    return sorted_arr


# открытие файла и считывание данных
with open('products.csv', 'r', encoding='utf-8-sig') as file:
    first_line = True
    reader = csv.reader(file, delimiter=';')
    results = {}  # словарь, в котором хранится категория и список сумм выручки за все продукты в ней
    for category, product, date, price_per_unit, count in reader: