from django.db import models


class Board(models.Model):
    board_code = models.AutoField(db_column='Board_Code', primary_key=True)  # Field name made lowercase.
    customer_code = models.ForeignKey('Customer', models.DO_NOTHING, db_column='Customer_Code', blank=True, null=True)  # Field name made lowercase.
    card_index = models.ForeignKey('Card', models.DO_NOTHING, db_column='Card_Index', blank=True, null=True)  # Field name made lowercase.
    board_star = models.FloatField(db_column='Board_Star', blank=True, null=True)  # Field name made lowercase.
    board_title = models.CharField(db_column='Board_Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    board_write = models.CharField(db_column='Board_Write', max_length=200, blank=True, null=True)  # Field name made lowercase.
    board_date = models.DateTimeField(db_column='Board_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'board'


class Card(models.Model):
    card_index = models.AutoField(db_column='Card_Index', primary_key=True)  # Field name made lowercase.
    card_code = models.CharField(db_column='Card_Code', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    card_co = models.CharField(db_column='Card_Co', max_length=20, blank=True, null=True)  # Field name made lowercase.
    card_name = models.CharField(db_column='Card_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    card_tag = models.CharField(db_column='Card_Tag', max_length=100, blank=True, null=True)  # Field name made lowercase.
    card_type = models.CharField(db_column='Card_Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    card_af = models.IntegerField(db_column='Card_AF', blank=True, null=True)  # Field name made lowercase.
    card_pm = models.IntegerField(db_column='Card_PM', blank=True, null=True)  # Field name made lowercase.
    card_img = models.CharField(db_column='Card_Img', max_length=50, blank=True, null=True)  # Field name made lowercase.
    card_benefit1 = models.CharField(db_column='Card_Benefit1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    card_benefit2 = models.CharField(db_column='Card_Benefit2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    card_benefit3 = models.CharField(db_column='Card_Benefit3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    card_detail = models.CharField(db_column='Card_Detail', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'card'


class Customer(models.Model):
    customer_code = models.AutoField(db_column='Customer_Code', primary_key=True)  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=20)  # Field name made lowercase.
    customer_id = models.CharField(db_column='Customer_ID', unique=True, max_length=20)  # Field name made lowercase.
    customer_pw = models.CharField(db_column='Customer_PW', max_length=20)  # Field name made lowercase.
    customer_birth = models.CharField(db_column='Customer_Birth', max_length=6)  # Field name made lowercase.
    customer_email = models.CharField(db_column='Customer_Email', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'

class Heart(models.Model):
    heart_index = models.AutoField(db_column='Heart_Index', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=150, blank=True, null=True)
    card_index = models.ForeignKey(Card, models.DO_NOTHING, db_column='Card_Index', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'heart'