from django.urls import path, include
from publication.views import AuthorViewSet,BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

#URLConf
urlpatterns = [
    path('',include(router.urls))
]