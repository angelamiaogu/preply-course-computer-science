from django.db import models
from django.utils import timezone
# Create your models here
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True,default='')


    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title
    

class comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now )
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
