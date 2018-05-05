from django.db import models

class DataSet(models.Model):
    class Meta:
        db_table = 'd2qc_datasets'
    id = models.AutoField(primary_key=True)
    expocode = models.CharField(max_length=255)
    is_reference = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class DataType(models.Model):
    class Meta:
        db_table = 'd2qc_datatypes'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class DataPoint(models.Model):
    class Meta:
        db_table = 'd2qc_datapoints'
    id = models.AutoField(primary_key=True)
    data_set = models.ForeignKey('DataSet', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    depth = models.DecimalField(max_digits=8, decimal_places=3)
    unix_time_millis = models.BigIntegerField()
    station_number = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class DataValue(models.Model):
    class Meta:
        db_table = 'd2qc_datavalues'
    id = models.AutoField(primary_key=True)
    data_point = models.ForeignKey('DataPoint', on_delete=models.CASCADE)
    data_type = models.ForeignKey('DataType', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=19, decimal_places=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
