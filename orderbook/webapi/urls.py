from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    # url(r'^orders/$', views.OrderList.as_view()),
    url(r'^orders/new$', views.NewOrder.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    url(r'^orders/pending/$', views.PendingOrderList.as_view()),
    url(r'^orders/due/$', views.DuePaymentOrderList.as_view()),
]

urlpatterns += [
    url(r'^customer/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url(r'^customer/list$', views.CustomerList.as_view()),
    url(r'^customer/new$', views.NewCustomer.as_view()),
    url(r'^customer/(?P<pk>[0-9]+)/orders/$', views.CustomerOrderList.as_view()),
]

urlpatterns += [
    url(r'jwt-auth/$', obtain_jwt_token),
]
