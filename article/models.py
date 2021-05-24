from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, default='', blank=True)
    type = models.CharField(max_length=4, default="")
    by = models.CharField(max_length=200, default='', blank=True)
    link = models.URLField(default='', blank=True)
    profile = models.CharField(max_length=3, default='', blank=True)
    byProfile = models.TextField(default='', blank=True)
    profilePic = models.ImageField(
        upload_to='blog/images/', default='', blank=True)
    date = models.DateField(default='', blank=True)

# podcasts
    podcast = models.CharField(max_length=3, default='', blank=True)
    podcastSummary = models.CharField(max_length=200, default='', blank=True)


# blogPage
    articlePageImage = models.ImageField(
        upload_to='blog/images/', default='', blank=True)
    articlePageContent = models.TextField(default='', blank=True)

    articlePageImage2 = models.ImageField(
        upload_to='blog/images/', default='', blank=True)
    articlePageContent2 = models.TextField(default='', blank=True)

    articlePageImage3 = models.ImageField(
        upload_to='blog/images/', default='', blank=True)
    articlePageContent3 = models.TextField(default='', blank=True)

    def __str__(self):
        return self.title

    def showAuthor(self):
        return self.by
