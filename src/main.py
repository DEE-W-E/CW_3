from src import utils
from src.utils import open_json_file, filter_operations, sort_operations, format_date, \
    mask_operation_info

data = open_json_file('operations.json')
operations = filter_operations(data)
operations = sort_operations(operations)[:5]

print(operations )
for i in operations:
    print(f'{format_date(i)}\n'
          f'{mask_operation_info(i)}\n')

