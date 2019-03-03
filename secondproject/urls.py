from django.contrib import admin
from django.urls import path, include
import blog.views
import portfolio.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.blog, name='blog'),

    path('blog/', include('blog.urls')),

    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)