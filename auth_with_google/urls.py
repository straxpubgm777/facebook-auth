from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include(('social_django.urls','auth_with_google'), namespace='social')), 
    path('', include(('acconunt.urls','auth_with_google'), namespace='acconunt')),
]
