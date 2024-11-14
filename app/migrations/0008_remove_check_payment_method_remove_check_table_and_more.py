# Generated by Django 5.1.3 on 2024-11-14 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='check',
            name='table',
        ),
        migrations.RemoveField(
            model_name='check',
            name='user',
        ),
        migrations.RemoveField(
            model_name='report',
            name='check_reference',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='check_reference',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='report',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_role',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
        migrations.DeleteModel(
            name='Check',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]
