from teacher.models import Teacher
from django.db import models
from ckeditor.fields import RichTextField

class File(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='techer_files', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    file = models.FileField(null=True, blank=True, upload_to='media/files/')
    is_public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
