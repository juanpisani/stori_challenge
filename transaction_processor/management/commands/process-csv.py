import logging
from pathlib import Path

from django.core.mail import send_mail
from django.core.management import BaseCommand
import pandas

from transaction_processor.serializers import TransactionSerializer
from transaction_processor.utils import convert_to_date, convert_to_transaction_type_and_amount, handle_csv_transaction

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--csv-file', nargs='?', default="example.csv")
        parser.add_argument('--email-address', nargs='?', default="default@email.com")

    def handle(self, *args, **options):
        try:
            file = options['csv_file']
            email_address = options['email_address']
            df = pandas.read_csv(Path(file), dtype=str)

            transaction_list = []

            for i, row in df.iterrows():
                date = convert_to_date(row["Date"])
                transaction_type, amount = convert_to_transaction_type_and_amount(row["Transaction"])
                serializer_data = {
                    "transaction_id": row["Id"],
                    "transaction_type": transaction_type.value,
                    "date": date,
                    "amount": amount
                }
                transaction_serializer = TransactionSerializer(data=serializer_data)
                if transaction_serializer.is_valid():
                    transaction_list.append(transaction_serializer.save())
                else:
                    logger.error(f"Serializer error: {transaction_serializer.errors}")

            process_result = handle_csv_transaction(transaction_list)

            send_mail(
                subject="Stori Challenge Result",
                message=None,
                from_email="stori.challenge.result@mail.com",
                recipient_list=[email_address],
                fail_silently=False,
                html_message=process_result
            )
        except Exception as e:
            logger.error(f"Exception error: {str(e)}")
