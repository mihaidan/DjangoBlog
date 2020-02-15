from django.contrib import admin
from django.urls import path

from blog import views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Route to the URL's for the blog. Could have routed the URL's here,
    # but this allows for the blog portion to be ported into a different
    # project.
    url(r'^blog/', include('blog.urls', namespace='blog')),
]
