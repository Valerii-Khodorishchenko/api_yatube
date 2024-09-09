from rest_framework import serializers

from posts.models import Comment, Group, Post


class AuthorRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class PostSerializer(serializers.ModelSerializer):
    author = AuthorRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
