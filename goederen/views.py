from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.db import transaction

from .forms import GoederenNotitieForm, GoederenNotitieFormSet
from .models import GoederenNotitie, Goederen

# Create your views here.
class GoederenListView(ListView):
    #queryset = GoederenNotitie.objects.select_related('goederen')
    queryset = Goederen.objects.prefetch_related('notities')
    template_name = 'goederen/goederen_list.html'


class GoederenCreateView(CreateView):
    model = Goederen
    fields = ['naam']
    success_url = reverse_lazy('goederen-list')
    template_name = 'goederen/goederen_form.html'

    def get_context_data(self, **kwargs):
        data = super(GoederenCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['notities'] = GoederenNotitieFormSet(self.request.POST)
        else:
            data['notities'] = GoederenNotitieFormSet()
        print(data['notities'])
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        notities = context['notities']
        with transaction.atomic():
            self.object = form.save()

            if notities.is_valid():
                notities.instance = self.object
                notities.save()
        return super(GoederenCreateView, self).form_valid(form)


class GoederenUpdateView(CreateView):
    pass
