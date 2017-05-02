from django.conf.urls import url, include

from goods import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'big_type', views.BigTypeViewSet)
# router.register(r'upload_goods', views.EditGoodsViewSet)
# router.register(r'small_type', views.SmallTypeViewSet)



urlpatterns = [

    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^big_type', views.big_types),
    url(r'^small_type', views.get_small_types),
    url(r'^show_goods', views.get_small_type_goods),
    url(r'^show_picture', views.show_picture),
    url(r'^goods_detail', views.goods_detail),
    url(r'^upload_goods', views.UploadGoods.as_view()),

    url(r'^collect_goods', views.collect_goods),
    url(r'^collect', views.collect),


]