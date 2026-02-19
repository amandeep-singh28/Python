from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StudentViewSet, ProdViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename = 'product')
router.register(r'students', StudentViewSet, basename = 'student')
router.register(r'prod', ProdViewSet, basename = 'prod')

urlpatterns = [
    path('', include(router.urls))
]