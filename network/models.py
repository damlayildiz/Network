from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user") 
    text = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    likes = models.IntegerField(default=0)

    def getLikes(self):
        likes = Like.objects.filter(post=self)
        users = []

        for like in likes:
            users.append(like.user)

        return users

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likedpost")

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userwhofollow")
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userwhofollowed")