from api.models import Post
from rest_framework import serializers

class PostListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()

    def create(self, validated_data):
        list = PostList(**validated_data)
        list.save()
        return list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    body = serializers.TextField()
    created_at = serializers.DateTimeField(read_only = True)
    like_count = serializers.IntegerField()
    created_by = serializes.ForeignKey()
    list = PostListSerializer(read_only = True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created_at', 'created_by', 'like_count', 'list',)
