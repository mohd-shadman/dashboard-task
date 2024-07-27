from django.db import models
from django.utils import timezone

class DataEntry(models.Model):
    end_year = models.CharField(max_length=10, blank=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=50, blank=True)
    topic = models.CharField(max_length=50)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=50, blank=True)
    start_year = models.CharField(max_length=10, blank=True)
    impact = models.CharField(max_length=10, blank=True)
    added = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=50, blank=True)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=50)
    title = models.TextField()
    likelihood = models.IntegerField()
