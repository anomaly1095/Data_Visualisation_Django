# Generated by Django 5.0.1 on 2024-01-14 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Countries_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pop1950', models.IntegerField(default=0)),
                ('pop1951', models.IntegerField(default=0)),
                ('pop1952', models.IntegerField(default=0)),
                ('pop1953', models.IntegerField(default=0)),
                ('pop1954', models.IntegerField(default=0)),
                ('pop1955', models.IntegerField(default=0)),
                ('pop1956', models.IntegerField(default=0)),
                ('pop1957', models.IntegerField(default=0)),
                ('pop1958', models.IntegerField(default=0)),
                ('pop1959', models.IntegerField(default=0)),
                ('pop1960', models.IntegerField(default=0)),
                ('pop1961', models.IntegerField(default=0)),
                ('pop1962', models.IntegerField(default=0)),
                ('pop1963', models.IntegerField(default=0)),
                ('pop1964', models.IntegerField(default=0)),
                ('pop1965', models.IntegerField(default=0)),
                ('pop1966', models.IntegerField(default=0)),
                ('pop1967', models.IntegerField(default=0)),
                ('pop1968', models.IntegerField(default=0)),
                ('pop1969', models.IntegerField(default=0)),
                ('pop1970', models.IntegerField(default=0)),
                ('pop1971', models.IntegerField(default=0)),
                ('pop1972', models.IntegerField(default=0)),
                ('pop1973', models.IntegerField(default=0)),
                ('pop1974', models.IntegerField(default=0)),
                ('pop1975', models.IntegerField(default=0)),
                ('pop1976', models.IntegerField(default=0)),
                ('pop1977', models.IntegerField(default=0)),
                ('pop1978', models.IntegerField(default=0)),
                ('pop1979', models.IntegerField(default=0)),
                ('pop1980', models.IntegerField(default=0)),
                ('pop1981', models.IntegerField(default=0)),
                ('pop1982', models.IntegerField(default=0)),
                ('pop1983', models.IntegerField(default=0)),
                ('pop1984', models.IntegerField(default=0)),
                ('pop1985', models.IntegerField(default=0)),
                ('pop1986', models.IntegerField(default=0)),
                ('pop1987', models.IntegerField(default=0)),
                ('pop1988', models.IntegerField(default=0)),
                ('pop1989', models.IntegerField(default=0)),
                ('pop1990', models.IntegerField(default=0)),
                ('pop1991', models.IntegerField(default=0)),
                ('pop1992', models.IntegerField(default=0)),
                ('pop1993', models.IntegerField(default=0)),
                ('pop1994', models.IntegerField(default=0)),
                ('pop1995', models.IntegerField(default=0)),
                ('pop1996', models.IntegerField(default=0)),
                ('pop1997', models.IntegerField(default=0)),
                ('pop1998', models.IntegerField(default=0)),
                ('pop1999', models.IntegerField(default=0)),
                ('pop2000', models.IntegerField(default=0)),
                ('pop2001', models.IntegerField(default=0)),
                ('pop2002', models.IntegerField(default=0)),
                ('pop2003', models.IntegerField(default=0)),
                ('pop2004', models.IntegerField(default=0)),
                ('pop2005', models.IntegerField(default=0)),
                ('pop2006', models.IntegerField(default=0)),
                ('pop2007', models.IntegerField(default=0)),
                ('pop2008', models.IntegerField(default=0)),
                ('pop2009', models.IntegerField(default=0)),
                ('pop2010', models.IntegerField(default=0)),
                ('pop2011', models.IntegerField(default=0)),
                ('pop2012', models.IntegerField(default=0)),
                ('pop2013', models.IntegerField(default=0)),
                ('pop2014', models.IntegerField(default=0)),
                ('pop2015', models.IntegerField(default=0)),
                ('pop2016', models.IntegerField(default=0)),
                ('pop2017', models.IntegerField(default=0)),
                ('pop2018', models.IntegerField(default=0)),
                ('pop2019', models.IntegerField(default=0)),
                ('pop2020', models.IntegerField(default=0)),
                ('pop2021', models.IntegerField(default=0)),
                ('pop2022', models.IntegerField(default=0)),
                ('pop2023', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='density',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='fertility_rate',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='land_area',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='median_age',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='net_change',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='net_migrants',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='population',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='population_urban',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='world_share',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='yearly_change',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='pop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Countries_App.population'),
        ),
    ]
