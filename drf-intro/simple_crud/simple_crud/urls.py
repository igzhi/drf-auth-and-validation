from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from measurements import views


router = DefaultRouter()
router.register('', views.ProjectViewSet, views.MeasurementViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
