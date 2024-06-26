from django.db import models
from django.conf import settings
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comment by {self.user.email} on {self.created_at}'
    