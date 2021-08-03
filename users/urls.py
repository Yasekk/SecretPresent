from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#Url aplikacji users
app_name='users'
urlpatterns = [
	#Strona logowania
	path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
	#Wylogowanie
	path("logout/",views.logout_view,name="logout"),
	#Strona rejestracji
	path('register/',views.register,name='register'),
]
