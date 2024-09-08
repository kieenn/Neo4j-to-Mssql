
from django.db import models


class BelongTo(models.Model):
    start = models.ForeignKey('Detail', models.DO_NOTHING, blank=True, null=True)
    end = models.ForeignKey('Bill', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BELONG_TO'


class Holds(models.Model):
    start = models.ForeignKey('Detail', models.DO_NOTHING, blank=True, null=True)
    end = models.ForeignKey('Menu', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HOLDS'


class Bill(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    order_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    total = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill'


class Detail(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    item_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    order_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    price = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail'


class Menu(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    category = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    price = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    product_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    name = models.TextField(db_column='Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'
    def __str__(self):
        return f'{self.name}, {self.id}, {self.price}, {self.category}, {self.product_id}, {self.id}'