# Generated by Django 5.1.3 on 2024-12-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0002_rename_percentag_result_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='id',
        ),
        migrations.AlterField(
            model_name='result',
            name='login_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
