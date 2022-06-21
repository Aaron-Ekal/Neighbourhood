# Generated by Django 2.2.24 on 2021-12-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0007_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='hood',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='administrator',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
