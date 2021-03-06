# Generated by Django 2.0 on 2017-12-16 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingdate', models.DateField(unique=True)),
                ('bookingstate', models.CharField(choices=[('TBC', 'TO BE CONFIRMED'), ('CON', 'CONFIRMED'), ('N/A', 'NOT AVAILABLE')], default='TBC', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='BookingReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('lastmodifieddate', models.DateTimeField(auto_now=True)),
                ('adultsnum', models.DecimalField(decimal_places=0, max_digits=1)),
                ('kidsnum', models.DecimalField(decimal_places=0, max_digits=1)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='bookingreference',
            name='customerdata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.CustomerData'),
        ),
        migrations.AddField(
            model_name='bookingcalendar',
            name='bookingreference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.BookingReference'),
        ),
    ]
