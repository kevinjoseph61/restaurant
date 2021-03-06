# Generated by Django 2.1.5 on 2020-06-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0008_auto_20200609_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='feedback',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(1, 'Confirmed! Please inform manager on arrival'), (2, 'Manager will ensure that you are in the restaurant. Please wait'), (3, 'Manager has confirmed. Start Ordering now!'), (4, 'Food ordering and preparation in progress'), (5, 'Awaiting Bill Payment Confirmation'), (6, 'Bill Paid and Reservation Over')], default=1),
        ),
    ]
