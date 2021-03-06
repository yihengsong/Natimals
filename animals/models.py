from django.db import models

class Natimal(models.Model):
    country = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    scientific_name = models.CharField(max_length=255)
    model_pic1 = models.ImageField(upload_to = 'pic_folder/', blank=True, null=True)
    model_pic2 = models.ImageField(upload_to = 'pic_folder/', blank=True, null=True)
    status = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __unicode__(self):
        return '%s' % (self.name)
    def get_absolute_url(self):
       return "/country/%s/" % self.name_slug

