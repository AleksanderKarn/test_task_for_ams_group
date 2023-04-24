import csv


def file_writer(row, percent):
    """
    Функция для записи данных в  CSV файл
    :param row: строка данных из таблицы
    :param percent: процент
    """
    with open('modified_file.csv', 'a', newline='') as f_object:
        writer_object = csv.writer(f_object, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        row.append(f"{percent}%")
        writer_object.writerow(row)


def calculate_percent(row):
    """
    Функция для расчета процента того что
    цена валюты продолжит расти
    :param row: строка таблицы
    :return: расчитанный процент
    """
    count = 0
    for i in range(len(row)):
        if row[i] and i != 0 and row[0].split(',')[-1] < row[i].split(',')[-1]:
            count += 1
    percent = count * 10
    return percent


def create_modified_file(object):
    """
    Функция для создания файла данных с дополнительным полем процентов
    :param object: обьект данных считанного офайла
    """
    for row in object:
        if row:
            percent = calculate_percent(row)
            file_writer(row, percent)


def file_reader(file):
    """
    Функция читает файл с данными и отдает их в
     функцию для создания модифицированного файла
    :param file: файл данных
    """
    with open(file, encoding='utf-8') as r_file:
        reader = csv.reader(r_file, delimiter=";")
        create_modified_file(reader)


file = "file_for_task.csv"

if __name__ == '__main__':
    file_reader(file)
