from django.db import models

# Create your models here.
class Teams(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    facebookLink = models.URLField(max_length=100)
    TwitterLink = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural='teams'
    
    def __str__(self) -> str:
        return self.firstName + " "+ self.lastName