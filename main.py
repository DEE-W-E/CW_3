import os.path

from config import ROOT_DIR
from src.utils import open_json_file, filter_operations, sort_operations, format_date, \
    mask_operation_info

PATH_OPERATIONS = os.path.join(ROOT_DIR, 'operations.json')

data = open_json_file(PATH_OPERATIONS)
operations = filter_operations(data)
operations = sort_operations(operations)[:5]

for i in operations:
    print(f'{format_date(i)} {i['description']}\n'
          f'{mask_operation_info(i)}\n'
          f'{i["operationAmount"]['amount']} {i["operationAmount"]["currency"]['name']}\n')
