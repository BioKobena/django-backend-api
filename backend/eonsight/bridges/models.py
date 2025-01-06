from django.contrib.gis.db import models

class Bridge(models.Model):
    bridge_id = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    location = models.PointField() 

    class Meta:
        db_table = 'bridges'