from django.shortcuts import render
from .models import MenuItem
from .forms import MenuItemForm
from django.views.generic import ListView

class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu_list.html'
    context_object_name = 'menu_items'