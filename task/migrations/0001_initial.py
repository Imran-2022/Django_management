# Generated by Django 5.0.3 on 2024-03-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=50)),
                ('task_description', models.TextField()),
                ('task_assign_date', models.DateField()),
                ('task_is_complete', models.BooleanField(default=False)),
                ('task_category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]