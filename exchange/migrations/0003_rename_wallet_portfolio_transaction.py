# Generated by Django 4.0.5 on 2022-06-30 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0002_buysellhistory_trader'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wallet',
            new_name='Portfolio',
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('note', models.TextField(max_length=100)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.coin')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
