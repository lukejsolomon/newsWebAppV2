
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.allArticles, name='allArticles'),
    path('news', views.news, name='news'),
    path('<int:blog_id>/', views.articlePage, name='articlePage'),
    path('contributors/', views.contributors, name='contributors'),
    path('<int:blog_id>/', views.contributorsPage, name='contributorsPage'),
    path('podcasts/', views.podcasts, name='podcasts'),
    path('<int:blog_id>/', views.podcastPage, name='podcastPage'),





    # path('mission/', views.mission, name='mission'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
