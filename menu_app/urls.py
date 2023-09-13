from django.urls import path
from .views import MenuListView

urlpatterns = [
     path('', MenuListView.as_view(), name='menu_list'),
     path('menu/create/', MenuCreateView.as_view(), name='menu_create'),
]