# Generated by Django 3.2.2 on 2021-07-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0026_delete_traffic_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='traffic_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('interface_out_1', models.CharField(blank=True, max_length=50, null=True)),
                ('interface_out_2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Traffic Interface',
                'verbose_name_plural': 'Traffic Interface',
                'ordering': ('id',),
            },
        ),
    ]