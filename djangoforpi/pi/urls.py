from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_new, name='post_new'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)