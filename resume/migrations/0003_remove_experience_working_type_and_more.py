# Generated by Django 4.2.10 on 2024-02-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0002_experience"),
    ]

    operations = [
        migrations.RemoveField(model_name="experience", name="working_type",),
        migrations.AlterField(
            model_name="experience",
            name="mode_of_work",
            field=models.CharField(
                choices=[
                    ("Freelancer", "Freelancer"),
                    ("Contract", "Contract"),
                    ("Internship", "Internship"),
                    ("Full-time", "Full-time"),
                    ("Part-time", "Part-time"),
                    ("Personal Project", "Personal Project"),
                ],
                max_length=50,
            ),
        ),
    ]
