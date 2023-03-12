from django.urls import path
from . import views

# Authentications 
from .views import RegisterViewnew , product_list ,LoginView  , logoutUser

app_name = 'shop'

urlpatterns = [


     path('register/', RegisterViewnew.as_view(), name="register_user" ), 
     path('login/', LoginView.as_view() , name="login_page"),
     path('logout/', logoutUser, name="logout"),
     path('FAQ', views.FAQ, name="FAQ"),
     path('About', views.About, name="About"),

 
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),

]