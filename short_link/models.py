from django.db import models


class Urls(models.Model):
    short_url_id = models.SlugField(max_length=6,primary_key=True)
    long_url = models.URLField(max_length=2000)
    transition_date = models.DateTimeField(auto_now=True)
    transition_count = models.IntegerField(default=0)

    def __str__(self):
        return self.long_url
