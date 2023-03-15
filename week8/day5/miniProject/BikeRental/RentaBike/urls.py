from django.urls import path
# from django.conf.urls import re_path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('bikes/',views.bikespage,name='bikes'),
    path('book/',views.book, name='book'),
    # re_path(r'^status/(?P<id>\d{1,3} )/$',views.book_process),
    # re_path(r'^return_status/(?P<id>\d{1,3})/(?P<id1>\d{1,3})/$',views.return_process),
    path('cart/',views.cart)
]