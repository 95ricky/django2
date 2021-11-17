# Generated by Django 3.0.2 on 2021-07-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_code', models.AutoField(db_column='Board_Code', primary_key=True, serialize=False)),
                ('board_star', models.FloatField(blank=True, db_column='Board_Star', null=True)),
                ('board_title', models.CharField(blank=True, db_column='Board_Title', max_length=100, null=True)),
                ('board_write', models.CharField(blank=True, db_column='Board_Write', max_length=200, null=True)),
                ('board_date', models.DateTimeField(blank=True, db_column='Board_Date', null=True)),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_index', models.AutoField(db_column='Card_Index', primary_key=True, serialize=False)),
                ('card_code', models.CharField(blank=True, db_column='Card_Code', max_length=20, null=True, unique=True)),
                ('card_co', models.CharField(blank=True, db_column='Card_Co', max_length=20, null=True)),
                ('card_name', models.CharField(blank=True, db_column='Card_Name', max_length=20, null=True)),
                ('card_tag', models.CharField(blank=True, db_column='Card_Tag', max_length=100, null=True)),
                ('card_type', models.CharField(blank=True, db_column='Card_Type', max_length=10, null=True)),
                ('card_af', models.IntegerField(blank=True, db_column='Card_AF', null=True)),
                ('card_pm', models.IntegerField(blank=True, db_column='Card_PM', null=True)),
                ('card_img', models.CharField(blank=True, db_column='Card_Img', max_length=50, null=True)),
                ('card_benefit1', models.CharField(blank=True, db_column='Card_Benefit1', max_length=50, null=True)),
                ('card_benefit2', models.CharField(blank=True, db_column='Card_Benefit2', max_length=50, null=True)),
                ('card_benefit3', models.CharField(blank=True, db_column='Card_Benefit3', max_length=50, null=True)),
                ('card_detail', models.CharField(blank=True, db_column='Card_Detail', max_length=200, null=True)),
            ],
            options={
                'db_table': 'card',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_code', models.AutoField(db_column='Customer_Code', primary_key=True, serialize=False)),
                ('customer_name', models.CharField(db_column='Customer_Name', max_length=20)),
                ('customer_id', models.CharField(db_column='Customer_ID', max_length=20, unique=True)),
                ('customer_pw', models.CharField(db_column='Customer_PW', max_length=20)),
                ('customer_birth', models.CharField(db_column='Customer_Birth', max_length=6)),
                ('customer_email', models.CharField(db_column='Customer_Email', max_length=50, unique=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('heart_index', models.AutoField(db_column='Heart_Index', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'heart',
                'managed': False,
            },
        ),
    ]
