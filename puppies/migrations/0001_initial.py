# Generated by Django 2.1.7 on 2021-04-23 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('home', models.IntegerField(default=1)),
                ('time_open', models.CharField(max_length=15)),
                ('time_close', models.CharField(max_length=15)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puppies.City')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puppies.City')),
            ],
        ),
        migrations.AddField(
            model_name='shops',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puppies.Street'),
        ),
        migrations.AlterUniqueTogether(
            name='shops',
            unique_together={('name', 'city', 'street')},
        ),
    ]
