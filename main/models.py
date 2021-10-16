from django.db import models

class Categories(models.Model):
    cat_title = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_title


class News(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=250)
    news_content = models.TextField(blank=True)
    news_create = models.DateField(auto_now_add=True)
    news_update = models.DateField(auto_now=True)
    news_image = models.ImageField(upload_to=f"photos/%Y/%m/%d/")

    def __str__(self):
        return self.news_title