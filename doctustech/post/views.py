from rest_framework.views import APIView
from doctustech.post.models import Post, Like, Comment
from django.http import Http404
from doctustech.post.serializers import CommentSerializer, LikeSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from doctustech.user.models import User
# Create your views here.


class PostView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        user_id = request.user.id
        try:
            like = Like.objects.filter(liked_by=user_id, post_id=id).get()
            return Response({
                "message": "Already liked"
            }, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            post = Post.objects.get(id=id)
            user = User.objects.get(id=user_id)
            like = Like.objects.create(liked_by=user, post_id=post)
            print(like)
        return Response({
        }, status=status.HTTP_201_CREATED)


    def get(self, request, id):
        likes = Like.objects.filter(post_id=id).count()
        return Response({
            "total_likes": likes
        }, status=status.HTTP_200_OK)

class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        data = {
            "post_id": id,
            "comment_by": request.user.id,
            "content":request.data["content"]
        }
        serializer = CommentSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id):
        likes = Comment.objects.filter(post_id=id).count()
        return Response({
            "total_comments": likes
        }, status=status.HTTP_200_OK)
