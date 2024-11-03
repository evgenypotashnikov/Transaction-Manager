from datetime import datetime
from prettytable import PrettyTable

from models.stream import Stream
from models.transaction import Transaction


def create_new_transaction():
    date = datetime.now()
    while True:
        print('Доступные категории:')
        categories = {
            f'{index + 1}': category
            for index, category in enumerate(Transaction.categories)
        }
        for index, value in categories.items():
            print(f'{index}. {value}')
        num_category = input(f'Выберете категорию(1 - {len(categories)}): ')
        if num_category in categories:
            break
        print(f'Введено не коректное значение. Допустимое значение от 1 - {len(categories)}')
    category = categories[num_category]
    while True:
        amount = input(f'Введите ссумму: ')
        if amount.replace(".", "", 1).isdigit() and float(amount) > 0:
            break
        print(f'Введено не коректное значение. Допустимое значение только численного типа больше 0')
    description = input(f'Введите описание транзакции: ')
    Stream.write(Transaction(date, category, float(amount), description))
    return 'Транзакция создана'


def balance():
    return Transaction.show_balance()


def income():
    return Transaction.show_income()


def expense():
    return Transaction.show_expense()


def show_all_transaction():
    table = PrettyTable(['№'] + list(Transaction.fields.values()))
    for ind, transaction in enumerate(Transaction.transactions):
        table.add_row(
            (
                [ind + 1] + [
                    getattr(transaction, field, "")
                    for field in Transaction.fields
                ]
            )
        )
    return table


def search_transaction():
    while True:
        print('Доступные поля поиска:')
        fields = {
            f'{ind + 1}': field
            for ind, field in enumerate(Transaction.search_fields)
        }
        for ind, field in fields.items():
            print(f'{ind}. {field}')
        num_field = input(f'Выберете поле для поиска (1 - {len(fields)}): ')
        if num_field in fields:
            break
        print(f"Введено не коректное значение. Допустимое значение от 1 - {len(fields)}")
    while True:
        value = input(f'Введите значение: ')
        try:
            if fields[num_field] == 'date' and bool(datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')):
                value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
                break
        except ValueError:
            print(f'Значение поля {fields[num_field]} должно быть формы "%Y-%m-%d %H:%M:%S.%f"')

        try:
            if fields[num_field] == 'amount':
                if value.replace(".", "", 1).isdigit() and float(value) > 0:
                    value = float(value)
                    break
                raise ValueError(f'Значение поля {fields[num_field]} должно быть численного типа больше 0')
        except ValueError as e:
            print(e)

        try:
            if fields[num_field] == 'category':
                if value in Transaction.categories:
                    break
                raise ValueError(f'Значение поля {fields[num_field]} должно быть из {Transaction.categories}')
        except ValueError as e:
            print(e)

    table = PrettyTable(['№'] + list(Transaction.fields.values()))
    for ind, transaction in enumerate(Transaction.search(fields[num_field], value)):
        table.add_row([ind + 1] + [
            getattr(transaction, field, '')
            for field in Transaction.fields
        ])
    print(table)


menu = {
    '1': {
        'name': 'Создать транзакцию',
        'func': create_new_transaction
    },
    '2': {
        'name': 'Посмотреть баланс',
        'func': balance
    },
    '3': {
        'name': 'Посмотреть доход',
        'func': income
    },
    '4': {
        'name': 'Посмотреть расход',
        'func': expense
    },
    '5': {
        'name': 'Посмотреть все транзакции',
        'func': show_all_transaction
    },
    '6': {
        'name': 'Произвести поиск транзакции',
        'func': search_transaction
    },
}
Stream.initialization()
data = Stream.read()
Transaction.append(data)

while True:
    print('Меню')
    for key, value in menu.items():
        print(f'{key}. {value["name"]}')
    choice = input(f'Введите желаемое действие(1 - {len(menu)}): ')
    if choice not in menu:
        print(f'Введено некоректное значение. Допустимое значение от 1 - {len(menu)}')
        continue
    result = menu[choice]['func']()
    if result is not None:
        print(result)
