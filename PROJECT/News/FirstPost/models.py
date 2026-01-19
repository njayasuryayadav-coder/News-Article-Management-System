from django.db import models
class NewsArticles(models.Model):
    articleId = models.IntegerField()
    articleImg = models.ImageField(upload_to='')
    articleName = models.CharField(max_length=100)
    articleContent = models.TextField()
    publishDate = models.DateField()
    authorId = models.IntegerField()
    
    def __str__(self):
        return self.articleName


