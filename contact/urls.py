# from django.urls import path
#
# from blog.views import home_page, blog_single, blog_page
#
# urlpatterns = [
#     path('', home_page, name='home'),
#     path('blog/', blog_page, name='blog'),
#     path('article_detail/<int:pk>/', blog_single, name='article_detail')
# ]

from django.urls import path
from .views import get_in_touch

urlpatterns = [
    path('', get_in_touch, name='contact')
]
