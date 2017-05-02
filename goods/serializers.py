
from models import BigType, SmallType, Goods
from rest_framework import serializers



class BigTypeSerializer(serializers.HyperlinkedModelSerializer):

    # small = serializers.PrimaryKeyRelatedField(many=True, queryset=SmallType.objects.all())


    class Meta:
        model = BigType
        fields = ('id', 'name','english_name','picture1', 'picture2')


class SmallTypeSerializer(serializers.HyperlinkedModelSerializer):

    big_type = serializers.ReadOnlyField(source='big_type.name')
    goods = serializers.StringRelatedField(many=True)

    class Meta:
        model = SmallType
        fields = ('id', 'name', 'big_type', 'goods')


class GoodsSerializer(serializers.ModelSerializer):

    # small_type = serializers.PrimaryKeyRelatedField(source='small_type.name')

    class Meta:
        model = Goods
        # fileds = ('id', 'small_type', 'seller', 'collected_number', 'goods_stock',
        #           'show_type', 'provide_design', 'provide_produce','custom_size',
        #         'custom_pattern', 'custom_style', 'name', 'description',
        #           'origin_price', 'new_price', 'colors', 'picture')
        exclude = ('create_time', )


















