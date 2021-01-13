# Generated by Django 3.1.3 on 2021-01-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='newsletter_agreement',
            field=models.BooleanField(db_index=True, default=False, help_text='Une par semaine maximum', verbose_name='Recevoir des newsletter'),
        ),
    ]