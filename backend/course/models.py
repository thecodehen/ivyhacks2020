from django.db import models
# How exactly do Django content types work?
# https://stackoverflow.com/questions/20895429/how-exactly-do-django-content-types-work
# https://simpleisbetterthancomplex.com/tutorial/2016/10/13/how-to-use-generic-relations.html
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Professor(models.Model):
    full_name = models.CharField()

    def __str__(self):
        return self.full_name

class Company(models.Model):
    full_name = models.CharField()

    def __str__(self):
        return self.full_name

class Image(models.Mode):
    image = models.ImageField()
    # caption = models.TextField(blank=True)

class Problem(models.Model):
    brief_problem_statement = models.CharField()
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
    )
    professor = models.ForeignKey(
        'Professor',
        on_delete=models.SET_NULL,
    )
    date_posted = models.DateTimeField()
    date_solved = models.DateTimeField()
    # course_content contains all the course content of a problem
    # the JSON is a list of basic elements that includes type and data
    # sample content: {[
    #     {"type": "text", "content": "Here is a piece of text"},
    #     {"type": "video", "url": "https://example.com/link_to_video"},
    #     {"type": "text", "content": "Here is another piece of text"},
    #     {"type": "image", "url": "https://example.com/link_to_image"}
    # ]}
    course_content = models.JSONField()
