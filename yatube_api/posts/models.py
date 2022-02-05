from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,
                             verbose_name='Подписчик',
                             related_name='follower',
                             on_delete=models.CASCADE
                             )
    following = models.ForeignKey(User,
                                  related_name='following',
                                  verbose_name='Автор',
                                  on_delete=models.CASCADE
                                  )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['following', 'user'],
                condition=~models.Q(user=models.F('following')),
                name='no_self_subscription'
            ),
        ]
