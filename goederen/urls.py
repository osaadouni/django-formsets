from django.urls import path
from django.views.generic import RedirectView

from .views import GoederenCreateView, GoederenUpdateView, GoederenListView

urlpatterns = [
    #path('', RedirectView.as_view(url='add/')),
    path('', GoederenListView.as_view(), name='goederen-list'),
    path('add/',  GoederenCreateView.as_view(), name='goederen-create'),
    #path('edit/',  GoederenUpdaeView.as_view(), name='goederen-edit'),
]