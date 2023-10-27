# Generated by Django 4.2.6 on 2023-10-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("transaction_id", models.CharField(max_length=255)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[
                            ("DEBIT_TRANSACTION", "DEBIT_TRANSACTION"),
                            ("CREDIT_TRANSACTION", "CREDIT_TRANSACTION"),
                        ],
                        max_length=20,
                    ),
                ),
                ("date", models.DateField()),
                ("amount", models.FloatField()),
            ],
        ),
    ]