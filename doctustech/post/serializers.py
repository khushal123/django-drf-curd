from rest_framework import serializers
from doctustech.post.models import Like, Post, Comment



class PostSerializer(serializers.ModelSerializer):
    post_media = serializers.CharField(required=False)
    class Meta:
        model = Post
        fields = ["post_by", "post_content", "post_media", "id"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["post_id", "liked_by"]

        def create(self, validated_data):
            try:
                like = Like.objects.filter(liked_by=validated_data['liked_by'], post_id=validated_data['post_id']).get()
                return like
            except Like.DoesNotExist:
                print("does not exists")
                return Like.objects.create(liked_by=validated_data['liked_by'], post_id=validated_data['post_id'])


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post_id", "comment_by", "content"]