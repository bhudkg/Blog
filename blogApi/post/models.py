from django.db import models

# Create your models here.

    

class PostModel(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=400)
    image = models.ImageField(
        upload_to="post/images",
        blank=True,
        null=True,
    )

    created_at = models.DateField(auto_now_add=True)
    uploaded_at = models.DateField(auto_now=True)
    


    def __str__(self):
        return self.title
    
class CommentsModel(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)