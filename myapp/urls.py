from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/<int:page_id>', views.DetailView.as_view(), name='detail'),
]