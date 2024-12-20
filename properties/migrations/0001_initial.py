# Generated by Django 5.1.2 on 2024-10-14 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=200)),
                ("town", models.CharField(max_length=100)),
                ("house_number", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Owner",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Tenant",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Property",
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
                ("name", models.CharField(max_length=200)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("commercial", "commercial"),
                            ("residential", "residential"),
                            ("warehouse", "warehouse"),
                            ("apartment", "apartment"),
                        ],
                        max_length=100,
                    ),
                ),
                ("rooms", models.IntegerField(default=1)),
                ("available", models.BooleanField(default=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "address",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="properties.address",
                    ),
                ),
                (
                    "owner",
                    models.ManyToManyField(
                        related_name="properties", to="properties.owner"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RentalAgreement",
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
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("rent", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="properties.property",
                    ),
                ),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="properties.tenant",
                    ),
                ),
            ],
        ),
    ]
