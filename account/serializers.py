


from rest_framework import serializers
from models import MessageBoard, Reply, MessageType, User





class MessageBoardSerializer(serializers.ModelSerializer):

    # reply = serializers.PrimaryKeyRelatedField(queryset=Reply.objects.all())
    reply = serializers.ReadOnlyField(source='reply.content')

    class Meta:
        model = MessageBoard
        fields = ('id', 'content', 'contact', 'username', 'reply')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'qq', 'nickname')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

