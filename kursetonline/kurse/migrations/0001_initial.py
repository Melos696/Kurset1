# Generated by Django 5.2.3 on 2025-06-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulli', models.CharField(max_length=100)),
                ('pershkrimi', models.TextField()),
                ('data_fillimit', models.DateField()),
                ('cmimi', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
