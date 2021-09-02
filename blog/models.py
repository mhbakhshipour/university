from teacher.models import Teacher
from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='techer_blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='media/blog_thumbnail/')
    description = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=False)
    content = RichTextField()
    created_at = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
