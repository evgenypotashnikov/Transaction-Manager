import csv
import os

from datetime import datetime

from models.transaction import Transaction
from settings import BASE_DIR, DIR_NAME, FILE_NAME


class Stream:

    @staticmethod
    def path_dir():
        return os.path.join(BASE_DIR, DIR_NAME)

    @classmethod
    def path_file(cls):
        return os.path.join(cls.path_dir(), FILE_NAME)

    @classmethod
    def initialization(cls):
        if not os.path.isdir(cls.path_dir()):
            os.mkdir(cls.path_dir())
        with open(cls.path_file(), "a", newline='') as file:
            if os.path.getsize(cls.path_file()) == 0:
                csv.DictWriter(
                    file,
                    fieldnames=Transaction.fields.keys()
                ).writeheader()

    @classmethod
    def read(cls):
        with open(cls.path_file()) as file:
            return [line for line in csv.DictReader(file)]

    @classmethod
    def write(cls, transaction: Transaction) -> None:
        with open(cls.path_file(), 'a', newline='') as file:
            # csv.writer(file).writerow(list(transaction.__dict__.values()))
            csv.writer(file).writerow(
                [
                    getattr(transaction, fields)
                    for fields in Transaction.fields
                ]
            )



