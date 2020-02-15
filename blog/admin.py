from django.contrib import admin
from .models import Post


# For development, needed to add some blog posts via
# the admin portal.
admin.site.register(Post)