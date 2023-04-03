from django.urls import path
from . import views
urlpatterns = [
    path('',views.add,name='home'),
    path('register/', views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name='logout'),
    path('movie/<int:movie_id/',views.detail,name='detail'),
]
