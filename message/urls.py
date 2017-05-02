from django.conf.urls import url, include
import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'system_information', views.SystemInformationViewSet)



urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'suggestion', views.suggestion ),
]