from django.db import models
from django.utils.text import slugify

class Subject(models.Model):
    subject_name = models.CharField(max_length=255,unique=True)
    slug         = models.SlugField(max_length=200,unique=True)
    subject_image = models.ImageField(upload_to='subject_images/',null=True)
      
    def __str__(self):
        return self.subject_name
      
class Topic(models.Model):
    subject_name= models.ForeignKey(Subject, on_delete=models.CASCADE) 
    topic_name = models.CharField(max_length=255,unique=True)
    slug         = models.SlugField(max_length=200,unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.topic_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.topic_name

class SubTopic(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sub_topic_name = models.CharField(max_length=255,unique=True)
    slug         = models.SlugField(max_length=200,unique=True)
    
    def __str__(self):
        return self.sub_topic_name

class Approver(models.Model):
    approver_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.approver_name

class Question(models.Model):
    sub_topic_name = models.ForeignKey(SubTopic, on_delete=models.CASCADE)
    question = models.TextField()
    options = models.TextField()
    opt_values = models.TextField()
    correct_options = models.TextField(max_length=255)
    selective_cnt = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    explanation = models.TextField()
    reference = models.TextField()
    source = models.TextField()
    approver_name = models.ForeignKey(Approver, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    visibility_flag = models.BooleanField(default=True)

    def __str__(self):
        return self.question

