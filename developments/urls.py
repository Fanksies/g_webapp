from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('listado/', views.ProjectListView.as_view(), name='listado'),
    path('<slug:project_slug>/', views.ProjectDetailView.as_view(), name='detalle'),
]