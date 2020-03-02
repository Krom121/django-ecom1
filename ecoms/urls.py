from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from blog.views import PostListView, PostDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('affiliate.urls')),
    #### BLOG URLS ###
    path('blog/', PostListView.as_view(), name='list'),
    path('post/<slug>/<pk>/', PostDetailView.as_view(), name='post-detail'),
    ## OTHER BASE URLS FOR DEPENDENCIES #####
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
