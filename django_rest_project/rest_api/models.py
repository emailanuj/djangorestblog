from django.db import models

# Create your models here.
class BlogList(models.Model):
    title=models.CharField(max_length=50,blank=False,unique=True)
    description=models.CharField(max_length=250,blank=False)
    date_created=models.DateTimeField(auto_now=True)
    blog_owner=models.ForeignKey('auth.User',related_name='bloglists',on_delete=models.CASCADE,default='1')

    def __str__(self):
        return "{}".format(self.title)
    