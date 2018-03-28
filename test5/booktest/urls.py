from django.conf.urls import url
import views

urlpatterns=[
    url(r'^uploadPic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle)
]