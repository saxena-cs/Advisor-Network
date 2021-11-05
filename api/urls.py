from rest_framework.routers import DefaultRouter
from django.conf.urls import url,include
from django.urls import include
from django.conf.urls import url
from .views import AdvisorViewset

router = DefaultRouter()
router.register('advisor',AdvisorViewset,basename='advisor')
urlpatterns = [
    url('',include(router.urls))
]