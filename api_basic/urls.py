from django import urls
from django.db import router
from django.urls import path, include
from .views import article_list,article_detail, ArticleApiView, ArticleDetail, GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:id>/', include(router.urls)),

    # path('article/', article_list, name="article"),
    path('article/', ArticleApiView.as_view(), name="article"),
    path('generic/article/<int:id>/', GenericAPIView.as_view(), name="article"),

    # path('detail/<int:pk>/', article_detail, name="detail")
    path('detail/<int:id>/', ArticleDetail.as_view(), name="detail")


]