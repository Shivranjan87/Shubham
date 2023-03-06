# Generated by Django 4.1.7 on 2023-03-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=30)),
                ('t_mname', models.CharField(max_length=30)),
                ('t_lname', models.CharField(max_length=30)),
                ('t_age', models.IntegerField()),
                ('t_add', models.CharField(max_length=40)),
                ('t_qual', models.CharField(max_length=10)),
                ('t_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=40)),
            ],
        ),
    ]
