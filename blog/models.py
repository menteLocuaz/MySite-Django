from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# esta clase sirve para el mager y solo publica los Punlisead
class PublisheadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    # añadimo nuestro propio satus
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    # creamos un manger
    objects = models.Manager()
    published = PublisheadManager()

    # metemos los meta datos, lo organisamos en decenso y de abajo hacia arriba
    # indesamos para mejora en ceo y la busqueda
    class Meta:
        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        return self.title

    # la url canonical que se comunica con url absoluta
    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )
