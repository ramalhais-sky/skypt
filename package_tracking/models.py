from django.db import models

# Create your models here.
class Package(models.Model):
    image_text = models.CharField(max_length=200)
    recipient_text = models.CharField(max_length=200)
    received_by_text = models.CharField(max_length=200)
    reception_date = models.DateTimeField('date registered')
# https://stackoverflow.com/questions/3419997/creating-a-dynamic-choice-field
# https://stackoverflow.com/questions/4784775/ldap-query-in-python
