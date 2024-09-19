from django.urls import path
from .views import blog_settings, set_preferences, get_preferences

urlpatterns = [
    path('settings/', blog_settings, name='blog_settings'),
    path('set-preferences/', set_preferences, name='set_preferences'),
    path('get-preferences/', get_preferences, name='get_preferences'),
]
#path используется для определения маршрутов (URL-путей) в Django.



