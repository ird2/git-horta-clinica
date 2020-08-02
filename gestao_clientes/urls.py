
from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_urls
from apps.avaliacao import urls as avaliacao_urls
from apps.ofertas import urls as ofertas_urls
from apps.tratamento import urls as tratamento_urls
from django.conf import settings
from django.conf.urls.static import static
from apps.blog import views


urlpatterns = [
    path('blog/', views.HomepageView.as_view(), name='home1'),
    path('', include(home_urls)),
    path('', include(avaliacao_urls)),
    path('', include(ofertas_urls)),
    path('', include(tratamento_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

