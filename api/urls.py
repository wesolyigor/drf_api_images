from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()
router.register('image', views.ImageUploadViewSet, basename='image')

urlpatterns = router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
