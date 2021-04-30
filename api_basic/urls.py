from django.urls import path
from .views import article_list,article_detail, ArticleApiView, ArticleDetail

urlpatterns = [
    # path('article/', article_list, name="article"),
    path('article/', ArticleApiView.as_view(), name="article"),

    # path('detail/<int:pk>/', article_detail, name="detail")
    path('detail/<int:id>/', ArticleDetail.as_view(), name="detail")


]