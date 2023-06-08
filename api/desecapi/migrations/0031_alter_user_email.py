# Generated by Django 4.1.9 on 2023-06-08 16:40

from django.contrib.postgres.operations import CreateCollation
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("desecapi", "0030_blockedsubnet_blockedsubnet_subnet_idx"),
    ]

    operations = [
        # Explanation: https://adamj.eu/tech/2023/02/23/migrate-django-postgresql-ci-fields-case-insensitive-collation/
        CreateCollation(
            "case_insensitive",
            provider="icu",
            locale="und-u-ks-level2",
            deterministic=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                db_collation="case_insensitive",
                max_length=254,
                unique=True,
                verbose_name="email address",
            ),
        ),
        migrations.RunSQL(
            sql='DROP EXTENSION IF EXISTS "citext"',
            reverse_sql='CREATE EXTENSION IF NOT EXISTS "citext"',
        ),
    ]
