from django.db import models

# Create your models here.

#models안에 Model 을 상속받기

class NewModel(models.Model):
    text = models.CharField(max_length=255, null=False)
