from django.db.models import Model, ForeignKey, CASCADE, TextField, DateTimeField
from doctustech.user.models import User

# Create your models here.


class Post(Model):
    post_by = ForeignKey(User, related_name="post_by", on_delete=CASCADE)
    post_content = TextField()
    post_media = TextField()
    created = DateTimeField(auto_now_add=True, blank=True)


class Like(Model):
    post_id = ForeignKey(Post, related_name="postid", on_delete=CASCADE)
    liked_by = ForeignKey(User, related_name="likedby", on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True, blank=True)

class Comment(Model):
    post_id = ForeignKey(Post, related_name="post_id", on_delete=CASCADE)
    comment_by = ForeignKey(User, related_name="liked_by", on_delete=CASCADE)
    content = TextField()
    created = DateTimeField(auto_now_add=True, blank=True)