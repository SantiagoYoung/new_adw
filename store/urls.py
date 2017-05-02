from django.conf.urls import url
from store import views
urlpatterns = [
    url(r'store_apply', views.store_apply),
    url(r'collect_store', views.collect_store),
    url(r'collect', views.collect),

]

