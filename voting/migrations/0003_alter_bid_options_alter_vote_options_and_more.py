# Generated by Django 5.0.3 on 2024-04-09 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0002_votinground_bids_applied_alter_voting_total_count_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bid",
            options={
                "ordering": ["voting", "member_id", "round_number"],
                "verbose_name": "Fern-Gebot",
                "verbose_name_plural": "Fern-Gebote",
            },
        ),
        migrations.AlterModelOptions(
            name="vote",
            options={
                "ordering": ["member_id"],
                "verbose_name": "Stimme",
                "verbose_name_plural": "Stimmen",
            },
        ),
        migrations.AlterModelOptions(
            name="voting",
            options={
                "ordering": ["-datetime"],
                "verbose_name": "Bieterrunde",
                "verbose_name_plural": "Bieterrunden",
            },
        ),
        migrations.AlterModelOptions(
            name="votinground",
            options={
                "ordering": ["voting", "round_number"],
                "verbose_name": "Abstimmungsrunde",
                "verbose_name_plural": "Abstimmungsrunden",
            },
        ),
        migrations.AlterField(
            model_name="voting",
            name="total_count",
            field=models.PositiveIntegerField(
                help_text="Anzahl der Mitglieder insgesamt.",
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Mitgliederanzahl",
            ),
        ),
        migrations.AlterField(
            model_name="voting",
            name="voter_count",
            field=models.PositiveIntegerField(
                help_text="Anzahl der Teilnehmer vor Ort (inkl. im Voraus abgegebener Gebote).",
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Teilnehmeranzahl",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="bid",
            unique_together={("voting", "member_id", "round_number")},
        ),
    ]