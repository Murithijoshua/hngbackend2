
from django.contrib import admin
from django.urls import path, include
# these imports are for django rest framework
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'api',views.ReportviewSet)
admin.site.site_header = "IssueReporter Admin"
admin.site.site_title = "IssueReporter Admin Portal"
admin.site.index_title = "Welcome to IssueReporter Portal"
urlpatterns = [
    path('', views.get_data, name="form"),
    path('thanks/', views.thanks, name="home"), 
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
