from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orders/$', views.OrderList.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    url(r'^orders/pending/$', views.PendingOrderList.as_view()),
    url(r'^orders/due/$', views.DuePaymentOrderList.as_view()),
]

urlpatterns += [
    url(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url(r'^customer/$', views.CustomerList.as_view()),
    url(r'^customer/orders/(?P<pk>[0-9]+)/$', views.CustomerOrderList.as_view()),
]
