# Generated by Django 3.2 on 2024-07-04 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField()),
                ('transaction_type', models.CharField(choices=[('expense', '支出'), ('income', '収入'), ('no_change', '変動なし')], max_length=10)),
                ('purpose', models.CharField(max_length=100)),
                ('major_category', models.CharField(choices=[('variable', '変動費'), ('fixed', '固定費'), ('special', '特別費')], max_length=10)),
                ('purpose_description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.paymentmethod')),
            ],
        ),
    ]
