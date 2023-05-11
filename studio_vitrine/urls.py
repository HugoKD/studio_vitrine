from django.contrib import admin
from django.urls import path
from .views import contact, index, about, work

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index' ),
    path('contact/', contact, name="contact"),
    path('about/', about, name="contact"),
    path('work/', about, name="contact"),
]
