from django.urls import path
from . import views

#NB: WHEN WORKING WITH CLASS BASED VIEWS, WE ALWAYS ADD .as_view(), AS SEEN BELOW. IF WE ARE WORKING WITH FUNCTION
# BASED VIEWS, WE DO views.bla_bla_bla, AS SEEN IN THE add_comment_to_post

urlpatterns = [
    path("", views.PostListView.as_view(), name='post_list'),
    path("about/", views.AboutView.as_view(), name='about'),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name='post_detail'),
    path("post/new", views.CreatePostView.as_view(), name='post_new'),
    path("post/<int:pk>/edit", views.PostUpdateView.as_view(), name='post_edit'),
    path("post/<int:pk>/remove", views.PostDeleteView.as_view(), name='post_remove'),
    path("drafts", views.DraftListView.as_view(), name='post_draft_list'),
    path("post/<int:pk>/comment", views.add_comment_to_post, name='add_comment_to_post'),
    path("comment/<int:pk>/approve", views.comment_approve, name='comment_approve'),
    path("comment/<int:pk>/remove", views.comment_remove, name='comment_remove'),
    path("post/<int:pk>publish", views.post_publish, name='post_publish'),
]