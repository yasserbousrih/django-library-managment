# Generated by Django 4.2.7 on 2023-12-13 03:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='first name', max_length=200),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='last name', max_length=200),
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('maintenance', 'Maintenance'), ('booked', 'Booked'), ('available', 'Available'), ('reserved', 'Reserved')], default='maintenance', max_length=20)),
                ('due_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylibrary.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='mylibrary.genre'),
        ),
    ]
