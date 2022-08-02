# Generated by Django 4.0.6 on 2022-07-22 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_team_supervisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.AlterField(
            model_name='team',
            name='user',
            field=models.ManyToManyField(related_name='team_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.team_category'),
        ),
        migrations.AddField(
            model_name='team',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='accounts.team_category'),
        ),
    ]