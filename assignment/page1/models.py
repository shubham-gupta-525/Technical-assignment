from django.db import models

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length = 100)
    ip_address = models.GenericIPAddressField()
    created = models.DateField()
    tag = models.CharField(max_length=100)
    provider = models.CharField(max_length= 100)

class UsageStats(models.Model):
    server = models.ForeignKey(Server, on_delete = models.CASCADE)
    cpu = models.FloatField()
    ram = models.FloatField()
    disk = models.FloatField()
    app = models.FloatField()

class Alerts(models.Model):
    LEVEL_CHOICES = [('critical', 'Critical'), ('medium', 'Medium',), ('low', 'Low') ]
    server = models.ForeignKey(Server,on_delete= models.CASCADE)
    level = models.CharField(choices=LEVEL_CHOICES, max_length = 100)
    message = models.TextField()

class NetworkTraffic(models.Model):
    server = models.ForeignKey(Server, on_delete = models.CASCADE)
    timestamp = models.DateTimeField()
    incoming = models.FloatField()
