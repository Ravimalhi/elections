# Generated by Django 2.2.5 on 2019-09-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_adhar_casted'),
    ]

    operations = [
        migrations.CreateModel(
            name='voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voterId', models.CharField(max_length=15, null=True)),
                ('casted', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='adhar',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='modi',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='nota',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='rahul',
        ),
        migrations.AddField(
            model_name='vote',
            name='conservative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='green',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='liberals',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='ndp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='people',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='public',
            field=models.IntegerField(default=0),
        ),
    ]
