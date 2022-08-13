from django.db import models

# Create your models here.


class Quote(models.Model):
    quote_author = models.CharField(max_length=10)
    quote_body = models.TextField()
    context = models.CharField(max_length=10)
    source = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.quote_author}"
    