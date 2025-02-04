from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    group_id = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    available = models.BooleanField(default=True, null=True)
    posted_at = models.DateTimeField(null=True, blank=True)
    post_url = models.URLField(null=True, blank=True)
    post_text = models.TextField(null=True)
    user_id = models.BigIntegerField(null=True, blank=True)
    username = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE, related_name='group', blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name='category', blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    user_url = models.URLField(null=True, max_length=5000)
    title = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username


class Image(models.Model):
    url = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.url
