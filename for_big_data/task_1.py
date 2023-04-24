CSV_DELIMITER = ';'
NAME_MOD_FILE = 'new_file_for_task.csv'

row_count = 0
file_count = 0

def calculate_percent(row):
    """
    Функция для расчета процента того что
    цена валюты продолжит расти
    :param row: строка таблицы
    :return: рассчитанный процент
    """
    count = 0
    for i in range(len(row)):
        if row[i] and i != 0 and row[0].split(',')[-1] < row[i].split(',')[-1]:
            count += 1
    percent = count * 10
    return percent


def processing_row(row):
    """Функция добавляет в строку значение процента"""
    percent = calculate_percent(row)
    row.append(f"{percent}%")
    return row


def get_row(file):
    """Получение одной строки информации из файла"""
    line = file.readline().rstrip()
    if not line:
        return
    return line.split(CSV_DELIMITER)



def set_row(file, row):
    global row_count, file_count

    file.write(CSV_DELIMITER.join(row) + '\n')
    if row_count > 8:
        split_name = NAME_MOD_FILE.split('.')
        file_count += 1
        new_name = f"{split_name[0]}{file_count}.{split_name[1]}"
        file.close()
        row_count = 0
        return open(new_name, 'w', newline='')

    row_count += 1
    return file


def run(file_source, file):
    """Функция запуска открывает одновременно файл на чтение и второй файл на запись и
    работает пока все данные не будут переработаны (пока не закончатся строки в файле)"""
    source = open(file_source, encoding='utf-8')
    data = open(file, 'w', newline='')
    while True:
        row = get_row(source)
        if not row:
            break

        new_row = processing_row(row)

        data = set_row(data, new_row)

    source.close()
    data.close()


if __name__ == "__main__":
    run('file_for_task.csv', NAME_MOD_FILE)
