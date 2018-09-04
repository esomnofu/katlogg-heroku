from django.urls import path, include
from . import views

#API CALLS MODULES IMPORT
from rest_framework.urlpatterns import format_suffix_patterns
#Import views if views is external to the App





#New API Tutorials Import
#Helps for GET, POST, PUT, DELETE
from rest_framework import routers

router = routers.DefaultRouter()

router.register('products', views.ProductView)



urlpatterns = [
    
   path('', views.index, name='index'),
   
   

    #path('products/', views.products, name='products'),
    path('crawl/', views.crawl, name='crawl'),


    #path('products/', views.products, name='products'),
    path('getXpaths/', views.getXpaths, name='getXpaths'),
    
    path('addstore/', views.addstore, name='addstore'),

    #path('products/', views.products, name='products'),
    path('train/', views.train, name='train'),

    #Form View
    path('form/', views.form, name='form'),
    #path('detail/<int:id>/', views.detail, name='detail'),
        
    #Search Query
    path('search/', views.search, name='search'),

    #NewsFeed Query
    path('newsfeed/', views.newsfeed, name='newsfeed'),

    #Increment In Price Query
    path('increase/', views.increase, name='increase'),

    #Reduction in Price Query
    path('reduce/', views.reduce, name='reduce'),

    #Change in Colors Query
    path('color/', views.color, name='color'),

    #Change in Size Query
    path('size/', views.size, name='size'),


    #Url for us to view Crawled Work
    path('dstesting/', views.dstesting, name="dstesting"),

    
    #Url for us to view Crawled Work
    path('unidentified/', views.unidentified, name="unidentified"),


    #ITEM BASED RECOMMENDATIONS URLS
    #ITEM BASED RECOMMENDATIONS URLS
    #ITEM BASED RECOMMENDATIONS URLS
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.loggedout, name='logout'),
    path('newsroom/', views.newsroom, name='newsroom'),
    path('create/', views.create, name='create'),
    path('recommend/', views.recommend, name='recommend'),






    #API BASED CALLED PATTERNS INCLUDE
    #API BASED CALLED PATTERNS INCLUDE
    #API BASED CALLED PATTERNS INCLUDE
    #API BASED CALLED PATTERNS INCLUDE
    path('apicalls/', views.ProductList.as_view(), name='apicalls'),
    
    path('newapis', include(router.urls))




]


#Import JSON Compatible Urlpatterns
#urlpatterns = format_suffix_patterns(urlpatterns)