from django.db import models
from ckeditor.fields import RichTextField

class Teacher(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    avatar = models.ImageField(null=True, blank=True, upload_to='media/teacher_avatar/')
    description = models.TextField(null=True, blank=True)
    content = RichTextField()
    
    def __str__(self) -> str:
        return self.full_name
