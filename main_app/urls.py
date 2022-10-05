from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
 path('', views.Home.as_view(), name='home'),
 path('about/', views.About.as_view(), name="about"),
 path('finchcolls/', views.FinchcollList.as_view(), name="finchcoll_list"),
 path('finchcolls/new/', views.FinchcollCreate.as_view(), name="finchcoll_create"),
 path('finchcolls/<int:pk>/', views.FinchcollDetail.as_view(), name="finchcoll_detail"),
 path('finchcolls/<int:pk>/update', views.FinchcollUpdate.as_view(), name="finchcoll_update"),
 path('finchcolls/<int:pk>/delete',views.FinchcollDelete.as_view(), name="finchcoll_delete"),
 path('finchcolls/<int:pk>/location/new/',views.LocationCreate.as_view(), name="location_create"),
 path('seasons/<int:pk>/locations/<int:location_pk>/', 
views.SeasonLocationAssoc.as_view(), name="season_location_assoc"),
]
