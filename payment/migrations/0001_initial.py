# Generated by Django 3.2.2 on 2021-05-25 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0003_alter_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mercadopago_id', models.IntegerField()),
                ('status', models.CharField(max_length=150)),
                ('installments', models.IntegerField(verbose_name='Parcelas')),
                ('status_detail', models.CharField(max_length=250)),
                ('payment_method', models.CharField(max_length=250)),
                ('payment_type', models.CharField(max_length=250)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
