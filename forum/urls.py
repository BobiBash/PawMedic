from django.urls import path

from forum.views import ForumPostsListView, ForumCreatePostView, \
    ForumUpdatePostView, ForumPostDetailView, ForumPostDeleteView,\
    ForumCreateCommentView, ForumUpdateCommentView, ForumDeleteCommentView, \
    TagListView,TagCreateView, TagUpdateView,\
    TagDeleteView, TagDetailView

urlpatterns = [
    path('', ForumPostsListView.as_view(), name='forum-posts-list'),
    path('create-post', ForumCreatePostView.as_view(), name='forum-post-create'),
    path('edit-post/<int:pk>', ForumUpdatePostView.as_view(), name='forum-edit-post'),
    path('post-details/<int:pk>', ForumPostDetailView.as_view(), name='forum-post-details'),
    path('post-delete/<int:pk>', ForumPostDeleteView.as_view(), name='forum-delete-post'),
    path('post-create-comment/<int:pk>', ForumCreateCommentView.as_view(), name='forum-create-comment'),
    path('post-update-comment/<int:pk>', ForumUpdateCommentView.as_view(), name='forum-update-comment'),
    path('post-delete-comment/<int:pk>', ForumDeleteCommentView.as_view(), name='forum-delete-comment'),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    path("tags/<int:pk>/edit/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]