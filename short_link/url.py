from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.create_short_link, name='createshortlink'),
    re_path(r'(?P<short_url_id>\w{6})$', views.redirect_original, name='redirectoriginal'),
    path('short_link/', views.short_link, name='shortlink'),
]
