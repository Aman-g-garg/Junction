# Generated by Django 3.2 on 2022-11-14 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0031_auto_20221114_1757'),
        ('schedule', '0008_auto_20200322_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='session',
            field=models.ForeignKey(blank=True, limit_choices_to={'review_status': 2}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proposals.proposal'),
        ),
    ]
