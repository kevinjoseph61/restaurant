# Generated by Django 2.1.5 on 2020-06-09 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0005_remove_reservation_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Starters'), (2, 'Main Course'), (3, 'Desserts')], default=1)),
                ('description', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Added to cart'), (2, 'Order Recieved'), (3, 'Preparing'), (4, 'Delivered')], default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserve.MenuItem')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(1, 'Confirmed! Please inform manager on arrival'), (2, 'Manager will ensure that you are in the restaurant. Please wait'), (3, 'Manager has confirmed. Start Ordering now!'), (4, 'Food ordering and preparation in progress'), (5, 'Bill Paid and Reservation Over')], default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserve.Reservation'),
        ),
    ]
