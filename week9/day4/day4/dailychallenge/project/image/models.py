from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


from django.db import models

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/%y")
    upload_date = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.caption
