from django.conf.urls import url
from school_app import views
urlpatterns = [
url(r'^school/$',views.school,name='school'),
url(r'^academics/$',views.academics,name='academics'),
url(r'^administration/$',views.administration,name='administration'),
url(r'^campusfacilites/$',views.campusfacilites,name='campusfacilites'),
url(r'^staff/$',views.staff,name='staff'),
url(r'^about/$',views.about,name='about'),

]
