from django.db import models
import uuid
# Create your models here.

class CreatePdf(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pdf = models.CharField(max_length=400,default="")
    dept = models.CharField(max_length=50,default="")
    session = models.CharField(max_length=50,default="")
    course_title = models.CharField(max_length=200,default="")
    teacher = models.CharField(max_length=100,default="")
    contributor = models.CharField(max_length=50,default="")
    is_approved = models.BooleanField(default=False)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.course_title + " " + self.session + " " + self.teacher

