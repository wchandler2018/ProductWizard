from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    url = models.TextField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    body = models.TextField(max_length=1000)
    wizard = models.ForeignKey(User, on_delete=models.CASCADE)

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")
    
    def summary(self):
        return self.body[:100]
    
    def __str__(self):
        return self.title
