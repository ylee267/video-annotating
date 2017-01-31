from django.db import models


class Annotation(models.Model):


    nickname = models.CharField(max_length=100)
    email = models.EmailField()
    video = models.CharField(max_length=100)
    time = models.FloatField()
    comment = models.TextField()
    comment_type = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s create a comment' % (self.nickname)
