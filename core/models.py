from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=128)
    image_src = models.CharField(max_length=128)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class SpecializationPage(models.Model):
    title = models.CharField(max_length=128)
    likes = models.PositiveIntegerField(default=0)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title


class SharePage(models.Model):
    title = models.CharField(max_length=128)
    courses = models.ManyToManyField(Course)
    is_for_specialization = models.BooleanField(null=True, blank=True)
    specialization = models.ForeignKey(SpecializationPage, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
