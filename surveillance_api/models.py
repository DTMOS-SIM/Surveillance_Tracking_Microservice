from typing import List
from django.db import models


# Create your models here.
class Node(models.Model):
    name = models.CharField(max_length=255)
    x_position = models.IntegerField(null=False)
    y_position = models.IntegerField(null=False)
    partners = models.ManyToManyField('self', through='Partner',
                                      symmetrical=False,
                                      related_name='related_to')
    date_created = models.IntegerField(null=False)
    date_updated = models.IntegerField(null=False)


class Partner(models.Model):
    from_person = models.ForeignKey(Node, related_name='from_people', on_delete=models.CASCADE)
    to_person = models.ForeignKey(Node, related_name='to_people', on_delete=models.CASCADE)
    angle_start = models.IntegerField(null=False)
    angle_end = models.IntegerField(null=False)
    date_created = models.IntegerField(null=False)
    date_updated = models.IntegerField(null=False)


class Report(models.Model):
    name = models.CharField(max_length=255, null=False)
    timestamp = models.IntegerField(null=False)
    frame_count = models.IntegerField(null=False)
    model_id = models.IntegerField(null=False)

    class Meta:
        managed = False

