from django.urls import path
from .views import pos_list, post_detail

app_name = "blog"

urlpatterns = [
    path("", pos_list, name="post_list"),
    path("<int:id>/", post_detail, name="post_detail"),
]
