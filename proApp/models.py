# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Env(models.Model):
    id = models.AutoField(verbose_name="id",primary_key=True)
    pin = models.TextField(verbose_name="京东账户名(pin)")
    remark = models.TextField(verbose_name="备注",blank=True, null=True)
    wskey = models.TextField(verbose_name="京东扫码获取的wskey",blank=True, null=True)
    ckvalue = models.TextField(verbose_name="京东短信获取的mck",blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    imgurl = models.TextField(verbose_name="用户头像链接",blank=True, null=True)
    uuid = models.TextField(verbose_name="WxPusher消息推送平台的uuid",blank=True, null=True)
    expired = models.IntegerField()
    status = models.IntegerField(verbose_name="京东账户是否启用")
    envt = models.IntegerField(verbose_name="用户登陆方式",db_column='Envt')  # Field name made lowercase.
    position = models.IntegerField()
    containerid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Env'


class Efmigrationshistory(models.Model):
    migrationid = models.TextField(primary_key=True,db_column='MigrationId')  # Field name made lowercase.
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
