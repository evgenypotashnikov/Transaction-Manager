from datetime import datetime
from typing import Union


class Transaction:
    __categories = ['Доход', 'Расход']
    __transactions = []
    __search_fields = ['date', 'category', 'amount']
    __validations = [
        '_validate_date',
        '_validate_category',
        '_validate_amount',
        '_validate_description'
    ]
    __fields = {
        'date': 'Дата',
        'category': 'Категория',
        'amount': 'Сумма',
        'description': 'Описание'
    }

    def __init__(
            self,
            date: datetime,
            category: str,
            amount: Union[int, float],
            description: str
    ):
        self.__date = date
        self.__category = category
        self.__amount = amount
        self.__description = description
        self._run_validations()
        self.transactions.append(self)

    @classmethod
    @property
    def fields(cls):
        return cls.__fields

    @property
    def date(self):
        return self.__date

    @property
    def category(self):
        return self.__category

    @property
    def amount(self):
        return self.__amount

    @property
    def description(self):
        return self.__description

    @classmethod
    @property
    def transactions(cls):
        return cls.__transactions

    @classmethod
    def show_balance(cls):
        return cls.show_income() - cls.show_expense()

    @classmethod
    def show_income(cls):
        income = 0
        for transaction in cls.transactions:
            if transaction.__category == 'Доход':
                income += transaction.__amount
        return income

    @classmethod
    def show_expense(cls):
        expense = 0
        for transaction in cls.transactions:
            if transaction.__category == 'Расход':
                expense += transaction.__amount
        return expense

    @classmethod
    def search(cls, field, value):
        if field not in cls.search_fields:
            raise ValueError(f'Не корректные поле для поиска. Выберите из: {cls.search_fields}')
        result = []
        for transaction in cls.transactions:
            if getattr(transaction, f'_{cls.__name__}__{field}') == value:
                result.append(transaction)
        return result

    # метод принимает список с ссылками на транзакции из файла transaction.csv и записывает в статическое свойство __transactions
    @classmethod
    def append(cls, data: list) -> None:
        for transaction in data:
            cls(
                date=datetime.strptime(transaction['date'], '%Y-%m-%d %H:%M:%S.%f'),
                category=transaction['category'],
                amount=float(transaction['amount']),
                description=transaction['description'],
            )

    @classmethod
    @property
    def categories(cls):
        return cls.__categories

    @classmethod
    @property
    def search_fields(cls):
        return cls.__search_fields

    @classmethod
    @property
    def validations(cls):
        return cls.__validations

    def _run_validations(self):
        for validate in self.validations:
            getattr(self, validate)()

    def _validate_date(self):
        if not isinstance(self.__date, datetime):
            raise TypeError('Дата должна быть экземпляром datetime')

    def _validate_category(self):
        if self.__category not in self.categories:
            raise TypeError(f'Категория должна быть: {self.categories}')

    def _validate_amount(self):
        if not isinstance(self.__amount, (int, float)):
            raise TypeError('Сумма должна быть числовым значением')

    def _validate_description(self):
        if not isinstance(self.__description, str):
            raise TypeError('Описание должно быть строковым значением')
