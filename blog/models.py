from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_url = models.URLField(blank=True)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(allow_unicode=True, db_index=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    comment_count = models.PositiveIntegerField(default=0)
    tag_set = models.models.ManyToManyField('Tag', blank=True)
    is_publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Item(models.Mdel):
    name = models.CharField(max_length=1000)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_publiish = models.BooleanField(default=False, verbose_name='공개여부')

    def __str__(self):
        return f'<{self.pk}> {self.name}'