# Generated by Django 5.0 on 2024-01-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_remove_seat_train'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seat',
            options={'ordering': ['seat_number']},
        ),
        migrations.AlterField(
            model_name='train',
            name='train_id',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]