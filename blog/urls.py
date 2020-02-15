from django.conf.urls import url
from .views import post_list, post_description, create_post, edit_post

app_name='blog'

urlpatterns = [
    # Post list route.
    url(r'^blog-list/$', post_list, name='blog_list_view'),
    # Create new post route.
    url(r'^create-post/$', create_post, name='create_post'),
    # Edit post based on the primary key of each blog post.
    url(r'^edit-post/(?P<pk>\d+)/$', edit_post, name='edit_post'),
    # Routes to the detailed view of a post based on the unique slug.
    url(r'^(?P<slug>[-\w]+)/$', post_description, name='blog_desc_view'),
]