from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', accounts_views.home, name='home'),
    path('', accounts_views.signup, name='signup'),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),  # Include Django's auth URLs
]
