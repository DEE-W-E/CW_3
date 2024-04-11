import json
import datetime as dt


def open_json_file(file_path):
    """Чтение json файла"""
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def filter_operations(operations_data):
    """Фильтрация json файла по статусу 'EXECUTED"""
    operations_list = []
    for operation in operations_data:
        if operation.get('state') == "EXECUTED":
            operations_list.append(operation)
    return operations_list


def sort_operations(operations_data: list[dict]) -> list[dict]:
    """Сортировка списка по дате"""
    sorted_list = sorted(operations_data, key=lambda x: x['date'], reverse=True)
    return sorted_list


def mask_operation_info(operation):
    """Преобразует информацию к ввиду : отправитель -> получатель
        Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
        Номер счета замаскирован и не отображается целиком в формате  **XXXX
        (видны только последние 4 цифры номера счета).
    """
    operation_from = operation.get('from')
    operation_to = operation.get('to')

    if operation_from:
        parts = operation_from.split(' ')
        numbers = parts[-1]
        if len(numbers) == 16:
            masked_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            operation_from = f"{" ".join(parts[:-1])} {masked_numbers}"
        else:
            operation_from = f'Счет **{numbers[-4:]}'

    if operation_to:
        parts = operation_to.split(' ')
        numbers = parts[-1]
        if len(numbers) == 16:
            masked_numbers = f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
            operation_to = f"{" ".join(parts[:-1])} {masked_numbers}"
        else:
            operation_to = f'Счет **{numbers[-4:]}'

    if operation_from is None:
        operation_from = "Отправитель не указан"

    return f"{operation_from} -> {operation_to}"


def format_date(operation):
    """Форматирует дату в необходимый формат"""
    date = operation['date']
    dt_time = dt.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return dt_time.strftime("%d.%m.%Y")





