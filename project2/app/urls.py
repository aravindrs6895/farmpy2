from django.urls import path
from . import views
app_name = "main"
urlpatterns=[
    path('', views.demo, name="demo"),

    path('zz',views.ace,name="add"),
    path('ss',views.ss,name='ss'),
    path('register',views.register_request,name="register"),
    path('login',views.login_request,name="login"),
    path('logout',views.logout_request,name="logout"),
]