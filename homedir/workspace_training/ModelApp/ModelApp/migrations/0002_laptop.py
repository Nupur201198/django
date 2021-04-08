# Generated by Django 2.1.7 on 2020-07-01 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('stud', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ModelApp.Student')),
            ],
        ),
    ]