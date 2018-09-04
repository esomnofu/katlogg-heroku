from django.urls import path

from xpaths.views import Xpath, XpathDetail, XpathCrawl, XpathCrawlDetail, XpathStores

urlpatterns = [
    path('', Xpath.as_view()),
    path('crawl/', XpathCrawl.as_view()),
    path('stores/', XpathStores.as_view()),
    #path('crawl/<slug:pk>/', XpathCrawlDetail.as_view()),
    path('crawl/<int:pk>/', XpathCrawlDetail.as_view()),
    path('<int:pk>/', XpathDetail.as_view()),
]