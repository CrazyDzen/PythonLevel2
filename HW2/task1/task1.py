import chardet
import re
import os
import csv


def search_keys(text):
    patterns = [r'Изготовитель системы:\s*\S*', r'Код продукта:\s*\S*', r'Тип системы:\s*\S*']
    # result_name = ['Изготовитель системы', 'Код продукта', 'Тип системы', 'Название ОС']
    result = []
    for pattern in patterns:
        result.append(re.findall(pattern, text)[0].split()[-1])
    result.append(re.findall(r'Windows\s\S*', text)[0])
    return result
    # {result_name[i]: result[i] for i in range(4)}


def get_data():
    all_files = os.listdir(os.getcwd())
    file_names = [all_files[i] for i in range(len(all_files)) if 'info_' in all_files[i]]
    main_data = [['Изготовитель системы', 'Код продукта', 'Тип системы', 'Название ОС']]

    for el in file_names:
        with open(el, 'rb') as f:
            res = chardet.detect(f.read())['encoding']
        with open(el, 'r', encoding=res) as f:
            main_data.append(search_keys(f.read()))
    return main_data


def write_to_csv(path):
    data = get_data()
    with open(path, 'w', encoding='utf8') as f:
        writer = csv.writer(f, delimiter=',')
        for el in data:
            writer.writerow(el)


write_to_csv('data.csv')
