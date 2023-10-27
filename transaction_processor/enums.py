from enum import Enum


class TransactionTypes(str, Enum):
    DEBIT_TRANSACTION = 'DEBIT_TRANSACTION'
    CREDIT_TRANSACTION = 'CREDIT_TRANSACTION'

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)
