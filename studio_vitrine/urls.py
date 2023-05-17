from django.contrib import admin
from django.urls import path
from .views import contact, index, about, rebook, requin, moto, bizarre_city, sphinx, booba_bts,uee, ziak

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index' ),
    path('contact/', contact, name="contact"),
    path('about/', about, name="contact"),
    path('work/', about, name="contact"),
    path('work/rebook', rebook, name="rebook"),
    path('work/requin', requin, name="requin"),
    path('work/moto_helmet', moto, name="moto"),
    path('work/sphinx', sphinx, name="moto"),
    path('work/bizarre_city', bizarre_city, name="moto"),
    path('work/booba_bts', booba_bts, name="moto"),
    path('work/uee', uee, name="moto"),
    path('work/ziak_bts', ziak, name="moto"),
]
