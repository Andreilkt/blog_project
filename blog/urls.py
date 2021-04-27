# blog/urls.py
#from django.urls import path

#from .views import BlogListView

#urlpatterns = [
   # path('', BlogListView.as_view(), name='home'),
#]

# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView  # новое изменение

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),  # новое изменение
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detaill'),  # новое изменение
    path('', BlogListView.as_view(), name='home'),
]