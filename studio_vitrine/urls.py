from django.contrib import admin
from django.urls import path
from .views import contact, index, about, rebook, requin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index' ),
    path('contact/', contact, name="contact"),
    path('about/', about, name="contact"),
    path('work/', about, name="contact"),
    path('work/rebook', rebook, name="contact"),
    path('work/requin', requin, name="contact"),
    path('work/moto_helmet', requin, name="contact"),
]
