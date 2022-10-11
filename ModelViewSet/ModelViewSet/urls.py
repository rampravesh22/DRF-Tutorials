from django.contrib import admin
from django.urls import path,include
from core import views
from rest_framework.routers import DefaultRouter
# creating Router object
router = DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls))
]
