from django.contrib import admin
from django.urls import path
from blog.views import home, article_list, article_detail, category_list
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    
    path('', home, name='home'),

   
    path('articles/', article_list, name='article_list'),

 
    path('articles/<int:pk>/', article_detail, name='article_detail'),

   
    path('categories/', category_list, name='category_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)