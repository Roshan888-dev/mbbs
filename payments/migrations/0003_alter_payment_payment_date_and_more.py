# Generated by Django 5.1.4 on 2025-01-08 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Bank Transfer', 'Bank Transfer'), ('Cash', 'Cash')], max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='completed', max_length=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='users.user'),
        ),
    ]
