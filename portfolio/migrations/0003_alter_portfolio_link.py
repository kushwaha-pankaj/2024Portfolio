# Generated by Django 4.2.10 on 2024-11-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_portfolio_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
