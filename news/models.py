from django.db import models

class Article(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    Paragraph_1 = models.TextField(null=True)
    Paragraph_2 = models.TextField(null=True)
    Paragraph_3 = models.TextField(null=True)
    status = models.IntegerField(choices=STATUS_CHOICES,default=1) 
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles_images/', null=True, blank=True)  # specify the directory relative to MEDIA_ROOT

    def __str__(self):
        return self.title
    
    

