# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории.

# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

import json
import os
import pickle
import csv


js_ = 'hw8.json'
csv_ = 'hw8.csv'
pickle_ = 'hw8.pickle'
dir_ = '/home/sasha/Documents/Developing/Python_WEB/Seminar_8/TestFolder1'


def directory_(json_file: str, csv_file: str, pickle_file, dir_path: str) -> None:
    my_dict = {}
    for path, dir_name, file_name in os.walk(dir_path):
        print(f'{path = }\n{dir_name = }\n{file_name = }\n')
        list_dir = os.listdir(path)
        for i in list_dir:
            if os.path.isdir(path + '/' + i):
                my_dict[i] = {'entity': 'dir'}
                size = 0
                for ele in os.scandir(path + '/' + i):
                    size += os.stat(ele).st_size
                my_dict[i]['size'] = str(size)
                my_dict[i]['parent'] = path.split('/')[-2]
            elif os.path.isfile(path + '/' + i):
                my_dict[i] = {'entity': 'file'}
                my_dict[i]['size'] = str(os.path.getsize(path + '/' + i))
                my_dict[i]['parent'] = path.split('/')[-1]

    with(
        open(json_file, 'w', encoding='utf-8') as j,
        open(csv_file, 'w', encoding='utf-8') as c,
        open(pickle_file, 'wb') as p,
    ):
        json.dump(my_dict, j, indent=2)
        pickle.dump(my_dict, p)
        csv_write = csv.writer(c, dialect='excel')
        list_ = [[level_, id_, name_] for level_, i_u in my_dict.items()
                 for id_, name_ in i_u.items()]
        csv_write.writerow(list_)


if __name__ == '__main__':
    directory_(js_, csv_, pickle_, dir_)
