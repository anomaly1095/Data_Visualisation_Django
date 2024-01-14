# Generated by Django 5.0.1 on 2024-01-13 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gdp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gdp1980', models.FloatField(default=0)),
                ('gdp1981', models.FloatField(default=0)),
                ('gdp1982', models.FloatField(default=0)),
                ('gdp1983', models.FloatField(default=0)),
                ('gdp1984', models.FloatField(default=0)),
                ('gdp1985', models.FloatField(default=0)),
                ('gdp1986', models.FloatField(default=0)),
                ('gdp1987', models.FloatField(default=0)),
                ('gdp1988', models.FloatField(default=0)),
                ('gdp1989', models.FloatField(default=0)),
                ('gdp1990', models.FloatField(default=0)),
                ('gdp1991', models.FloatField(default=0)),
                ('gdp1992', models.FloatField(default=0)),
                ('gdp1993', models.FloatField(default=0)),
                ('gdp1994', models.FloatField(default=0)),
                ('gdp1995', models.FloatField(default=0)),
                ('gdp1996', models.FloatField(default=0)),
                ('gdp1997', models.FloatField(default=0)),
                ('gdp1998', models.FloatField(default=0)),
                ('gdp1999', models.FloatField(default=0)),
                ('gdp2000', models.FloatField(default=0)),
                ('gdp2001', models.FloatField(default=0)),
                ('gdp2002', models.FloatField(default=0)),
                ('gdp2003', models.FloatField(default=0)),
                ('gdp2004', models.FloatField(default=0)),
                ('gdp2005', models.FloatField(default=0)),
                ('gdp2006', models.FloatField(default=0)),
                ('gdp2007', models.FloatField(default=0)),
                ('gdp2008', models.FloatField(default=0)),
                ('gdp2009', models.FloatField(default=0)),
                ('gdp2010', models.FloatField(default=0)),
                ('gdp2011', models.FloatField(default=0)),
                ('gdp2012', models.FloatField(default=0)),
                ('gdp2013', models.FloatField(default=0)),
                ('gdp2014', models.FloatField(default=0)),
                ('gdp2015', models.FloatField(default=0)),
                ('gdp2016', models.FloatField(default=0)),
                ('gdp2017', models.FloatField(default=0)),
                ('gdp2018', models.FloatField(default=0)),
                ('gdp2019', models.FloatField(default=0)),
                ('gdp2020', models.FloatField(default=0)),
                ('gdp2021', models.FloatField(default=0)),
                ('gdp2022', models.FloatField(default=0)),
                ('gdp2023', models.FloatField(default=0)),
                ('gdp2024', models.FloatField(default=0)),
                ('gdp2025', models.FloatField(default=0)),
                ('gdp2026', models.FloatField(default=0)),
                ('gdp2027', models.FloatField(default=0)),
                ('gdp2028', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Not Available', max_length=45)),
                ('gdp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Countries_App.gdp')),
            ],
        ),
    ]