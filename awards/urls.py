from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^register',views.register, name='register'),
    url(r'^profile',views.profile, name='profile'),
    url(r'^feed',views.feed, name='feed'),
    url(r'^review/(\d+)', views.review, name = 'review'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)