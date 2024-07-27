# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Env(models.Model):
    id = models.AutoField(primary_key=True)
    pin = models.TextField()
    remark = models.TextField(blank=True, null=True)
    wskey = models.TextField(blank=True, null=True)
    ckvalue = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    imgurl = models.TextField(blank=True, null=True)
    uuid = models.TextField(blank=True, null=True)
    expired = models.IntegerField()
    status = models.IntegerField()
    envt = models.IntegerField(db_column='Envt')  # Field name made lowercase.
    position = models.IntegerField()
    containerid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Env'


class Efmigrationshistory(models.Model):
    migrationid = models.TextField(db_column='MigrationId')  # Field name made lowercase.
    productversion = models.TextField(db_column='ProductVersion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


class Containers(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.IntegerField()
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    type = models.IntegerField()
    url = models.TextField(blank=True, null=True)
    wskeycount = models.IntegerField()
    ckcount = models.IntegerField()
    wpapptoken = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    clientid = models.TextField(blank=True, null=True)
    clientsecret = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'containers'
