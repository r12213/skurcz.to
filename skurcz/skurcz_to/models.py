from django.db import models


class ShortURL(models.Model):
    full_url = models.URLField('URL', unique=True)
    code = models.CharField(unique=True, max_length=10, primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_url

    class Meta:
        ordering = ['-create_date']
        unique_together = (('full_url', 'code'),)
