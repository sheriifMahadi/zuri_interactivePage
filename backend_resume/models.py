from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}\'s comment on {self.date.strftime("%b %d %Y, %I:%M %p")}'

class PersonalInfo(models.Model):
    """Model to hold my personal information"""
    summary = models.TextField()
    expertise = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name


        
class Contact(models.Model):
    """A model for social 
    media links and contact"""
    social_media = models.CharField(max_length=50)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.social_media

    class Meta:
        verbose_name_plural = 'contact'

class Tools(models.Model):
    """A model to hold the skills i have and 
    ones applied to existing projeccs"""
    tools = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tools
    class Meta:
        verbose_name_plural = 'tools'

class Languages(models.Model):
    """A model to hold the languages i have used"""
    language = models.CharField(max_length=100)
    
    def __str__(self):
        return self.language

    class Meta:
        verbose_name_plural = 'languages'


