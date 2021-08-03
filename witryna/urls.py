from django.urls import path
from . import views
#Url aplikacji Secret Present
app_name='witryna'
urlpatterns = [
	#Strona główna
	path("",views.index,name="index"),
	#Lista wydarzeń
	path("wydarzenia/",views.wydarzenia,name="wydarzenia"),
	#Dodawanie wydarzeń
	path("dod_wydarzenia/",views.dod_wydarzenia,name="dod_wydarzenia"),
	#Strona z wydarzeniem
	path("wydarzenie/<int:event_id>/",views.wydarzenie,name="wydarzenie"),
	#Dodawanie uczestników
	path("dod_uczestnik/<int:event_id>/",views.dod_uczestnik,name="dod_uczestnik"),
	#Losowanie kto komu dawać będzie prezent
	path("losowanie/<int:event_id>/",views.losowanie,name="losowanie"),
]
