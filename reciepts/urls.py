
from django.contrib import admin
from django.urls import path,include
# from app.app import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
]
