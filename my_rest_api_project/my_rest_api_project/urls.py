from django.contrib import admin
from django.urls import path, include
from items.views import home_view  # Import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls')),  # Includes the items app's URLs
    path('', home_view, name='home'),  # Handles the root URL
]
