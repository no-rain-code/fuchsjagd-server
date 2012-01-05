from django.db import models

class SenderGroup(models.Model):
    """contains some senders"""
    hash = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = u'Sender Gruppe'
        verbose_name_plural = u'Sender Gruppen'
    
    def __unicode__(self):
        return self.hash

class Sender(models.Model):
    """this is the physical sender in the original fuchsjagd game"""
    latitude = models.DecimalField(decimal_places=6, max_digits=8)
    longitude = models.DecimalField(decimal_places=6, max_digits=8)
    senderpower = models.FloatField(default=1)
    group = models.ForeignKey('SenderGroup', related_name='senders')
    
    class Meta:
        verbose_name = u'Sender'
        verbose_name_plural = u'Sender'
    
    def __unicode__(self):
        return u"%s, %s" % (self.latitude, self.longitude)

