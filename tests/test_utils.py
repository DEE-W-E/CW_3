import os.path

from config import ROOT_DIR
from src.utils import open_json_file, filter_operations, sort_operations, mask_operation_info, format_date

TEST_PATH_OPERATIONS = os.path.join(ROOT_DIR, 'tests', 'test_data.json')


def test_open_json_file(list_with_dict):
    # assert type(open_json_file("test_data.json")) == dict
    assert open_json_file(TEST_PATH_OPERATIONS) == list_with_dict


def test_filter_operations(list_with_dict):
    assert filter_operations(list_with_dict)[0] == {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }


def test_sort_operations(list_with_dict):
    assert sort_operations(list_with_dict)[0] == {
        "id": 207126257,
        "state": "EXECUTED",
        "date": "2019-07-15T11:47:40.496961",
        "operationAmount": {
            "amount": "92688.46",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 35737585785074382265"
    }


def test_mask_operation_info_btb():
    operation = {'from': 'SomeBank XXXXXX4098761234', 'to': 'AnotherBank XXXXXX7776545678'}
    assert mask_operation_info(operation) == 'SomeBank XXXX XX** **** 1234 -> AnotherBank XXXX XX** **** 5678'


def test_mask_operation_info_tb():
    operation = {'to': 'AnotherBank XXXXXX7776545678'}
    assert mask_operation_info(operation) == 'Отправитель не указан -> AnotherBank XXXX XX** **** 5678'


def test_mask_operation_info_btc():
    operation = {'from': 'SomeBank XXXXXX4098761234', 'to': 'Счет XX5678'}
    assert mask_operation_info(operation) == 'SomeBank XXXX XX** **** 1234 -> Счет **5678'


def test_mask_operation_info_ctc():
    operation = {'from': 'Счет XX1234', 'to': 'Счет XX5678'}
    assert mask_operation_info(operation) == "Счет **1234 -> Счет **5678"


def test_format_date():
    operation = {'date': '2019-04-04T23:20:05.206878'}
    assert format_date(operation) == "04.04.2019"
