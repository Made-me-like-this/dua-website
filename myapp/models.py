from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Dua(models.Model):
    title = models.CharField(max_length=200)
    arabic_text = models.TextField()
    transliteration = models.TextField()
    translation = models.TextField()
    reference = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='duas')
    benefit = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    answers = models.TextField(blank=True)

    def __str__(self):
        return self.title
