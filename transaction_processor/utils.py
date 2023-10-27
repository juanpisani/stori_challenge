from datetime import date, datetime
from typing import Tuple, List, Dict

from transaction_processor.enums import TransactionTypes
from transaction_processor.models import Transaction


def convert_to_date(date_str: str) -> date:
    today = date.today()
    year = today.year

    # Create a datetime object with the current year and the given month and day
    date_obj = date(year, int(date_str.split("/")[0]), int(date_str.split("/")[1]))

    return date_obj


def convert_to_transaction_type_and_amount(amount_str: str) -> Tuple[TransactionTypes, float]:
    transaction_type = TransactionTypes.DEBIT_TRANSACTION if amount_str[
                                                                 0] == "-" else TransactionTypes.CREDIT_TRANSACTION
    remaining_string = float(amount_str[1:])
    return transaction_type, remaining_string


def get_monthly_count_transactions(transaction_list: List[Transaction]) -> Dict[str, int]:
    """Return dict of month names and amount of transactions"""
    result = {}
    for transaction in transaction_list:
        month_name = transaction.date.strftime("%B")
        if month_name in result:
            result[month_name] += 1
        else:
            result[month_name] = 1
    # return only months with transactions in it
    return {x: y for x, y in result.items() if y != 0}


def get_total_balance_and_average_results(debit_transactions: List[Transaction],
                                          credit_transactions: List[Transaction]) -> Tuple[float, float, float]:
    """Return total balance, average_credit_amount and average_debit_amount"""
    credit_balance = 0
    debit_balance = 0
    credit_count = 0
    debit_count = 0
    for transaction in credit_transactions:
        credit_balance += transaction.amount
        credit_count += 1
    for transaction in debit_transactions:
        debit_balance -= transaction.amount
        debit_count += 1
    total_balance = credit_balance + debit_balance
    average_credit_amount = credit_balance / credit_count if credit_count > 0 else 0
    average_debit_amount = debit_balance / debit_count if debit_count > 0 else 0
    return round(total_balance, 2), round(average_credit_amount, 2), round(average_debit_amount, 2)


def handle_csv_transaction(transaction_list):
    """Process transaction list and return html with results"""
    debit_transactions = list(filter(lambda x: x.transaction_type == TransactionTypes.DEBIT_TRANSACTION.value,
                                     transaction_list))
    credit_transactions = list(
        filter(lambda x: x.transaction_type == TransactionTypes.CREDIT_TRANSACTION.value, transaction_list))
    monthly_transactions = get_monthly_count_transactions(transaction_list)
    total_balance, average_credit_amount, average_debit_amount = get_total_balance_and_average_results(
        debit_transactions, credit_transactions)
    return f"Total balance is: {total_balance} <br>" \
           f"Transactions per month: {monthly_transactions} <br>" \
           f"Average debit amount: {average_debit_amount} <br>" \
           f"Average credit amount {average_credit_amount}"

