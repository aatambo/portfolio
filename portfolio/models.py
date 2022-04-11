from django.core.validators import RegexValidator
from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    github_url = models.URLField(blank=True)
    project_url = models.URLField(blank=True)
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Quote(models.Model):

    quote = models.TextField()
    author = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.author


class Profile(models.Model):

    name = models.CharField(max_length=100)
    skills = models.TextField()
    image = models.ImageField()
    education = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format:'+999999999'. Up to 15 digits allowed.",
    )
    phone = models.CharField(validators=[phone_regex], max_length=17)
    github = models.URLField()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.name
