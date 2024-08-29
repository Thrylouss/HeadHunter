# Generated by Django 4.2.13 on 2024-07-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeadHunterApp', '0003_alter_resume_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('IN_PROGRESS', 'In progress'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='NEW', max_length=100),
        ),
    ]
