from django.db import models
from django.template.defaultfilters import slugify


# Blog Post database model
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # Added the slug since I had some problems with using the title
    # as the string to query on.
    slug = models.SlugField(max_length=100, unique=True, default=slugify(title))

    # Automatically creates the slug based on the title of the post.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    # Ordering the blog posts by date such that the most recent one
    # shows up at the top.
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title