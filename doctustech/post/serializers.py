from rest_framework import serializers
from doctustech.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    post_media = serializers.CharField(required=False)
    class Meta:
        model = Post
        fields = ["post_by", "post_content", "post_media"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["post_id", "liked_by"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["post_id", "comment_by", "content"]