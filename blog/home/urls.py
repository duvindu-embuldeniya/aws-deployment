from django.urls import path
from .views import *

urlpatterns = [
    # path('', BlogListView.as_view(), name = 'home'),
    path('', home, name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),

    path('profile/<str:username>/', profile, name = 'profile'),
    path('profile/<str:username>/delete/', delete_acc, name = 'delete_acc'),

    path('blog/<int:pk>/', blogDetail, name = 'blog-detail'),
]