# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has on_delete set to the desired behavior
#   * Remove managed = False lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Appuser(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'appuser'


class Area(models.Model):
    areaid = models.AutoField(primary_key=True)
    areadescription = models.TextField(blank=True, null=True)
    principalinvestigatorid = models.ForeignKey('Person', models.DO_NOTHING, db_column='principalinvestigatorid', blank=True, null=True)
    labid = models.ForeignKey('Lab', models.DO_NOTHING, db_column='labid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'area'


class Building(models.Model):
    buildingid = models.AutoField(primary_key=True)
    buildingname = models.CharField(max_length=255)
    buildingcampus = models.CharField(max_length=255, blank=True, null=True)
    buildingaddress = models.TextField(blank=True, null=True)
    buildingmanagerid = models.ForeignKey('Person', models.DO_NOTHING, db_column='buildingmanagerid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'building'


class College(models.Model):
    collegeid = models.AutoField(primary_key=True)
    collegename = models.CharField(max_length=255)
    collegedeanid = models.ForeignKey('Person', models.DO_NOTHING, db_column='collegedeanid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'college'


class Collegedepartment(models.Model):
    collegeid = models.OneToOneField(College, models.DO_NOTHING, db_column='collegeid', primary_key=True)  # The composite primary key (collegeid, departmentid) found, that is not supported. The first column is selected.
    departmentid = models.ForeignKey('Department', models.DO_NOTHING, db_column='departmentid')

    class Meta:
        managed = True
        db_table = 'collegedepartment'
        unique_together = (('collegeid', 'departmentid'),)


class Department(models.Model):
    departmentid = models.AutoField(primary_key=True)
    departmentname = models.CharField(max_length=255)
    departmentheadid = models.ForeignKey('Person', models.DO_NOTHING, db_column='departmentheadid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'department'


class Departmentbuilding(models.Model):
    departmentid = models.OneToOneField(Department, models.DO_NOTHING, db_column='departmentid', primary_key=True)  # The composite primary key (departmentid, buildingid) found, that is not supported. The first column is selected.
    buildingid = models.ForeignKey(Building, models.DO_NOTHING, db_column='buildingid')

    class Meta:
        managed = True
        db_table = 'departmentbuilding'
        unique_together = (('departmentid', 'buildingid'),)


class Focus(models.Model):
    focusid = models.AutoField(primary_key=True)
    focuscategory = models.CharField(max_length=255)
    lastcertified = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'focus'


class Hazard(models.Model):
    hazardid = models.AutoField(primary_key=True)
    hazardtype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hazard'


class Lab(models.Model):
    labid = models.AutoField(primary_key=True)
    labname = models.CharField(max_length=255)
    labdescription = models.TextField(blank=True, null=True)
    labphone = models.CharField(max_length=20, blank=True, null=True)
    labbuildingid = models.ForeignKey(Building, models.DO_NOTHING, db_column='labbuildingid', blank=True, null=True)
    labroomid = models.ForeignKey('Room', models.DO_NOTHING, db_column='labroomid', blank=True, null=True)
    labresearchfocusid = models.ForeignKey(Focus, models.DO_NOTHING, db_column='labresearchfocusid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lab'


class Labbiosafetyofficer(models.Model):
    labid = models.OneToOneField(Lab, models.DO_NOTHING, db_column='labid', primary_key=True)  # The composite primary key (labid, userid) found, that is not supported. The first column is selected.
    userid = models.ForeignKey(Appuser, models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = True
        db_table = 'labbiosafetyofficer'
        unique_together = (('labid', 'userid'),)


class Labfocushazard(models.Model):
    focusid = models.OneToOneField(Focus, models.DO_NOTHING, db_column='focusid', primary_key=True)  # The composite primary key (focusid, hazardid) found, that is not supported. The first column is selected.
    hazardid = models.ForeignKey(Hazard, models.DO_NOTHING, db_column='hazardid')

    class Meta:
        managed = True
        db_table = 'labfocushazard'
        unique_together = (('focusid', 'hazardid'),)


class Labsafetyofficer(models.Model):
    labid = models.OneToOneField(Lab, models.DO_NOTHING, db_column='labid', primary_key=True)  # The composite primary key (labid, userid) found, that is not supported. The first column is selected.
    userid = models.ForeignKey(Appuser, models.DO_NOTHING, db_column='userid')

    class Meta:
        managed = True
        db_table = 'labsafetyofficer'
        unique_together = (('labid', 'userid'),)


class Notification(models.Model):
    notificationid = models.AutoField(primary_key=True)
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='personid', blank=True, null=True)
    overdueid = models.ForeignKey('Overdue', models.DO_NOTHING, db_column='overdueid', blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    notificationdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notification'


class Overdue(models.Model):
    overdueid = models.AutoField(primary_key=True)
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='personid', blank=True, null=True)
    type = models.CharField(max_length=50)
    itemid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'overdue'


class Person(models.Model):
    personid = models.AutoField(primary_key=True)
    personfirstname = models.CharField(max_length=255)
    personlastname = models.CharField(max_length=255)
    personphone = models.CharField(max_length=20, blank=True, null=True)
    persontitle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'person'


class Personemail(models.Model):
    emailid = models.AutoField(primary_key=True)
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='personid', blank=True, null=True)
    email = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'personemail'


class Room(models.Model):
    roomid = models.AutoField(primary_key=True)
    roomnumber = models.CharField(max_length=50)
    buildingid = models.ForeignKey(Building, models.DO_NOTHING, db_column='buildingid', blank=True, null=True)
    departmentid = models.ForeignKey(Department, models.DO_NOTHING, db_column='departmentid', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'room'


class Userbuilding(models.Model):
    userid = models.OneToOneField(Appuser, models.DO_NOTHING, db_column='userid', primary_key=True)  # The composite primary key (userid, buildingid) found, that is not supported. The first column is selected.
    buildingid = models.ForeignKey(Building, models.DO_NOTHING, db_column='buildingid')

    class Meta:
        managed = True
        db_table = 'userbuilding'
        unique_together = (('userid', 'buildingid'),)