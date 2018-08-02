from django.urls import path
from . import views


urlpatterns=[
    path('index/', views.index_handler, name='index'),
    path('index/search/',views.Search, name='search'),
    path('article/<int:id>', views.detail_handler, name='detail'),
    path('article/<str:Blogtype>', views.article_with_type, name='article_with_type'),
    path('article/date/<int:year>/<int:month>', views.article_with_date, name='article_with_date')
]